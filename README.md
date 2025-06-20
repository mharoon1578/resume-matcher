
# Resume Screener & Job Matcher

A Streamlit app that analyzes the compatibility of a resume against a job description using the Groq API powered by the mistral-saba-24b language model.

---

## Features

- Upload a PDF resume (text-based).
- Paste a full job description.
- Enter your Groq API key directly in the app UI every time.
- Analyze and generate a detailed screening report including:
  - Match Score
  - Matching Skills & Experience
  - Missing Critical Skills or Experience
  - Risk Assessment
  - Resume Improvement Suggestions
  - Final Verdict

---

## Getting Started

### Prerequisites

- Python 3.8+
- Groq API key (get one at [https://developer.groq.com](https://developer.groq.com))
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-screener.git
   cd resume-screener
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Run the App

```bash
streamlit run app.py
```

---

## How to Use

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Upload your **resume in PDF format** (ensure it is text-based, not scanned images).
3. Paste the **job description** text in the provided text area.
4. Enter your **Groq API key** in the input box.
5. Click the **Check Compatibility** button.
6. View the detailed screening report generated by the AI.

---

## Important Notes

- The app requires a valid Groq API key to run.
- Your resume and job description data are sent securely to Groq’s API for processing.
- The app does **not** store your API key or input data.
- Make sure your resume PDF is text-based for successful text extraction.

---

## File Structure

```
├── app.py                  # Main Streamlit application
├── prompts.py              # Contains the resume screening prompt template
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .env.example            # Example env file (optional)
```

---

## Dependencies

- streamlit
- PyPDF2
- langchain
- langchain_groq
- python-dotenv

---

## License

MIT License

---

## Contact

For any questions or issues, please open an issue or contact me at mharoon1578@gmail.com.

---
