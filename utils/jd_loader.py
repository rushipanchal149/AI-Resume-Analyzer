from utils.pdf_loader import extract_text_from_pdf


def load_job_description(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    return uploaded_file.read().decode("utf-8")