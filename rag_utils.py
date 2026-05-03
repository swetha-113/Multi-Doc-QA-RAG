import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def process_pdfs(uploaded_files):
    os.makedirs("docs", exist_ok=True)

    all_docs = []

    for file in uploaded_files:
        file_path = os.path.join("docs", file.name)

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        loader = PyPDFLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(all_docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)

    return vector_db


def retrieve_context(vector_db, question):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(question)

    context = ""

    for i, doc in enumerate(relevant_docs):
        context += f"\n--- Relevant Part {i + 1} ---\n"
        context += doc.page_content + "\n"

    return context