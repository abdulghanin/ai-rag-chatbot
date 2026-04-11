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
index = pc.Index(INDEX_NAME)

# Embeddings 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB 
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM 
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0  
)

def ask_question(question: str):
    try:
        docs = retriever.invoke(question)

        if not docs:
            return "I don't know"

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a professional real estate AI assistant for "Luxury Estates Dubai".

STRICT RULES:
- Answer ONLY using the context below
- If answer not found → say: I don't know
- Do NOT guess or add information

STYLE:
- Clear and professional
- Use bullet points if needed

CONTEXT:
{context}

QUESTION:
{question}

FINAL ANSWER:
"""

        response = llm.invoke(prompt)
        return response.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"