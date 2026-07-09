from utils.gemini import get_llm


def ats_checker(resume_text):

    llm = get_llm()

    prompt = f"""
You are an ATS (Applicant Tracking System).

Analyze the following resume.

Resume:

{resume_text}

Give:

# ATS Score (0-100)

# ATS Friendly (Yes/No)

# Good Points

# Missing Sections

# Resume Improvement Tips

Use simple English.
"""

    response = llm.invoke(prompt)

    return response.content