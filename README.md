# AI RAG Chatbot (Pinecone + Groq + FastAPI + React)

A full-stack Retrieval-Augmented Generation (RAG) chatbot with PDF ingestion, semantic search, and a React chat widget.

## 🚀 Features
- Retrieval-Augmented Generation (RAG)
- PDF ingestion and text chunking
- Fast vector search with Pinecone
- Groq Llama 3.3 70B inference via Groq API
- React chat widget UI
- Deploy backend to Render and frontend to Vercel

## 🧠 Tech Stack
- Backend: FastAPI, LangChain, Pinecone, Groq, HuggingFace embeddings
- Frontend: React, Axios, Tailwind CSS

## 📁 Project Structure
```
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
│   └── Dockerfile
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── ChatWidget.js
│   │   └── index.js
│   ├── package.json
│   └── vercel.json
│
└── render.yaml
```

## ⚙️ Backend Setup
1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```
2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```
3. Add environment variables in `backend/.env`:
```env
GROQ_API_KEY=your_key
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME=rag-chatbot
```
4. Add PDFs to `backend/docs/`.
5. Run ingestion:
```bash
python ingest/ingest.py
```
6. Start the API:
```bash
uvicorn app.main:app --reload
```

Local backend URL:
```text
http://localhost:8000
```

## 💬 Frontend Setup
1. Install dependencies:
```bash
cd frontend
npm install
```
2. Start the React app:
```bash
npm start
```

Local frontend URL:
```text
http://localhost:3000
```

## 🔌 API Usage
**POST** `/chat`

Request body:
```json
{
  "message": "your question"
}
```

Response body:
```json
{
  "question": "...",
  "answer": "..."
}
```

## 🚀 Deployment Guide
### Backend Deployment (Render)
1. Push the repo to GitHub.
2. Ensure `render.yaml` is at the repository root.
3. Configure Render to use Docker and `backend/Dockerfile`.
4. Set these environment variables in Render:
   - `GROQ_API_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_INDEX_NAME=rag-chatbot`
5. Deploy and note your backend URL.

### Frontend Deployment (Vercel)
1. Deploy the `frontend/` folder as the project root.
2. Set `Build Command` to:
```text
npm run build
```
3. Set `Output Directory` to:
```text
build
```
4. Add this environment variable in Vercel:
   - `REACT_APP_BACKEND_URL=https://your-backend.onrender.com`
5. Deploy.

## 🔧 Important Notes
- The frontend reads the backend endpoint from `REACT_APP_BACKEND_URL`.
- `frontend/vercel.json` is configured to serve static assets and SPA routes correctly.
- If you see a white page in production, check the browser console and confirm the Vercel env var.

## 🧩 Embedding the Chat Widget
In `frontend/src/App.js`:
```jsx
import ChatWidget from "./ChatWidget";

function App() {
  return (
    <div>
      <ChatWidget />
    </div>
  );
}

export default App;
```