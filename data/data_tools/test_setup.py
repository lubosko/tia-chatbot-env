# test_setup.py
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:8b")  # ← use exact name from ollama list
response = llm.invoke("What is Siemens TIA Portal?")
print(response.content)
