import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Warning: Missing GOOGLE_API_KEY - RAG functionality will be limited")
    GOOGLE_API_KEY = None