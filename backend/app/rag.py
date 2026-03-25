import os
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

BASE_DIR = os.path.dirname(__file__)

# LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
vector_db = Chroma(
    persist_directory=os.path.join(BASE_DIR, "../vector_db"),
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

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