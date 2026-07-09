from utils.gemini import get_llm


def ask_resume_question(vector_store, resume_text, question):

    # Retrieve more relevant chunks
    docs = vector_store.similarity_search(
        question,
        k=8
    )

    context = ""

    for i, doc in enumerate(docs):
        context += f"\n--- Resume Chunk {i+1} ---\n"
        context += doc.page_content + "\n"

    llm = get_llm()

    prompt = f"""
You are an AI Resume Assistant.

Below is the candidate's FULL resume and the most relevant retrieved sections.

==========================
FULL RESUME
==========================

{resume_text}

==========================
RETRIEVED RESUME SECTIONS
==========================

{context}

Answer the user's question ONLY using the resume information.

Rules:
1. Search the complete resume before saying information is unavailable.
2. Use the retrieved sections as the primary source.
3. Do NOT make up information.
4. If the information is truly not present, reply:
   "The information is not available in the resume."

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content