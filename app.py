import streamlit as st


from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_resume_text
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.analyzer import analyze_resume
from utils.ats import ats_checker
from utils.jd_loader import load_job_description
from utils.chatbot import ask_resume_question
from utils.pdf_report import generate_pdf
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your Resume using AI and Chat with your Resume.")

# -----------------------------
# File Upload
# -----------------------------
resume = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.file_uploader(
    "📋 Upload Job Description (PDF or TXT)",
    type=["pdf", "txt"]
)

# -----------------------------
# Analyze Resume
# -----------------------------
if st.button("🚀 Analyze Resume"):

    if resume is None:
        st.warning("Please upload your Resume.")
        st.stop()

    if job_description is None:
        st.warning("Please upload Job Description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        # Extract Resume Text
        resume_text = extract_text_from_pdf(resume)

        # Load Job Description
        jd_text = load_job_description(job_description)

        # Split Resume
        chunks = split_resume_text(resume_text)

        # Embedding Model
        embedding_model = get_embedding_model()

        # Create Vector Store
        vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        # Save Vector Store
        st.session_state["vector_store"] = vector_store

        # Save Resume Text
        st.session_state["resume_text"] = resume_text

        # Resume Analysis
        resume_result = analyze_resume(
            resume_text,
            jd_text
        )

        # ATS Analysis
        ats_result = ats_checker(
            resume_text
        )

        # Save Results
        st.session_state["resume_result"] = resume_result
        st.session_state["ats_result"] = ats_result

    st.success("✅ Resume Analysis Completed!")

# -----------------------------
# Show Resume Analysis
# -----------------------------
if "resume_result" in st.session_state:

    st.divider()

    st.header("🤖 Resume Analysis")

    st.markdown(st.session_state["resume_result"])
  
# -----------------------------
# Show ATS Analysis
# -----------------------------
# -----------------------------
# Show ATS Analysis
# -----------------------------
if "ats_result" in st.session_state:

    st.divider()

    st.header("📊 ATS Resume Analysis")

    st.markdown(st.session_state["ats_result"])

    # Generate PDF Report
    pdf_file = generate_pdf(
        st.session_state["resume_result"],
        st.session_state["ats_result"]
    )

    # Download Button
    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📥 Download AI Report",
            data=file,
            file_name="AI_Resume_Report.pdf",
            mime="application/pdf"
        )
# -----------------------------
# Resume Chatbot
# -----------------------------
if "vector_store" in st.session_state:

    st.divider()

    st.header("💬 Chat With Your Resume")

    question = st.text_input(
        "Ask anything about your resume"
    )

    if st.button("🤖 Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                answer = ask_resume_question(
                st.session_state["vector_store"],
                st.session_state["resume_text"],
                question
                )

            st.subheader("Answer")

            st.write(answer)