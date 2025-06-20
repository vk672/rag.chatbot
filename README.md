# rag.chatbot
A full-stack, production-ready Retrieval-Augmented Generation (RAG) Chatbot that answers user queries by combining OpenAI GPT with custom scraped data. It features real-time document retrieval, natural language understanding, and a seamless user interface.

<br/>
🚀 Features
🔍 RAG Pipeline: Combines semantic search and GPT-based generation

📄 Data Ingestion: Crawls tech websites and indexes content with FAISS

🧠 LLM Integration: Supports OpenAI and local LLMs via LangChain

⚡ FastAPI Backend: Modular, scalable backend API

💬 Frontend UI: Clean, responsive chat interface (HTML/CSS/JS)

🛡️ .env-based Secrets: All credentials are safely stored using environment variables

📁 Docker-ready: Optional Docker setup for deployment

# Project Structure
rag-chatbot/
├── backend/
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── fetch_data.py        # Scrapes or fetches external content
│   │   ├── process_data.py      # Embeds & stores in FAISS
│   │   ├── rag_engine.py        # RAG logic (retrieve + generate)
│   │   └── utils.py             # Helper functions
│   ├── data/                    # Raw or processed data
│   ├── app.py                   # FastAPI entry point
│   └── .env                     # API Keys (not tracked)
├── frontend/
│   ├── index.html               # UI Layout
│   ├── style.css                # Styling
│   └── app.js                   # JS for chat interaction
├── .gitignore
├── requirements.txt
└── uvicorn                      # Server runner (optional)


🛠️ Setup Instructions
1. Clone the repository
   git clone https://github.com/vk672/rag-chatbot.git
cd rag-chatbot

2. Create virtual environment
   python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4.start backend
cd backend
uvicorn main:app --reload


