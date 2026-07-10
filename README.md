# 🤖 AI Resume Analyzer


🚀 **Live Demo:**  
https://ai-resume-analyzer-9mbhafwnnwknf865bhjrqs.streamlit.app/

An AI-powered Resume Analyzer built using **Streamlit, LangChain, Google Gemini, FAISS, and HuggingFace Embeddings**.

The application analyzes resumes against job descriptions, provides ATS feedback, allows users to chat with their resume using Retrieval-Augmented Generation (RAG), and generates a downloadable PDF report.

---

## 🚀 Features

* 📄 Upload Resume (PDF)
* 📋 Upload Job Description (PDF/TXT)
* 🤖 AI Resume Analysis
* 📊 ATS Resume Analysis
* 💬 Chat with Your Resume (RAG)
* 🧠 Semantic Search using FAISS
* 📥 Download AI Analysis Report (PDF)

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini
* HuggingFace Embeddings
* FAISS
* ReportLab
* PyPDF
* Sentence Transformers

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── utils/
│   ├── analyzer.py
│   ├── ats.py
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── gemini.py
│   ├── jd_loader.py
│   ├── pdf_loader.py
│   ├── pdf_report.py
│   ├── text_splitter.py
│   └── vector_store.py
```

---

## 🧠 How It Works

1. Upload Resume and Job Description.
2. Extract text from the uploaded files.
3. Split the resume into chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in a FAISS vector database.
6. Use Google Gemini for:

   * Resume Analysis
   * ATS Analysis
   * Resume Question Answering
7. Generate and download a PDF report.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

Move into the project folder:

```bash
cd AI-Resume-Analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots of:

* Home Page
* Resume Analysis
* ATS Analysis
* Resume Chatbot
* PDF Report

---

## 🔮 Future Improvements

* Resume Match Score
* Skill Gap Visualization
* Multiple Resume Comparison
* Interview Question Generator
* Resume Recommendation System

---

## 👨‍💻 Developer

**Rushikesh Panchal**

B.Tech Computer Science & Engineering

AI & Data Science Enthusiast

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
