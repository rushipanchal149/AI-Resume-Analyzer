from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_resume_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.create_documents([text])