from langchain_community.vectorstores import FAISS

def create_vector_store(documents, embedding_model):

    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    return vector_store