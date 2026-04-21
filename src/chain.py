# src/chain.py
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# ── Configuration ────────────────────────────────────────────────
VECTOR_DB_DIR  = Path("vectordb")
EMBED_MODEL    = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL   = "qwen3:8b"       # ← use your exact model name from ollama list
TOP_K_RESULTS  = 5                # number of chunks retrieved per query
TEMPERATURE    = 0.2              # low = more factual, high = more creative

# ── TIA Portal System Prompt ─────────────────────────────────────
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
- TIA Portal libraries and reusable components

INSTRUCTIONS:
- Answer questions based on the provided context from TIA Portal documentation
- If the context contains relevant information, use it to give a precise answer
- Always mention the source document when referencing documentation
- For SCL/LAD code examples, format them clearly in code blocks
- If you are unsure or the context does not cover the question, say so clearly
- Keep answers structured and practical for automation engineers
- Use proper Siemens terminology

CONTEXT FROM DOCUMENTATION:
{context}
"""

# ── Load Vector Store ─────────────────────────────────────────────
def load_vector_store() -> Chroma:
    if not VECTOR_DB_DIR.exists():
        raise FileNotFoundError(
            f"❌ Vector DB not found at: {VECTOR_DB_DIR}\n"
            "   Run src/ingest.py first to build the knowledge base."
        )

    print(f"🗄️  Loading vector store from: {VECTOR_DB_DIR}")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL,
        model_kwargs={"device": "mps"},     # change to "mps" for Apple Silicon
        encode_kwargs={"normalize_embeddings": True},
    )

    vector_store = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
        collection_name="tia_portal_kb",
    )

    count = vector_store._collection.count()
    print(f"✅ Vector store loaded — {count} vectors available")
    return vector_store


# ── Format Retrieved Documents ────────────────────────────────────
def format_docs(docs: list) -> str:
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "Unknown source")
        page   = doc.metadata.get("page", "")
        page_str = f" (page {page})" if page else ""
        formatted.append(
            f"[{i}] Source: {source}{page_str}\n"
            f"{doc.page_content}"
        )
    return "\n\n---\n\n".join(formatted)


# ── Format Chat History ───────────────────────────────────────────
def format_history(history: list) -> list:
    messages = []
    for entry in history:
        if entry["role"] == "user":
            messages.append(HumanMessage(content=entry["content"]))
        elif entry["role"] == "assistant":
            messages.append(AIMessage(content=entry["content"]))
    return messages


# ── Build RAG Chain ───────────────────────────────────────────────
def build_chain(vector_store: Chroma):
    # Retriever — fetches top K relevant chunks
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K_RESULTS},
    )

    # LLM
    llm = ChatOllama(
        model=OLLAMA_MODEL,
        temperature=TEMPERATURE,
        num_ctx=4096,           # context window size
    )

    # Prompt template with chat history support
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    # Full RAG chain
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


# ── TIA Portal Chatbot Class ──────────────────────────────────────
class TIAChatbot:
    def __init__(self):
        print("\n" + "=" * 50)
        print("   TIA Portal AI Assistant — Loading")
        print("=" * 50 + "\n")

        self.vector_store = load_vector_store()
        self.chain, self.retriever = build_chain(self.vector_store)
        self.chat_history = []
        print("\n✅ Chatbot ready!\n")

    def ask(self, question: str, show_sources: bool = True) -> dict:
        # Get relevant source documents
        source_docs = self.retriever.invoke(question)

        # Run RAG chain
        answer = self.chain.invoke({
            "question": question,
            "chat_history": self.chat_history,
        })

        # Update chat history
        self.chat_history.append({"role": "user",      "content": question})
        self.chat_history.append({"role": "assistant", "content": answer})

        # Keep history manageable (last 10 exchanges)
        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]

        # Extract source references
        sources = []
        for doc in source_docs:
            source = doc.metadata.get("source", "Unknown")
            page   = doc.metadata.get("page", "")
            entry  = f"{Path(source).name}" + (f" p.{page}" if page else "")
            if entry not in sources:
                sources.append(entry)

        return {
            "answer":  answer,
            "sources": sources,
        }

    def clear_history(self):
        self.chat_history = []
        print("🗑️  Conversation history cleared.")


# ── Quick CLI Test ────────────────────────────────────────────────
if __name__ == "__main__":
    bot = TIAChatbot()

    test_questions = [
        "What is the difference between FB and FC in TIA Portal?",
        "How do I declare a Data Block in SCL?",
        "What is OB1 used for?",
    ]

    for question in test_questions:
        print(f"\n{'='*50}")
        print(f"❓ {question}")
        print(f"{'='*50}")

        result = bot.ask(question)

        print(f"\n💬 Answer:\n{result['answer']}")
        print(f"\n📄 Sources: {', '.join(result['sources']) if result['sources'] else 'No sources found'}")