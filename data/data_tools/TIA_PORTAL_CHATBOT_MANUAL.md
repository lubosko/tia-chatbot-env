# 🏭 TIA Portal AI Chatbot — Complete Installation Manual

> **Claude-assisted build guide** — Created from a real development session.
> All errors encountered during installation are documented as **⚠️ WATCH** warnings.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Prerequisites](#prerequisites)
3. [Phase 1 — Environment Setup](#phase-1--environment-setup)
4. [Phase 2 — Install Ollama + Qwen3](#phase-2--install-ollama--qwen3)
5. [Phase 3 — Python Dependencies](#phase-3--python-dependencies)
6. [Phase 4 — Knowledge Base (Ingestion)](#phase-4--knowledge-base-ingestion)
7. [Phase 5 — RAG Chain](#phase-5--rag-chain)
8. [Phase 6 — Gradio UI](#phase-6--gradio-ui)
9. [Phase 7 — Docker Containerization](#phase-7--docker-containerization)
10. [Project Structure Reference](#project-structure-reference)
11. [Troubleshooting Reference](#troubleshooting-reference)

---

## Architecture Overview

```
User Query
    ↓
Gradio Web UI  (app.py)
    ↓
LangChain RAG Chain  (chain.py)
    ↓              ↓
ChromaDB        Ollama / Qwen3
(vector search) (local LLM)
    ↓              ↓
         Answer + Sources
```

**Stack:**
| Component | Technology |
|---|---|
| Local LLM | Ollama + Qwen3 |
| Orchestration | LangChain |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers (local) |
| Web UI | Gradio 6 |
| Containerization | Docker + Docker Compose |

---

## Prerequisites

- macOS (M1/M2/M3 recommended, Intel supported)
- Python 3.11+ installed (`python3 --version`)
- Docker Desktop installed (for containerization phase)
- ~10GB free disk space (for models + vector DB)
- Internet connection (first-time model download only)

---

## Phase 1 — Environment Setup

### 1.1 Create Project Structure

```bash
mkdir tia-chatbot
cd tia-chatbot
mkdir -p data/raw vectordb src prompts
```

### 1.2 Create Virtual Environment

```bash
python3 -m venv tia-chatbot-env
source tia-chatbot-env/bin/activate
```

> ⚠️ **WATCH — Environment Not Active**
> Always verify your environment is active before installing packages or running scripts.
> Your terminal prompt must show the env name:
> ```
> # CORRECT ✅
> (tia-chatbot-env) user@Mac tia-chatbot %
>
> # WRONG ❌ — packages install to system Python
> user@Mac tia-chatbot %
> ```
> If not active, run: `source tia-chatbot-env/bin/activate`

---

## Phase 2 — Install Ollama + Qwen3

### 2.1 Install Ollama

```bash
brew install ollama
```

### 2.2 Pull Qwen3 Model

```bash
ollama pull qwen3
```

### 2.3 Start Ollama Service

```bash
ollama serve
```

> Keep this running in a dedicated terminal tab.

### 2.4 Verify Model Name

```bash
ollama list
```

You will see output like:

```
NAME          ID           SIZE
qwen3:8b      abc123...    5.2 GB
```

> ⚠️ **WATCH — Model Name Mismatch**
> The model name in your code **must exactly match** the output of `ollama list`.
> Common mistake: using `"qwen3"` in code when the actual name is `"qwen3:8b"`.
>
> **Error you will see:**
> ```
> ollama._types.ResponseError: model 'qwen3' not found (status code: 404)
> ```
>
> **Fix:** Update `OLLAMA_MODEL` in `src/chain.py`:
> ```python
> OLLAMA_MODEL = "qwen3:8b"   # use exact name from ollama list
> ```

---

## Phase 3 — Python Dependencies

### 3.1 Install All Packages

```bash
source tia-chatbot-env/bin/activate

pip3 install langchain
pip3 install langchain-community
pip3 install langchain-core
pip3 install langchain-ollama
pip3 install langchain-text-splitters
pip3 install chromadb
pip3 install sentence-transformers
pip3 install pypdf
pip3 install unstructured
pip3 install beautifulsoup4
pip3 install lxml
pip3 install gradio
pip3 install python-dotenv
```

Or install all at once using `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

**`requirements.txt` contents:**
```txt
langchain
langchain-community
langchain-core
langchain-ollama
langchain-text-splitters
chromadb
sentence-transformers
pypdf
unstructured
beautifulsoup4
lxml
gradio
python-dotenv
```

### 3.2 Test LangChain + Ollama Connection

Create `test_setup.py` in your project root:

```python
# test_setup.py
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:8b")  # use exact name from ollama list
response = llm.invoke("What is Siemens TIA Portal?")
print(response.content)
```

Run it:

```bash
python3 test_setup.py
```

> ⚠️ **WATCH — Missing langchain_ollama Module**
> ```
> ModuleNotFoundError: No module named 'langchain_ollama'
> ```
> **Fix:**
> ```bash
> pip3 install langchain-ollama
> ```
> Note the dash (`-`) in the pip name vs underscore (`_`) in the import.

> ⚠️ **WATCH — pip vs pip3**
> On macOS, `pip` may point to Python 2 or a different environment.
> Always use `pip3` or `python3 -m pip` inside your virtual environment.
>
> If `pip3` is not found at all:
> ```bash
> python3 -m ensurepip --upgrade
> ```

---

## Phase 4 — Knowledge Base (Ingestion)

### 4.1 Collect TIA Portal Documents

Add your documents to `data/raw/`. Supported formats:

| Format | Notes |
|---|---|
| `.pdf` | Official Siemens manuals — best source |
| `.md` | Custom notes, SCL snippets, how-to guides |
| `.txt` | Plain text references |
| `.html` | Exported web pages, forum content |

**Recommended documents to download** from `support.industry.siemens.com`:
- TIA Portal Getting Started Guide
- S7-1200 / S7-1500 System Manual
- SCL Programming Guide
- LAD/FBD/STL Reference Manual
- Error Codes Reference

> ✅ **TIP — Markdown files work great**
> `.md` files parse cleanly and headings (`#`, `##`) help the chunker
> split content logically. Use them for your own custom notes,
> SCL code examples, and troubleshooting tips.

### 4.2 Create `src/ingest.py`

```python
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

# ── Configuration ─────────────────────────────────────────────────
RAW_DATA_DIR  = Path("data/raw")
VECTOR_DB_DIR = Path("vectordb")
EMBED_MODEL   = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE    = 1000
CHUNK_OVERLAP = 200

def load_documents(data_dir: Path) -> list:
    all_docs = []
    loaders = {
        "PDF":      DirectoryLoader(str(data_dir), glob="**/*.pdf",
                        loader_cls=PyPDFLoader, show_progress=True,
                        use_multithreading=True),
        "Markdown": DirectoryLoader(str(data_dir), glob="**/*.md",
                        loader_cls=UnstructuredMarkdownLoader, show_progress=True),
        "Text":     DirectoryLoader(str(data_dir), glob="**/*.txt",
                        loader_cls=TextLoader, show_progress=True,
                        loader_kwargs={"encoding": "utf-8"}),
        "HTML":     DirectoryLoader(str(data_dir), glob="**/*.html",
                        loader_cls=UnstructuredHTMLLoader, show_progress=True),
    }
    for doc_type, loader in loaders.items():
        try:
            docs = loader.load()
            print(f"✅ {doc_type}: loaded {len(docs)} document(s)")
            all_docs.extend(docs)
        except Exception as e:
            print(f"⚠️  {doc_type}: skipped — {e}")
    return all_docs

def split_documents(docs: list) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    print(f"\n📄 Total chunks created: {len(chunks)}")
    return chunks

def build_vector_store(chunks: list):
    print(f"\n🔄 Loading embedding model: {EMBED_MODEL}")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL,
        model_kwargs={"device": "cpu"},   # change to "mps" for Apple Silicon
        encode_kwargs={"normalize_embeddings": True},
    )
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTOR_DB_DIR),
        collection_name="tia_portal_kb",
    )
    print(f"✅ Vector store saved — {vector_store._collection.count()} vectors")
    return vector_store

def main():
    print("=" * 50)
    print("   TIA Portal Knowledge Base — Ingestion")
    print("=" * 50)

    if not RAW_DATA_DIR.exists():
        print(f"❌ Directory not found: {RAW_DATA_DIR}")
        return

    file_counts = {
        "PDF":  len(list(RAW_DATA_DIR.rglob("*.pdf"))),
        "MD":   len(list(RAW_DATA_DIR.rglob("*.md"))),
        "TXT":  len(list(RAW_DATA_DIR.rglob("*.txt"))),
        "HTML": len(list(RAW_DATA_DIR.rglob("*.html"))),
    }

    print("\n📁 Files found in data/raw/:")
    for fmt, count in file_counts.items():
        print(f"   {'✅' if count > 0 else '—'} {fmt}: {count} file(s)")

    if sum(file_counts.values()) == 0:
        print("\n⚠️  No documents found. Add files to data/raw/ and retry.")
        return

    docs   = load_documents(RAW_DATA_DIR)
    chunks = split_documents(docs)
    build_vector_store(chunks)
    print("\n🎉 Ingestion complete!")

if __name__ == "__main__":
    main()
```

### 4.3 Run Ingestion

```bash
python3 src/ingest.py
```

> ⚠️ **WATCH — Wrong text_splitter Import Path**
> ```
> ModuleNotFoundError: No module named 'langchain.text_splitter'
> ```
> LangChain refactored modules into separate packages. The old import path no longer works.
>
> **Wrong (old):**
> ```python
> from langchain.text_splitter import RecursiveCharacterTextSplitter
> ```
> **Correct (new):**
> ```python
> from langchain_text_splitters import RecursiveCharacterTextSplitter
> ```
> Then install the package:
> ```bash
> pip3 install langchain-text-splitters
> ```

> ℹ️ **LangChain Import Reference**
> Many LangChain modules moved in v0.2+:
>
> | Old (broken) | New (correct) |
> |---|---|
> | `langchain.text_splitter` | `langchain_text_splitters` |
> | `langchain.embeddings` | `langchain_community.embeddings` |
> | `langchain.vectorstores` | `langchain_community.vectorstores` |
> | `langchain.document_loaders` | `langchain_community.document_loaders` |

---

## Phase 5 — RAG Chain

### 5.1 Create `src/chain.py`

```python
# src/chain.py
import os
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# ── Configuration ─────────────────────────────────────────────────
VECTOR_DB_DIR   = Path("vectordb")
EMBED_MODEL     = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL    = "qwen3:8b"          # must match: ollama list
OLLAMA_BASE_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")
TOP_K_RESULTS   = 5
TEMPERATURE     = 0.2

SYSTEM_PROMPT = """
You are an expert Siemens TIA Portal automation engineer assistant.
You have deep knowledge of:
- Siemens S7-1200 and S7-1500 PLC hardware and configuration
- TIA Portal software (V16, V17, V18, V19)
- Programming languages: SCL, LAD, FBD, STL, GRAPH
- Organization Blocks (OB1, OB30, OB35, OB40, etc.)
- Function Blocks (FB), Functions (FC), Data Blocks (DB)
- PROFINET, PROFIBUS, Industrial Ethernet networking
- HMI configuration (WinCC, KTP panels)
- Drive integration (SINAMICS)
- Diagnostics and error code interpretation

INSTRUCTIONS:
- Answer based on the provided context from TIA Portal documentation
- Always mention the source document when referencing documentation
- Format SCL/LAD code examples clearly in code blocks
- If unsure or context does not cover the question, say so clearly
- Use proper Siemens terminology

CONTEXT FROM DOCUMENTATION:
{context}
"""

def load_vector_store() -> Chroma:
    if not VECTOR_DB_DIR.exists():
        raise FileNotFoundError(
            f"❌ Vector DB not found at: {VECTOR_DB_DIR}\n"
            "   Run src/ingest.py first."
        )
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    return Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
        collection_name="tia_portal_kb",
    )

def format_docs(docs: list) -> str:
    formatted = []
    for i, doc in enumerate(docs, 1):
        source   = doc.metadata.get("source", "Unknown")
        page     = doc.metadata.get("page", "")
        page_str = f" (page {page})" if page else ""
        formatted.append(f"[{i}] Source: {source}{page_str}\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)

def format_history(history: list) -> list:
    messages = []
    for entry in history:
        if entry["role"] == "user":
            messages.append(HumanMessage(content=entry["content"]))
        elif entry["role"] == "assistant":
            messages.append(AIMessage(content=entry["content"]))
    return messages

def build_chain(vector_store: Chroma):
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K_RESULTS},
    )
    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=TEMPERATURE,
        num_ctx=4096,
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])
    chain = (
        RunnablePassthrough.assign(
            context=RunnableLambda(
                lambda x: format_docs(retriever.invoke(x["question"]))
            )
        )
        | RunnablePassthrough.assign(
            chat_history=RunnableLambda(
                lambda x: format_history(x.get("chat_history", []))
            )
        )
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain, retriever

class TIAChatbot:
    def __init__(self):
        print("\n" + "=" * 50)
        print("   TIA Portal AI Assistant — Loading")
        print("=" * 50 + "\n")
        self.vector_store = load_vector_store()
        print(f"✅ Vector store loaded — "
              f"{self.vector_store._collection.count()} vectors")
        self.chain, self.retriever = build_chain(self.vector_store)
        self.chat_history = []
        print("\n✅ Chatbot ready!\n")

    def ask(self, question: str) -> dict:
        source_docs = self.retriever.invoke(question)
        answer = self.chain.invoke({
            "question": question,
            "chat_history": self.chat_history,
        })
        self.chat_history.append({"role": "user",      "content": question})
        self.chat_history.append({"role": "assistant", "content": answer})
        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]

        sources = []
        for doc in source_docs:
            source = doc.metadata.get("source", "Unknown")
            page   = doc.metadata.get("page", "")
            entry  = f"{Path(source).name}" + (f" p.{page}" if page else "")
            if entry not in sources:
                sources.append(entry)

        return {"answer": answer, "sources": sources}

    def clear_history(self):
        self.chat_history = []
        print("🗑️  Conversation history cleared.")
```

### 5.2 Test the Chain

```bash
python3 src/chain.py
```

Expected output:
```
✅ Vector store loaded — 1,243 vectors
✅ Chatbot ready!

❓ What is the difference between FB and FC in TIA Portal?
💬 Answer: In TIA Portal, FB (Function Block) and FC (Function)...
📄 Sources: s7_1500_manual.pdf p.45
```

---

## Phase 6 — Gradio UI

### 6.1 Create `src/app.py`

```python
# src/app.py
import gradio as gr
from pathlib import Path
from chain import TIAChatbot

print("🚀 Starting TIA Portal AI Assistant...")
bot = TIAChatbot()

def chat(message: str, history: list) -> tuple:
    if not message.strip():
        return "", history
    result = bot.ask(message)
    answer = result["answer"]
    sources = result["sources"]
    if sources:
        answer += "\n\n📄 **Sources:** " + " | ".join(sources)
    history.append({"role": "user",      "content": message})
    history.append({"role": "assistant", "content": answer})
    return "", history

def clear_chat():
    bot.clear_history()
    return "", []

def get_vector_count() -> int:
    try:
        return bot.vector_store._collection.count()
    except Exception:
        return 0

def refresh_status() -> str:
    history_len = len(bot.chat_history) // 2
    return f"""
        <div class="status-bar-wrap">
            <div class="stat-item">
                <span class="stat-dot"></span><span>ONLINE</span>
            </div>
            <div class="stat-item">
                <span style="color:#4a7ab5;">&#9632;</span>
                <span>VECTORS: {get_vector_count()}</span>
            </div>
            <div class="stat-item">
                <span style="color:#4a7ab5;">&#9632;</span>
                <span>MODEL: QWEN3</span>
            </div>
            <div class="stat-item">
                <span style="color:#4a7ab5;">&#9632;</span>
                <span>HISTORY: {history_len} exchanges</span>
            </div>
        </div>
    """

EXAMPLE_QUESTIONS = [
    "What is the difference between FB and FC in TIA Portal?",
    "How do I configure PROFINET on S7-1500?",
    "Explain OB1, OB30 and OB35 organization blocks",
    "How to declare and use a Data Block in SCL?",
    "What does error code 16#8022 mean?",
    "How to set up S7 communication between two PLCs?",
    "Show me an example of a PID controller in SCL",
    "What is the difference between global DB and instance DB?",
]

CSS = """
body { background-color: #0a0e1a !important; }
.gradio-container {
    max-width: 1000px !important; margin: auto !important;
    font-family: 'Segoe UI', sans-serif !important;
    background-color: #0a0e1a !important;
}
footer { display: none !important; }
.header-box {
    background: linear-gradient(135deg, #001f4d 0%, #003399 60%, #0055cc 100%);
    border-radius: 8px; padding: 18px 28px; margin-bottom: 12px;
    border: 1px solid #0044bb;
    box-shadow: 0 4px 24px rgba(0,80,200,0.3);
}
.status-bar-wrap {
    background: #0d1526; border: 1px solid #1a2a4a;
    border-left: 4px solid #0055cc; border-radius: 6px;
    padding: 10px 16px; margin-bottom: 10px;
    display: flex; gap: 24px; align-items: center;
    font-size: 13px; color: #8aafd4;
    font-family: 'Courier New', monospace;
}
.stat-item { display: flex; align-items: center; gap: 6px; }
.stat-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #00cc66; box-shadow: 0 0 6px #00cc66; display: inline-block;
}
.send-btn {
    background: linear-gradient(135deg, #0044bb, #0066ff) !important;
    color: white !important; border-radius: 6px !important;
    font-weight: 600 !important; border: none !important;
}
.action-btn {
    background: #0d1a30 !important; color: #8aafd4 !important;
    border: 1px solid #1a2a4a !important; border-radius: 6px !important;
}
.section-label {
    color: #4a7ab5; font-size: 11px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    margin: 10px 0 6px 2px; font-family: 'Courier New', monospace;
}
.example-btn button {
    background: #0d1a30 !important; color: #7aaddd !important;
    border: 1px solid #1a3050 !important; border-radius: 5px !important;
    font-size: 12px !important;
}
.footer-bar {
    text-align: center; margin-top: 14px; font-size: 11px;
    color: #2a4a7a; letter-spacing: 1px;
    font-family: 'Courier New', monospace;
    border-top: 1px solid #0d1a30; padding-top: 10px;
}
"""

def build_ui():
    with gr.Blocks(css=CSS, title="TIA Portal AI Assistant") as demo:

        gr.HTML("""
            <div class="header-box">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="font-size:32px;">🏭</div>
                    <div>
                        <div style="font-size:22px; font-weight:700;
                                    color:#ffffff; letter-spacing:1px;">
                            TIA PORTAL AI ASSISTANT
                        </div>
                        <div style="font-size:12px; color:#7aaae0;
                                    letter-spacing:2px; margin-top:3px;
                                    font-family:'Courier New',monospace;">
                            QWEN3 | LANGCHAIN | CHROMADB | LOCAL INFERENCE
                        </div>
                    </div>
                </div>
            </div>
        """)

        status = gr.HTML(value=f"""
            <div class="status-bar-wrap">
                <div class="stat-item">
                    <span class="stat-dot"></span><span>ONLINE</span>
                </div>
                <div class="stat-item">
                    <span style="color:#4a7ab5;">&#9632;</span>
                    <span>VECTORS: {get_vector_count()}</span>
                </div>
                <div class="stat-item">
                    <span style="color:#4a7ab5;">&#9632;</span>
                    <span>MODEL: QWEN3</span>
                </div>
                <div class="stat-item">
                    <span style="color:#4a7ab5;">&#9632;</span>
                    <span>HISTORY: 0 exchanges</span>
                </div>
            </div>
        """)

        chatbot = gr.Chatbot(
            value=[], height=460, show_label=False,
            avatar_images=(
                None,
                "https://img.icons8.com/color/48/robot-2.png",
            ),
        )

        with gr.Row(elem_classes=["input-area"]):
            msg_input = gr.Textbox(
                placeholder="Enter query — TIA Portal, SCL, PROFINET, PLC diagnostics...",
                show_label=False, scale=9, lines=1, max_lines=4, autofocus=True,
            )
            send_btn = gr.Button("SEND ▶", scale=1, variant="primary",
                                 elem_classes=["send-btn"])

        with gr.Row():
            clear_btn   = gr.Button("⟳  CLEAR CHAT",     scale=1, elem_classes=["action-btn"])
            refresh_btn = gr.Button("↺  REFRESH STATUS", scale=1, elem_classes=["action-btn"])

        gr.HTML('<div class="section-label">// quick queries</div>')
        with gr.Row():
            for i in range(0, 4):
                gr.Button(EXAMPLE_QUESTIONS[i], elem_classes=["example-btn"]).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q, outputs=msg_input)
        with gr.Row():
            for i in range(4, 8):
                gr.Button(EXAMPLE_QUESTIONS[i], elem_classes=["example-btn"]).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q, outputs=msg_input)

        gr.HTML("""
            <div class="footer-bar">
                🔒 FULLY LOCAL — NO DATA SENT TO CLOUD |
                ANSWERS GROUNDED IN YOUR TIA PORTAL DOCUMENTATION
            </div>
        """)

        send_btn.click(fn=chat, inputs=[msg_input, chatbot],
                       outputs=[msg_input, chatbot])
        msg_input.submit(fn=chat, inputs=[msg_input, chatbot],
                         outputs=[msg_input, chatbot])
        clear_btn.click(fn=clear_chat, outputs=[msg_input, chatbot])
        refresh_btn.click(fn=refresh_status, outputs=status)

    return demo

if __name__ == "__main__":
    demo = build_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        inbrowser=True,
    )
```

### 6.2 Run the App

```bash
cd tia-chatbot
source tia-chatbot-env/bin/activate
python3 src/app.py
```

Open browser at: `http://localhost:7860`

> ⚠️ **WATCH — Gradio Module Not Found**
> ```
> ModuleNotFoundError: No module named 'gradio'
> ```
> **Fix:** Install inside your active virtual environment:
> ```bash
> source tia-chatbot-env/bin/activate
> pip3 install gradio
> ```
> Gradio is ~500MB — allow time for the download.

> ⚠️ **WATCH — Gradio 6: bubble_full_width removed**
> ```
> TypeError: Chatbot.__init__() got an unexpected keyword argument 'bubble_full_width'
> ```
> This parameter was removed in Gradio 6. Simply delete the line:
> ```python
> bubble_full_width=False,   # ← remove this line entirely
> ```

> ⚠️ **WATCH — Gradio 6: type parameter removed from Chatbot**
> ```
> TypeError: Chatbot.__init__() got an unexpected keyword argument 'type'
> ```
> In Gradio 6, `type="messages"` is the default and only format.
> The `type` parameter itself was removed from the constructor.
> Simply delete the line:
> ```python
> type="messages",   # ← remove this line entirely
> ```

> ⚠️ **WATCH — Gradio 6: Message format changed**
> ```
> gradio.exceptions.Error: "Data incompatible with messages format.
> Each message should be a dictionary with 'role' and 'content' keys"
> ```
> Gradio 6 dropped the old tuple format `(user_msg, bot_msg)`.
> Messages must now be dicts:
> ```python
> # WRONG — old tuple format
> history.append((message, answer))
>
> # CORRECT — Gradio 6 dict format
> history.append({"role": "user",      "content": message})
> history.append({"role": "assistant", "content": answer})
> ```
> Also update `clear_chat()`:
> ```python
> def clear_chat():
>     bot.clear_history()
>     return "", []   # returns (msg_input, chatbot)
> ```

---

## Phase 7 — Docker Containerization

### 7.1 Create `Dockerfile`

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY prompts/ ./prompts/

RUN mkdir -p data/raw vectordb

EXPOSE 7860

ENV OLLAMA_HOST=http://ollama:11434
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

CMD ["python", "src/app.py"]
```

### 7.2 Create `docker-compose.yml`

```yaml
version: "3.9"

services:

  ollama:
    image: ollama/ollama:latest
    container_name: tia-ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434"]
      interval: 10s
      timeout: 5s
      retries: 5

  chatbot:
    build: .
    container_name: tia-chatbot
    ports:
      - "7860:7860"
    volumes:
      - ./data:/app/data
      - ./vectordb:/app/vectordb
    environment:
      - OLLAMA_HOST=http://ollama:11434
    depends_on:
      ollama:
        condition: service_healthy
    restart: unless-stopped

volumes:
  ollama_data:
```

### 7.3 Create `.dockerignore`

```
tia-chatbot-env/
__pycache__/
*.pyc
.env
.DS_Store
vectordb/
data/raw/
```

### 7.4 Build and Launch

```bash
# Build and start all services
docker compose up --build

# Pull Qwen3 into the Ollama container (first time only)
docker exec -it tia-ollama ollama pull qwen3:8b

# Run ingestion inside the chatbot container
docker exec -it tia-chatbot python src/ingest.py
```

Open browser at: `http://localhost:7860`

### 7.5 Useful Docker Commands

```bash
# Start in background
docker compose up -d

# View live logs
docker compose logs -f chatbot
docker compose logs -f ollama

# Stop everything
docker compose down

# Rebuild after code changes (chatbot only)
docker compose up --build chatbot

# Open shell inside container
docker exec -it tia-chatbot bash
```

> ⚠️ **WATCH — Python Version in Docker**
> Use `python:3.11-slim` in your Dockerfile, NOT Python 3.14.
> Python 3.14 caused multiple compatibility issues with LangChain,
> ChromaDB and Gradio during development. Python 3.11 is stable
> and fully supported by all dependencies.

> ✅ **TIP — Apple Silicon (M1/M2/M3) GPU**
> Add this to the `ollama` service for faster inference:
> ```yaml
> deploy:
>   resources:
>     reservations:
>       devices:
>         - capabilities: [gpu]
> ```

---

## Project Structure Reference

```
tia-chatbot/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── test_setup.py
├── data/
│   └── raw/                    # ← add your PDFs, MDs, TXTs here
│       ├── s7_1500_manual.pdf
│       ├── scl_guide.pdf
│       ├── error_codes.md
│       └── custom_notes.md
├── vectordb/                   # ← auto-created by ingest.py
├── src/
│   ├── ingest.py               # Phase 4 — document ingestion
│   ├── chain.py                # Phase 5 — RAG pipeline
│   └── app.py                  # Phase 6 — Gradio UI
├── prompts/
│   └── system.txt              # optional: externalize system prompt
└── tia-chatbot-env/            # virtual environment (not in Docker)
```

---

## Troubleshooting Reference

| Error | Cause | Fix |
|---|---|---|
| `No module named 'langchain_ollama'` | Package not installed | `pip3 install langchain-ollama` |
| `No module named 'langchain.text_splitter'` | Old import path | Use `from langchain_text_splitters import ...` + `pip3 install langchain-text-splitters` |
| `model 'qwen3' not found (404)` | Wrong model name | Run `ollama list`, use exact name in code |
| `No module named 'gradio'` | Not installed in venv | Activate venv, then `pip3 install gradio` |
| `unexpected keyword argument 'bubble_full_width'` | Removed in Gradio 6 | Delete that line |
| `unexpected keyword argument 'type'` | Removed in Gradio 6 | Delete that line |
| `Data incompatible with messages format` | Old tuple format | Use `{"role": ..., "content": ...}` dicts |
| `pip` not found | macOS Python setup | Use `pip3` or `python3 -m pip` |
| Vector DB not found | ingest.py not run yet | Run `python3 src/ingest.py` first |

---

## Quality Tuning Guide

Once running, use these levers to improve answer quality:

| Problem | Solution |
|---|---|
| Wrong or vague answers | Improve system prompt in `chain.py` |
| Missing context | Reduce `CHUNK_SIZE`, increase `CHUNK_OVERLAP` |
| Too slow on CPU | Use smaller model or enable MPS (Apple Silicon) |
| Hallucinations | Lower `TEMPERATURE` to `0.1` |
| Poor PDF parsing | Switch to `unstructured` loader |
| Answers ignore docs | Increase `TOP_K_RESULTS` from 5 to 8 |

---

*Built with Claude — Anthropic's AI assistant*
*Session date: April 2026*
