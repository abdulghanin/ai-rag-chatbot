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

# Embeddings
try:
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    print("Embeddings loaded successfully")
except Exception as e:
    print(f"Error loading embeddings: {e}")
    embeddings = None

# Vector DB
try:
    if embeddings:
        vector_db = Chroma(persist_directory='./vector_db', embedding_function=embeddings)
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        print("Vector database loaded successfully")
    else:
        vector_db = None
        retriever = None
        print("Vector database not loaded - embeddings failed")
except Exception as e:
    print(f"Error loading vector database: {e}")
    vector_db = None
    retriever = None

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

    try:
        # Direct LLM query for testing Google Gemini
        prompt = f"Please answer this question: {question}"
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"⚠️ Error processing your question: {str(e)}"