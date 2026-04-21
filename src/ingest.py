# src/ingest.py
import os
from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredMarkdownLoader,
    TextLoader,
    UnstructuredHTMLLoader,
    DirectoryLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# ── Configuration ────────────────────────────────────────────────
RAW_DATA_DIR   = Path("/Users/test/tia-chatbot-env/data/raw")
VECTOR_DB_DIR  = Path("vectordb")
EMBED_MODEL    = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE     = 1000
CHUNK_OVERLAP  = 200

# ── Document Loaders ─────────────────────────────────────────────
def load_documents(data_dir: Path) -> list:
    all_docs = []

    # PDF loader
    pdf_loader = DirectoryLoader(
        str(data_dir),
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True,
    )

    # Markdown loader
    md_loader = DirectoryLoader(
        str(data_dir),
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        show_progress=True,
    )

    # Text loader
    txt_loader = DirectoryLoader(
        str(data_dir),
        glob="**/*.txt",
        loader_cls=TextLoader,
        show_progress=True,
        loader_kwargs={"encoding": "utf-8"},
    )

    # HTML loader
    html_loader = DirectoryLoader(
        str(data_dir),
        glob="**/*.html",
        loader_cls=UnstructuredHTMLLoader,
        show_progress=True,
    )

    loaders = {
        "PDF":      pdf_loader,
        "Markdown": md_loader,
        "Text":     txt_loader,
        "HTML":     html_loader,
    }

    for doc_type, loader in loaders.items():
        try:
            docs = loader.load()
            print(f"✅ {doc_type}: loaded {len(docs)} document(s)")
            all_docs.extend(docs)
        except Exception as e:
            print(f"⚠️  {doc_type}: skipped — {e}")

    return all_docs


# ── Text Splitter ─────────────────────────────────────────────────
def split_documents(docs: list) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""],  # respects paragraphs first
    )
    chunks = splitter.split_documents(docs)
    print(f"\n📄 Total chunks created: {len(chunks)}")
    return chunks


# ── Embeddings & Vector Store ─────────────────────────────────────
def build_vector_store(chunks: list):
    print(f"\n🔄 Loading embedding model: {EMBED_MODEL}")
    print("   (first run downloads ~90MB — please wait...)\n")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL,
        model_kwargs={"device": "cpu"},       # change to "mps" for Apple Silicon GPU
        encode_kwargs={"normalize_embeddings": True},
    )

    print("🗄️  Building ChromaDB vector store...")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTOR_DB_DIR),
        collection_name="tia_portal_kb",
    )

    print(f"✅ Vector store saved to: {VECTOR_DB_DIR}/")
    print(f"✅ Total vectors stored:  {vector_store._collection.count()}")
    return vector_store


# ── Main ──────────────────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   TIA Portal Knowledge Base — Ingestion")
    print("=" * 50)

    # Check data directory exists
    if not RAW_DATA_DIR.exists():
        print(f"❌ Data directory not found: {RAW_DATA_DIR}")
        print("   Create it and add your documents first.")
        return

    # Count available files
    file_counts = {
        "PDF":  len(list(RAW_DATA_DIR.rglob("*.pdf"))),
        "MD":   len(list(RAW_DATA_DIR.rglob("*.md"))),
        "TXT":  len(list(RAW_DATA_DIR.rglob("*.txt"))),
        "HTML": len(list(RAW_DATA_DIR.rglob("*.html"))),
    }

    print("\n📁 Files found in data/raw/:")
    for fmt, count in file_counts.items():
        status = "✅" if count > 0 else "—"
        print(f"   {status} {fmt}: {count} file(s)")

    total = sum(file_counts.values())
    if total == 0:
        print("\n⚠️  No documents found. Add files to data/raw/ and retry.")
        return

    print(f"\n   Total: {total} file(s) to process\n")

    # Run pipeline
    docs   = load_documents(RAW_DATA_DIR)
    chunks = split_documents(docs)
    build_vector_store(chunks)

    print("\n🎉 Ingestion complete! Ready for RAG pipeline.")
    print(f"   Vector DB location: {VECTOR_DB_DIR}/")


if __name__ == "__main__":
    main()
