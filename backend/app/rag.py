import os
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

BASE_DIR = os.path.dirname(__file__)

# LLM
if GROQ_API_KEY:
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile"
    )
else:
    llm = None

# Embeddings - temporarily disabled for testing
embeddings = None
vector_db = None
retriever = None
print("RAG components disabled for testing")

# Prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant.

Answer ONLY from the context below.
If the answer is not in the context, say: "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
)

def ask_question(question: str):

    if not llm:
        return "⚠️ AI service is not configured. Please set GROQ_API_KEY in your environment."

    # Temporary response for testing
    return f"Test response: You asked '{question}'. RAG functionality is temporarily disabled for testing."