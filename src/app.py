# src/app.py
import gradio as gr
from pathlib import Path
from chain import TIAChatbot

# ── Initialize Chatbot ────────────────────────────────────────────
print("🚀 Starting TIA Portal AI Assistant...")
bot = TIAChatbot()

# ── Chat Function ─────────────────────────────────────────────────
def chat(message: str, history: list) -> tuple:
    if not message.strip():
        return "", history

    result = bot.ask(message)
    answer = result["answer"]
    sources = result["sources"]

    if sources:
        sources_text = "\n\n📄 **Sources:** " + " | ".join(sources)
        answer += sources_text

    history.append({"role": "user",      "content": message})
    history.append({"role": "assistant", "content": answer})
    return "", history

def clear_chat():
    bot.clear_history()
    return "", []


# ── Status Info ───────────────────────────────────────────────────
def get_status() -> str:
    try:
        count = bot.vector_store._collection.count()
        history_len = len(bot.chat_history) // 2
        return (
            f"🟢 Online  |  "
            f"📚 {count} vectors  |  "
            f"💬 {history_len} exchanges in history  |  "
            f"🤖 Qwen3"
        )
    except Exception:
        return "🔴 Error loading status"


# ── Example Questions ─────────────────────────────────────────────
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


# ── Custom CSS ────────────────────────────────────────────────────
CSS = """
body {
    background-color: #0a0e1a !important;
}
.gradio-container {
    max-width: 1000px !important;
    margin: auto !important;
    font-family: 'Segoe UI', sans-serif !important;
    background-color: #0a0e1a !important;
}
footer { display: none !important; }

.header-box {
    background: linear-gradient(135deg, #001f4d 0%, #003399 60%, #0055cc 100%);
    border-radius: 8px;
    padding: 18px 28px;
    margin-bottom: 12px;
    border: 1px solid #0044bb;
    box-shadow: 0 4px 24px rgba(0,80,200,0.3);
}

.status-bar-wrap {
    background: #0d1526;
    border: 1px solid #1a2a4a;
    border-left: 4px solid #0055cc;
    border-radius: 6px;
    padding: 10px 16px;
    margin-bottom: 10px;
    display: flex;
    gap: 24px;
    align-items: center;
    font-size: 13px;
    color: #8aafd4;
    font-family: 'Courier New', monospace;
}

.stat-item {
    display: flex;
    align-items: center;
    gap: 6px;
}

.stat-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00cc66;
    box-shadow: 0 0 6px #00cc66;
    display: inline-block;
}

.gradio-chatbot {
    background: #0d1526 !important;
    border: 1px solid #1a2a4a !important;
    border-radius: 8px !important;
}

/* User message */
.message-wrap .user {
    background: #0a2150 !important;
    border: 1px solid #1a3a6a !important;
    border-radius: 8px !important;
    color: #cce0ff !important;
}

/* Bot message */
.message-wrap .bot {
    background: #0d1a30 !important;
    border: 1px solid #1a2a4a !important;
    border-radius: 8px !important;
    color: #e0eeff !important;
}

.input-area textarea {
    background: #0d1526 !important;
    border: 1px solid #1a3a6a !important;
    border-radius: 6px !important;
    color: #cce0ff !important;
    font-size: 14px !important;
}
.input-area textarea:focus {
    border-color: #0055cc !important;
    box-shadow: 0 0 0 2px rgba(0,85,204,0.3) !important;
}

.send-btn {
    background: linear-gradient(135deg, #0044bb, #0066ff) !important;
    color: white !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    border: none !important;
    box-shadow: 0 2px 8px rgba(0,80,200,0.4) !important;
}
.send-btn:hover {
    background: linear-gradient(135deg, #0055cc, #0077ff) !important;
}

.action-btn {
    background: #0d1a30 !important;
    color: #8aafd4 !important;
    border: 1px solid #1a2a4a !important;
    border-radius: 6px !important;
}
.action-btn:hover {
    border-color: #0055cc !important;
    color: #cce0ff !important;
}

.section-label {
    color: #4a7ab5;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 10px 0 6px 2px;
    font-family: 'Courier New', monospace;
}

.example-btn button {
    background: #0d1a30 !important;
    color: #7aaddd !important;
    border: 1px solid #1a3050 !important;
    border-radius: 5px !important;
    font-size: 12px !important;
    padding: 6px 10px !important;
    text-align: left !important;
}
.example-btn button:hover {
    border-color: #0055cc !important;
    color: #cce0ff !important;
    background: #0a2150 !important;
}

.footer-bar {
    text-align: center;
    margin-top: 14px;
    font-size: 11px;
    color: #2a4a7a;
    letter-spacing: 1px;
    font-family: 'Courier New', monospace;
    border-top: 1px solid #0d1a30;
    padding-top: 10px;
}
"""

