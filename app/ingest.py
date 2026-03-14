from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

# تحميل ملفات PDF
docs_path = "docs"
documents = []

for file in os.listdir(docs_path):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(docs_path, file))
        documents.extend(loader.load())

print(f"Loaded {len(documents)} pages")

# تقسيم النص
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# إنشاء embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# إنشاء vector database
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vector_db"
)

print("Embeddings stored successfully")