#!/usr/bin/env python3
"""
TIA Portal Scraper - docs.tia.siemens.cloud
Saves one .md file per top-level TOC section, matching existing structure.

Usage:
    cd /Users/test/tia-chatbot-env
    python scraper.py
"""

import asyncio
import json
import re
import os
from pathlib import Path
from playwright.async_api import async_playwright
from markdownify import markdownify as md_convert

# ── Config ────────────────────────────────────────────────────────────────────
BASE_URL        = "https://docs.tia.siemens.cloud"
COLLECTION      = "simatic_s7_1200_manual_collection_eses_20"
ENTRY_URL       = f"{BASE_URL}/r/{COLLECTION}/programming-concepts"
OUTPUT_DIR      = Path("/Users/test/tia-chatbot-env/data/raw/files/output")
MAP_ID          = "VBkTPlmjVZAl17lebjV9hA"   # discovered from network requests
DELAY           = 0.8   # seconds between topic fetches
SKIP_EXISTING   = True  # resume support

# ── HTML → Markdown ───────────────────────────────────────────────────────────
def html_to_md(html: str, depth: int = 0) -> str:
    if not html or html.strip() in ("{}", ""):
        return ""
    text = md_convert(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "button", "nav", "aside"],
        newline_style="backslash",
    )
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ── Flatten TOC tree ──────────────────────────────────────────────────────────
def flatten_toc(pages_data: dict) -> list[dict]:
    """
    Returns list of:
      { section_slug, title, content_id, depth, pretty_url }
    grouped by top-level section.
    """
    result = []

    def walk(items, section_slug, depth):
        for item in items:
            url = item.get("prettyUrl", "")
            slug = url.rstrip("/").split("/")[-1]
            result.append({
                "section_slug": section_slug or slug,
                "slug": slug,
                "title": item.get("title", slug),
                "content_id": item.get("contentId", ""),
                "depth": depth,
                "pretty_url": url,
            })
            children = item.get("children") or item.get("pageToc") or []
            walk(children, section_slug or slug, depth + 1)

    for top_item in pages_data.get("paginatedToc", []):
        top_url = top_item.get("prettyUrl", "")
        top_slug = top_url.rstrip("/").split("/")[-1]
        result.append({
            "section_slug": top_slug,
            "slug": top_slug,
            "title": top_item.get("title", top_slug),
            "content_id": top_item.get("contentId", ""),
            "depth": 0,
            "pretty_url": top_url,
        })
        for child in top_item.get("pageToc", []):
            walk([child], top_slug, 1)

    return result


# ── Main ──────────────────────────────────────────────────────────────────────
async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )
        page = await context.new_page()

        # ── 1. Load entry page to establish session ──────────────────────────
        print("Loading entry page to establish session…")
        await page.goto(ENTRY_URL, wait_until="networkidle", timeout=45_000)
        print("Session established.")

        # ── 2. Fetch full TOC via API ────────────────────────────────────────
        print("Fetching TOC…")
        pages_resp = await page.evaluate(
            """async (mapId) => {
                const r = await fetch('/api/khub/maps/' + mapId + '/pages');
                return await r.json();
            }""",
            MAP_ID,
        )
        topics = flatten_toc(pages_resp)
        print(f"Found {len(topics)} topics across "
              f"{len(set(t['section_slug'] for t in topics))} sections.")

        # ── 3. Group topics by top-level section ─────────────────────────────
        sections: dict[str, list] = {}
        for t in topics:
            sections.setdefault(t["section_slug"], []).append(t)

        # ── 4. Scrape each section → one .md file ────────────────────────────
        for section_slug, section_topics in sections.items():
            out_path = OUTPUT_DIR / f"{section_slug}.md"

            if SKIP_EXISTING and out_path.exists():
                print(f"  ⏭  Skipping {out_path.name} (exists)")
                continue

            print(f"\n📄 Section: {section_slug} ({len(section_topics)} topics)")
            parts = []

            for topic in section_topics:
                cid = topic["content_id"]
                title = topic["title"]
                depth = topic["depth"]
                print(f"   {'  ' * depth}→ {title}")

                if not cid:
                    continue

                # Fetch topic HTML via the khub API using page context
                try:
                    html = await page.evaluate(
                        """async ([mapId, contentId]) => {
                            const url = '/api/khub/maps/' + mapId + '/topics/' + contentId + '/content?target=DESIGNED_READER';
                            const r = await fetch(url);
                            if (!r.ok) return '';
                            return await r.text();
                        }""",
                        [MAP_ID, cid],
                    )
                except Exception as e:
                    print(f"     ⚠ fetch error: {e}")
                    html = ""

                body = html_to_md(html, depth)
                heading = "#" * (depth + 1)
                parts.append(f"{heading} {title}\n\n{body}" if body else f"{heading} {title}\n")

                await asyncio.sleep(DELAY)

            if parts:
                full_md = "\n\n---\n\n".join(parts)
                out_path.write_text(full_md, encoding="utf-8")
                print(f"   ✅ Written → {out_path}")
            else:
                print(f"   ⚠  No content for {section_slug}")

        await browser.close()
        print("\n🎉 Scraping complete!")


if __name__ == "__main__":
    asyncio.run(main())
