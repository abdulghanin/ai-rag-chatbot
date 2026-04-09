# 🤖 AI RAG Chatbot (Pinecone + Groq + FastAPI + React)

An advanced AI-powered Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, Pinecone, Groq (LLM), and React.

---

## 🚀 Features

- 🔍 RAG (Retrieval-Augmented Generation) architecture
- 📄 PDF document ingestion and semantic search
- ⚡ Fast vector search using Pinecone
- 🧠 LLM powered by Groq (Llama 3.3 70B)
- 💬 Modern chat UI (React + Tailwind CSS)
- 🧩 Embeddable chatbot widget
- 🌍 Real-world use case: Real Estate AI Assistant

---

## 🧠 Tech Stack

### Backend
- FastAPI
- LangChain
- Pinecone (Vector Database)
- HuggingFace Embeddings
- Groq API (LLM)

### Frontend
- React
- Axios
- Tailwind CSS

---

Setup
Backend
Install dependencies: pip install -r requirements.txt
Run ingestion: python app/ingest.py
Start server: python -m uvicorn app.main:app --reload
Frontend
Install dependencies: cd chatbot-ui && npm install
Start dev server: npm start
Build for production: npm run build
Usage
Access the chat interface at http://localhost:3000
API endpoint: POST /chat with JSON {"message": "your question"}
