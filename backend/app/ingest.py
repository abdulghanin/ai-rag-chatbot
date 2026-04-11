from dotenv import load_dotenv
load_dotenv()

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

# ENV
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Init Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)


index = pc.Index(INDEX_NAME)

# 📁 FIX PATH 
BASE_DIR = os.path.dirname(__file__)
DOCS_PATH = os.path.join(BASE_DIR, "../docs")

if not os.path.exists(DOCS_PATH):
    raise Exception(f"❌ docs folder not found at: {DOCS_PATH}")

documents = []

for file in os.listdir(DOCS_PATH):
    if file.endswith(".pdf"):
        file_path = os.path.join(DOCS_PATH, file)
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())

print(f"📄 Loaded {len(documents)} pages")

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"✂️ Created {len(chunks)} chunks")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

vectorstore.add_documents(chunks)

print("✅ Uploaded to Pinecone")