# Resume-JD Analyzer API

A FastAPI project that compares a resume (PDF) with a job description and returns a
match score, the skills that match, and the skills that are missing.

## Features
- Upload a resume as a PDF and paste a job description
- Text extraction from the PDF using pypdf
- Skill extraction from both texts using a keyword list
- Match score = 60% skill coverage + 40% TF-IDF text similarity (scikit-learn)
- Interactive API docs at `/docs` (Swagger UI)

## Tech stack
Python, FastAPI, scikit-learn, pypdf, Uvicorn, Git

## How to run
```bash
git clone https://github.com/Hemapriyaraghu/resume-analyzer.git
cd resume-analyzer
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs, try `POST /analyze`, upload a PDF resume and paste a job description.

## Example response
```json
{
  "filename": "resume.pdf",
  "match_score": 32.2,
  "matched_skills": ["python"],
  "missing_skills": ["java"]
}
```

## Limitations
- Only finds skills listed in `skills.py` (keyword matching, no understanding of meaning)
- Scanned (image-only) PDFs are not supported

## Planned
- [ ] Save analysis history in SQLite
- [ ] Tests with pytest
- [ ] Deployment
- [ ] Simple frontend

## Author
Hemapriya R, B.Sc. Information Technology graduate
