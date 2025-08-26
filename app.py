import streamlit as st
import re
import docx2txt
import fitz
from io import BytesIO
import numpy as np
from sentence_transformers import SentenceTransformer,util
from benchmark_skills import extract_skill,find_gaps

#Streamlit UI
st.set_page_config(page_title="AI Powered Resume Screener",layout="centered")
st.title("AI Powered Resume Screener")


#helper functions
def extract_text(uploaded_file):
    if uploaded_file is None:
        return ""
    data=uploaded_file.getvalue()

    name=uploaded_file.name.lower()
    if name.endswith(".pdf"):
        doc=fitz.open(stream=data,filetype="pdf")
        text=""
        for page in doc:
            text+=page.get_text()
        return text
    elif name.endswith(".docx"):
        try:
            buf=BytesIO(data)
            return docx2txt.process(buf)
        except Exception:
            return ""
        
    elif name.endswith(".txt"):
        return data.encode("utf-8",errors="ignore")
    else:
        return ""
       
def clean_text(text):
    #Basic text cleaning
    if not isinstance(text,str):
        return ""
    text=text.lower()
    text=re.sub(r"[^a-z0-9\s]"," ",text)
    text=re.sub(r"\s+"," ", text).strip()
    return text

@st.cache_resource
def load_bert():
        return SentenceTransformer('all-MiniLM-L6-v2')
bert_model= load_bert()
   
def compute_similarity(resume_txt,jd_text):
    resume_emb=bert_model.encode([resume_txt],convert_to_tensor=True,normalize_embeddings=True)
    jd_emb=bert_model.encode([jd_text], convert_to_tensor=True,normalize_embeddings=True)
    score=util.cos_sim(resume_emb,jd_emb).cpu().item()
    return round(score,4)


#Upload Resume
upload_resume=st.file_uploader("Upload Your Resume (PDF/DOCX/TXT)",type=["pdf","docx","txt"])

#Enter the job description
job_description=st.text_area("Paste the Job Description here")

#Action buttons

analyze_btn=st.button("Analyze")
gap_btn=st.button("Identify Gaps")

#Analyze flow
if analyze_btn and upload_resume and job_description:
    resume_txt=extract_text(upload_resume)

    if resume_txt.strip() and job_description.strip():
        score=compute_similarity(resume_txt,job_description)
        st.metric("Cosine Similarity Score (0-1):",f"{score}")
        st.info("Higher similarity means Resume and JD are semantically more similar")
    else:
        st.info("Please provide both Resume and job description text")
        
   
#Identify gaps flow
if gap_btn and upload_resume and job_description:
    resume_txt=extract_text(upload_resume)
    
    #find matching, missing and extra skills
    matched, missing, extra=find_gaps(resume_txt,job_description)

    col1,col2,col3 =st.columns(3)

    with col1:
        #Display matched skills
        st.markdown("<h4 style='color:green;'>✅ Matched Skills</h4>", unsafe_allow_html=True)
        with st.expander("View Matched Skills", expanded=True):
            for skill in matched:
                st.markdown(f"- {skill}")
    with col2:
        st.markdown("<h4 style='color:red;'>❌ Missing Skills</h4>", unsafe_allow_html=True)
        with st.expander("View Missing Skills", expanded=True):
            for skill in missing:
                st.markdown(f"- {skill}")
    with col3:
        #Display extra skills
        st.markdown("<h4 style='color:orange;'>📌 Extra Skills</h4>", unsafe_allow_html=True)
        with st.expander("View Extra Skills", expanded=True):
            for skill in extra:
                st.markdown(f"- {skill}")