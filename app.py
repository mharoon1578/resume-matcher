import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from prompts import resume_screening_template

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.title("Resume Screener & Job Matcher")
st.markdown('''    Upload your **resume (PDF format)** and paste the **full job description** below.
    The app will analyze and generate a detailed compatibility report, including skill matches, gaps, and recommendations.''')
GROQ_API_KEY = st.text_input(
    "Enter your Groq API Key",
    type="password",
    placeholder="Paste your Groq API key here",
    help="Get your API key from https://developer.groq.com",
)
uploaded_file = st.file_uploader("Upload your Resume (PDF only)",
    type=["pdf"],
    help="Please upload a text-based PDF resume (not scanned images) for accurate analysis.")
job_description = st.text_area("Paste the Job Description", height=250, placeholder="Copy and paste the complete job description here, including responsibilities and requirements.",
    help="The more detailed the job description, the more accurate the screening.")

def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text.strip
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

if st.button("Check Compatibility"):
    if not uploaded_file:
        st.warning("⚠️ Please upload a resume PDF file to proceed.")
    elif not job_description.strip():
        st.warning("⚠️ Please paste a job description to proceed.")
        
    if uploaded_file and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)

        if not resume_text:
            st.warning("Could not extract any text from the PDF. Try using a text-based resume.")
        else:
            llm = ChatGroq(
                temperature=0,
                groq_api_key=GROQ_API_KEY,
                model_name="gemma2-9b-it"
            )
            chain = LLMChain(llm=llm, prompt=resume_screening_template)

            with st.spinner("Analyzing resume..."):
                try:
                    result = chain.run(resume_text=resume_text, job_description=job_description)
                    st.subheader("Screening Report")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error running the LLM: {e}")