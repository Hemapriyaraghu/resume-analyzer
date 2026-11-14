import io
from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader
from analyzer import analyze_resume

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Resume-JD Analyzer is running"}


@app.post("/analyze")
async def analyze(resume: UploadFile = File(...), jd_text: str = Form(...)):
    pdf_bytes = await resume.read()
    reader = PdfReader(io.BytesIO(pdf_bytes))
    resume_text = " ".join((page.extract_text() or "") for page in reader.pages)
    result = analyze_resume(resume_text, jd_text)
    return {"filename": resume.filename, **result}