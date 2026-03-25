import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

BASE_DIR = os.path.dirname(__file__)
DOCS_PATH = os.path.join(BASE_DIR, "docs")

if not os.path.exists(DOCS_PATH):
    raise Exception("docs folder not found")

documents = []

for file in os.listdir(DOCS_PATH):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DOCS_PATH, file))
        documents.extend(loader.load())

print(f"Loaded {len(documents)} pages")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# embeddings 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=os.path.join(BASE_DIR, "../vector_db")
)

print("Embeddings stored successfully")