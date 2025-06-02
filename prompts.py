from langchain.prompts import PromptTemplate

resume_screening_template = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
You are an expert HR evaluator.

Your task is to **exhaustively and accurately match the resume to the job description**. If the resume contains a required skill, qualification, or experience — even in the education or achievements section — it must be marked as matched.

Your evaluation must be complete. **Parse the entire resume**, including PROFILE, EMPLOYMENT HISTORY, EDUCATION, CERTIFICATIONS, SKILLS, and ACHIEVEMENTS.

Do not ignore bullet points or formatted sections. Be strict, but do not miss any clearly stated qualification.

Respond in the following format:

---
### Match Score (0–100)
<Numeric score — 95 or higher only if most items are directly present>

### Matching Skills & Experience
- <Every requirement explicitly stated or strongly present in the resume if not say not present>

### Missing Critical Skills or Experience
- <Only list what is completely missing or ambiguous — not phrased differently>

### Risk Assessment
- <If any, explain the risk of hiring this candidate based on missing items>

### Resume Improvement Suggestions
- <Only suggest improvements based on actual gaps>

### Final Verdict
<Yes or No>: <Justify your answer briefly>
---

Resume:
{resume_text}

Job Description:
{job_description}
"""
)