# ── Build UI ──────────────────────────────────────────────────────
def build_ui():
    with gr.Blocks(
        css=CSS,
        title="TIA Portal AI Assistant",
    ) as demo:

        # ── Header ────────────────────────────────────────────────
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
                            QWEN3 &nbsp;|&nbsp; LANGCHAIN &nbsp;|&nbsp;
                            CHROMADB &nbsp;|&nbsp; LOCAL INFERENCE
                        </div>
                    </div>
                </div>
            </div>
        """)

        # ── Status Bar ────────────────────────────────────────────
        status = gr.HTML(value=f"""
            <div class="status-bar-wrap">
                <div class="stat-item">
                    <span class="stat-dot"></span>
                    <span>ONLINE</span>
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

        # ── Chat Window ───────────────────────────────────────────
        chatbot = gr.Chatbot(
            value=[],
            height=460,
            show_label=False,
            avatar_images=(
                None,
                "https://img.icons8.com/color/48/robot-2.png",
            ),
        )

        # ── Input Row ─────────────────────────────────────────────
        with gr.Row(elem_classes=["input-area"]):
            msg_input = gr.Textbox(
                placeholder="Enter query — TIA Portal, SCL, PROFINET, PLC diagnostics...",
                show_label=False,
                scale=9,
                lines=1,
                max_lines=4,
                autofocus=True,
            )
            send_btn = gr.Button(
                "SEND ▶",
                scale=1,
                variant="primary",
                elem_classes=["send-btn"],
            )

        # ── Action Buttons ────────────────────────────────────────
        with gr.Row():
            clear_btn = gr.Button(
                "⟳  CLEAR CHAT",
                scale=1,
                elem_classes=["action-btn"],
            )
            refresh_btn = gr.Button(
                "↺  REFRESH STATUS",
                scale=1,
                elem_classes=["action-btn"],
            )

        # ── Example Questions ─────────────────────────────────────
        gr.HTML('<div class="section-label">// quick queries</div>')
        with gr.Row():
            for i in range(0, 4):
                gr.Button(
                    EXAMPLE_QUESTIONS[i],
                    elem_classes=["example-btn"],
                ).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q,
                    outputs=msg_input,
                )
        with gr.Row():
            for i in range(4, 8):
                gr.Button(
                    EXAMPLE_QUESTIONS[i],
                    elem_classes=["example-btn"],
                ).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q,
                    outputs=msg_input,
                )

        # ── Footer ────────────────────────────────────────────────
        gr.HTML("""
            <div class="footer-bar">
                🔒 FULLY LOCAL — NO DATA SENT TO CLOUD &nbsp;|&nbsp;
                ANSWERS GROUNDED IN YOUR TIA PORTAL DOCUMENTATION
            </div>
        """)

        # ── Event Handlers ────────────────────────────────────────
        send_btn.click(
            fn=chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )
        msg_input.submit(
            fn=chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )
        clear_btn.click(
            fn=clear_chat,
            outputs=[msg_input, chatbot],
        )
        refresh_btn.click(
            fn=refresh_status,
            outputs=status,
        )

    return demo

# ── Build UI ──────────────────────────────────────────────────────
def build_ui():
    with gr.Blocks(
        css=CSS,
        title="TIA Portal AI Assistant",
        theme=gr.themes.Soft(
            primary_hue="blue",
            neutral_hue="slate",
        ),
    ) as demo:

        # ── Header ────────────────────────────────────────────────
        gr.HTML("""
            <div class="header-box">
                <h1 style="margin:0; font-size:24px; font-weight:700;">
                    🏭 TIA Portal AI Assistant
                </h1>
                <p style="margin:6px 0 0 0; opacity:0.85; font-size:14px;">
                    Powered by Qwen3 + LangChain + ChromaDB — runs fully locally
                </p>
            </div>
        """)

        # ── Status Bar ────────────────────────────────────────────
        status = gr.Markdown(
            value=get_status(),
            elem_classes=["status-bar"],
        )

        # ── Chat Window ───────────────────────────────────────────
        chatbot = gr.Chatbot(
            value=[],
            height=480,
            show_label=False,
            avatar_images=(
        None,
        "https://img.icons8.com/color/48/robot-2.png",
        ),
        )

        # ── Input Row ─────────────────────────────────────────────
        with gr.Row(elem_classes=["input-row"]):
            msg_input = gr.Textbox(
                placeholder="Ask anything about TIA Portal, SCL, PLCs, PROFINET...",
                show_label=False,
                scale=9,
                lines=1,
                max_lines=4,
                autofocus=True,
            )
            send_btn = gr.Button(
                "Send ➤",
                scale=1,
                variant="primary",
                elem_classes=["send-btn"],
            )

        # ── Action Buttons ────────────────────────────────────────
        with gr.Row():
            clear_btn = gr.Button(
                "🗑️ Clear Chat",
                scale=1,
                elem_classes=["clear-btn"],
            )
            refresh_btn = gr.Button(
                "🔄 Refresh Status",
                scale=1,
                elem_classes=["clear-btn"],
            )

        # ── Example Questions ─────────────────────────────────────
        gr.Markdown("### 💡 Example Questions")
        with gr.Row(elem_classes=["examples-row"]):
            for i in range(0, 4):
                gr.Button(EXAMPLE_QUESTIONS[i]).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q,
                    outputs=msg_input,
                )
        with gr.Row(elem_classes=["examples-row"]):
            for i in range(4, 8):
                gr.Button(EXAMPLE_QUESTIONS[i]).click(
                    fn=lambda q=EXAMPLE_QUESTIONS[i]: q,
                    outputs=msg_input,
                )

        # ── Footer ────────────────────────────────────────────────
        gr.HTML("""
            <div style="text-align:center; margin-top:16px;
                        font-size:12px; color:#888;">
                🔒 Fully local — no data sent to cloud &nbsp;|&nbsp;
                📚 Answers based on your TIA Portal documentation
            </div>
        """)

        # ── Event Handlers ────────────────────────────────────────
        # Send on button click
        send_btn.click(
            fn=chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )

        # Send on Enter key
        msg_input.submit(
            fn=chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )

        # Clear chat
        clear_btn.click(
        fn=clear_chat,
        outputs=[msg_input, chatbot],
        )

        # Refresh status
        refresh_btn.click(
            fn=get_status,
            outputs=status,
        )

    return demo


# ── Launch ────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo = build_ui()
    demo.launch(
        server_name="0.0.0.0",    # accessible on local network
        server_port=7860,
        share=False,               # set True to get a public gradio.live URL
        inbrowser=True,            # auto-opens browser tab
    )