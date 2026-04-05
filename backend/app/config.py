import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("Warning: Missing GROQ_API_KEY - RAG functionality will be limited")
    GROQ_API_KEY = None