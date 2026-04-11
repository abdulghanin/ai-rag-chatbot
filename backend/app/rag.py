from dotenv import load_dotenv
load_dotenv()

import os
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from pinecone import Pinecone

# ENV
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Init Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Embeddings 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
vectorstore = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM 
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

def ask_question(question: str):
    try:
        docs = retriever.invoke(question)
        

        # fallback لو مافي نتائج
        if not docs:
            return "I don't know. Please try asking in a different way."

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a professional real estate AI assistant for "Luxury Estates Dubai".

Your role:
- Help users find, buy, rent, and understand properties in Dubai.
- Act like an expert real estate agent.

Rules:
- Answer ONLY from the provided context.
- If the answer is not found, say: "I don't know".
- Do NOT make up information.
- Keep answers clear and structured.
- Use bullet points when helpful.

Behavior:
- If user asks about properties → suggest options with details (price, location, size).
- If user asks about process → explain step-by-step.
- If user shows interest → suggest next step (schedule visit, contact agent).

Context:
{context}

User Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
    try:
        docs = retriever.invoke(question)  # 

        if not docs:
            return "I don't know"

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are an AI assistant.

Answer ONLY from the context below.
If the answer is not in the context, say: "I don't know".

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"