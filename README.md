🤖 AI RAG Chatbot (Pinecone + Groq + FastAPI + React)
A full‑stack Retrieval‑Augmented Generation (RAG) chatbot using FastAPI, LangChain, Pinecone, Groq Llama 3.3 70B, and a modern React chat widget.
Supports PDF ingestion, semantic search, and real‑time conversational AI.

🚀 Features
🔍 Retrieval‑Augmented Generation (RAG)

📄 PDF ingestion + text chunking

⚡ Fast vector search using Pinecone

🧠 Groq Llama 3.3 70B for ultra‑fast inference

💬 React chat widget (embeddable anywhere)

🎨 Tailwind CSS UI

🌍 Real‑world example: Real Estate AI Assistant

🧠 Tech Stack
Backend
FastAPI

LangChain

Pinecone

HuggingFace Embeddings

Groq API

Frontend
React

Axios

Tailwind CSS

📁 Project Structure
Code
ai-rag-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag.py
│   │   ├── config.py
│   ├── ingest/
│   │   └── ingest.py
│   ├── docs/          # PDF files go here
│   ├── requirements.txt
│   ├── start.sh
│   └── render.yaml
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js
⚙️ Backend Setup (FastAPI)
1. Create virtual environment
bash
python -m venv venv
venv\Scripts\activate
2. Install dependencies
bash
pip install -r requirements.txt
3. Add environment variables
Create .env inside backend/:

Code
GROQ_API_KEY=your_key
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME=rag-chatbot
4. Add PDFs
Place your documents inside:

Code
backend/docs/
5. Run ingestion
bash
python ingest/ingest.py
6. Start the API
bash
uvicorn app.main:app --reload
API runs at:

Code
http://localhost:8000
💬 Frontend Setup (React)
1. Install dependencies
bash
cd frontend
npm install
2. Set API URL
Inside your widget:

js
const API_URL = "http://localhost:8000";
3. Start development server
bash
npm start
Frontend runs at:

Code
http://localhost:3000
🔌 API Usage
POST /chat
Request:

json
{
  "message": "your question"
}
Response:

json
{
  "question": "...",
  "answer": "..."
}
🚀 Deployment Guide
Backend Deployment (Render)
Push backend to GitHub

Add start.sh:

bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
Add environment variables in Render dashboard

Deploy as a Web Service

Render will give you a URL like:

Code
https://your-backend.onrender.com
Frontend Deployment (Vercel)
Push frontend to GitHub

Update API URL:

js
const API_URL = "https://your-backend.onrender.com";
Deploy on Vercel

Your chatbot widget becomes publicly accessible.

🧩 Embedding the Chat Widget
jsx
import ChatWidget from "./ChatWidget";

function App() {
  return <ChatWidget />;
}