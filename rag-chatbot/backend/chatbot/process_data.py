import json
from langchain.text_splitter import CharacterTextSplitter

def load_cached_data():
    with open("data/cache.json") as f:
        return json.load(f)

def prepare_documents():
    data = load_cached_data()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = []
    for item in data:
        if item["content"]:
            chunks = splitter.split_text(item["content"])
            for chunk in chunks:
                docs.append({"content": chunk, "metadata": item})
    return docs
