# AI Resume Screener

An AI-powered resume screening tool that extracts skills from resumes and compares them with job description (JD). The app highlights missing skills and provides a simple gap analysis to help candidates quickly evaluate alignment.

---

## 📌 Features
- **Skill Extraction**: Parses resumes and extracts key technical and soft skills.
- **Benchmark Comparison**: Matches extracted skills against a predefined benchmark skills list.
- **Gap Analysis**: Identifies missing or underrepresented skills in the resume.
- **Interactive App**: Built with **Streamlit** for a user-friendly interface.
- **Note**: The benchmark skills list does not include all possible skills and will be **updated over time** to cover more skills.

---

## 📂 Project Structure
```
AI-Resume-Screener/
├── app.py                # Main Streamlit app
├── benchmark_skills.pkl  # Pre-saved benchmark skills list (to be updated over time)
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Resume-Screener.git
   cd AI-Resume-Screener
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Upload a resume (PDF or text) and compare against the benchmark skills.

---

## 🛠 Tech Stack
- **Python**
- **Streamlit**
- **scikit-learn**
- **NLTK / Regex** for text parsing
- **Pickle** for storing benchmark skills

---

## 🚀 Future Improvements
- Add **SHAP/Explainability** for model transparency.
- Expand support for **multiple resumes** at once.
- Improve **UI/UX** with better design and filtering options.
- Integration with **ATS (Applicant Tracking Systems)**.
- Continuously **update benchmark_skills.pkl** to include more skills.

---

