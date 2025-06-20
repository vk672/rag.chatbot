from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from chatbot.process_data import prepare_documents

def build_vector_store():
    docs = prepare_documents()
    lang_docs = [Document(page_content=d["content"], metadata=d["metadata"]) for d in docs]
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(lang_docs, embeddings)
    return vector_store

def build_rag_chain():
    vector_store = build_vector_store()
    retriever = vector_store.as_retriever()
    llm = OpenAI(temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
