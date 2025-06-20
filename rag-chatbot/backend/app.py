from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot.fetch_data import fetch_and_cache_articles
from chatbot.rag_engine import build_rag_chain

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

# Root route to prevent 404 at "/"
@app.get("/")
def read_root():
    return {"message": "RAG Chatbot Backend is running!"}

@app.get("/api/refresh")
def refresh_articles():
    try:
        fetch_and_cache_articles()
        return {"status": "refreshed"}
    except Exception as e:
        print("🔥 Error in /api/refresh:", str(e))
        return {"error": "Failed to refresh articles", "details": str(e)}

@app.post("/api/ask")
def ask_question(query: Query):
    try:
        print("📥 Question received:", query.question)
        rag_chain = build_rag_chain()
        print("✅ RAG chain built successfully.")
        answer = rag_chain.run(query.question)
        print("✅ Answer generated:", answer)
        return {"answer": answer}
    except Exception as e:
        print("🔥 Error in /api/ask:", str(e))
        return {"error": "Internal server error", "details": str(e)}
