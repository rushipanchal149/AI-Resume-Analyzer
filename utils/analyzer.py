from utils.gemini import get_llm


def analyze_resume(resume_text, jd_text):

    llm = get_llm()

    prompt = f"""
You are an expert HR recruiter hiring a Data Science Intern.

Compare the following Resume with the Job Description.

=====================
RESUME
=====================

{resume_text}

=====================
JOB DESCRIPTION
=====================

{jd_text}

Give the output in the following format.

# Resume Match Score
(Give score out of 100)

# Resume Summary

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Resume Improvement Suggestions

# 5 Interview Questions

Use simple English.

Do not make up information that is not present in the resume.
"""

    response = llm.invoke(prompt)

    return response.content