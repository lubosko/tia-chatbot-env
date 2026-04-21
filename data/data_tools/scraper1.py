#!/usr/bin/env python3
"""
TIA Portal Scraper - docs.tia.siemens.cloud
One .md file per top-level TOC section, matching your existing structure.

Save to:  /Users/test/tia-chatbot-env/scraper.py
Run with: cd /Users/test/tia-chatbot-env && python scraper.py
"""

import asyncio
import json
import re
from pathlib import Path
from playwright.async_api import async_playwright
from markdownify import markdownify as md_convert

# ── Config ────────────────────────────────────────────────────────────────────
BASE_URL   = "https://docs.tia.siemens.cloud"
COLLECTION = "simatic_s7_1200_manual_collection_eses_20"
ENTRY_URL  = f"{BASE_URL}/r/{COLLECTION}/programming-concepts"
OUTPUT_DIR = Path("/Users/test/tia-chatbot-env/data/raw/files/output")
MAP_ID     = "VBkTPlmjVZAl17lebjV9hA"
DELAY      = 0.8     # polite delay between topic fetches (seconds)
SKIP_EXISTING = True # set False to re-scrape everything


# ── HTML → Markdown ───────────────────────────────────────────────────────────
def html_to_md(html: str) -> str:
    if not html or not html.strip() or html.strip().startswith("{"):
        return ""
    text = md_convert(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "button", "nav", "aside"],
    )
    # collapse 3+ blank lines to 2
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ── Flatten TOC tree ──────────────────────────────────────────────────────────
def flatten_toc(pages_data: dict) -> list[dict]:
    """
    Returns flat list of topic dicts:
      { section_slug, title, content_id, depth }
    All topics share the section_slug of their top-level parent.
    """
    result = []

    def walk(items: list, section_slug: str, depth: int):
        for item in items:
            result.append({
                "section_slug": section_slug,
                "title":        item.get("title", ""),
                "content_id":   item.get("contentId", ""),
                "depth":        depth,
            })
            children = item.get("children") or []
            if children:
                walk(children, section_slug, depth + 1)

    for top in pages_data.get("paginatedToc", []):
        url       = top.get("prettyUrl", "")
        top_slug  = url.rstrip("/").split("/")[-1]

        result.append({
            "section_slug": top_slug,
            "title":        top.get("title", top_slug),
            "content_id":   top.get("contentId", ""),
            "depth":        0,
        })
        walk(top.get("pageToc", []), top_slug, 1)

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

        # 1. Load entry page → establishes session cookies
        print("⏳ Loading entry page (establishing session)…")
        await page.goto(ENTRY_URL, wait_until="networkidle", timeout=45_000)
        print("✅ Session ready.\n")

        # 2. Fetch full TOC via the khub API
        print("⏳ Fetching TOC from API…")
        pages_json = await page.evaluate(
            """async (mapId) => {
                const r = await fetch('/api/khub/maps/' + mapId + '/pages');
                return await r.json();
            }""",
            MAP_ID,
        )
        topics = flatten_toc(pages_json)
        sections = {}
        for t in topics:
            sections.setdefault(t["section_slug"], []).append(t)

        total_topics   = len(topics)
        total_sections = len(sections)
        print(f"✅ {total_topics} topics in {total_sections} sections.\n")

        # 3. For each section, scrape all topics → write one .md file
        for i, (section_slug, section_topics) in enumerate(sections.items(), 1):
            out_path = OUTPUT_DIR / f"{section_slug}.md"

            if SKIP_EXISTING and out_path.exists():
                print(f"[{i}/{total_sections}] ⏭  {out_path.name}  (skipped – exists)")
                continue

            print(f"[{i}/{total_sections}] 📄 {section_slug}.md  ({len(section_topics)} topics)")
            parts = []

            for topic in section_topics:
                cid   = topic["content_id"]
                title = topic["title"]
                depth = topic["depth"]
                indent = "  " * depth
                print(f"   {indent}→ {title}")

                if not cid:
                    hashes = "#" * (depth + 1)
                    parts.append(f"{hashes} {title}\n")
                    continue

                # Fetch content HTML via existing session
                html = await page.evaluate(
                    """async ([mapId, contentId]) => {
                        try {
                            const url = '/api/khub/maps/' + mapId
                                      + '/topics/' + contentId
                                      + '/content?target=DESIGNED_READER';
                            const r = await fetch(url);
                            if (!r.ok) return '';
                            return await r.text();
                        } catch(e) {
                            return '';
                        }
                    }""",
                    [MAP_ID, cid],
                )

                body   = html_to_md(html)
                hashes = "#" * (depth + 1)

                if body:
                    parts.append(f"{hashes} {title}\n\n{body}")
                else:
                    parts.append(f"{hashes} {title}\n")

                await asyncio.sleep(DELAY)

            if parts:
                full_md = "\n\n---\n\n".join(parts)
                out_path.write_text(full_md, encoding="utf-8")
                print(f"   ✅ Written → {out_path.name}\n")
            else:
                print(f"   ⚠  No content captured for {section_slug}\n")

        await browser.close()
        print("🎉  All done!")


if __name__ == "__main__":
    asyncio.run(main())