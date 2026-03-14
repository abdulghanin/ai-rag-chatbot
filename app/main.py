from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .rag import ask_question

app = FastAPI()

# إضافة CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3002"],  # السماح بالمنافذ المختلفة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# نموذج الطلب
class ChatRequest(BaseModel):
    message: str


# endpoint
@app.post("/chat")

def chat(request: ChatRequest):

    answer = ask_question(request.message)

    return {
        "question": request.message,
        "answer": answer
    }