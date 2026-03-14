# AI RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built with FastAPI, LangChain, Ollama, and React.

## Features

- Document ingestion and vector storage using ChromaDB
- RAG-based question answering with Llama 3
- Web-based chat interface with Tailwind CSS
- Embeddable widget for any website

## Setup

### Backend
1. Install dependencies: `pip install -r requirements.txt`
2. Run ingestion: `python app/ingest.py`
3. Start server: `python -m uvicorn app.main:app --reload`

### Frontend
1. Install dependencies: `cd chatbot-ui && npm install`
2. Start dev server: `npm start`
3. Build for production: `npm run build`

## Usage

- Access the chat interface at `http://localhost:3000`
- API endpoint: `POST /chat` with JSON `{"message": "your question"}`

## Deployment

- Host the backend on a server (e.g., Heroku)
- Host the frontend build on Netlify/Vercel
- Update widget script with live URLs