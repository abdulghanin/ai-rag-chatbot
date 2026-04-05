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
try:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    print("Embeddings loaded successfully")
except Exception as e:
    print(f"Warning: Failed to load embeddings: {e}")
    embeddings = None

# Vector DB
if embeddings:
    try:
        vector_db = Chroma(
            persist_directory=os.path.join(BASE_DIR, "../vector_db"),
            embedding_function=embeddings
        )
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        print("Vector DB loaded successfully")
    except Exception as e:
        print(f"Warning: Failed to load vector DB: {e}")
        vector_db = None
        retriever = None
else:
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

    if not retriever:
        return "⚠️ Document search is not available. Vector database failed to load."

    docs = retriever.invoke(question)

    if not docs:
        return "I couldn't find relevant information."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = prompt_template.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content