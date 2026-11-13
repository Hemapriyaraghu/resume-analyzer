import io
from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume-JD Analyzer is running"}

@app.post("/analyze")
async def analyze(resume: UploadFile = File(...)):
    pdf_bytes = await resume.read()
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = " ".join((page.extract_text() or "") for page in reader.pages)
    return {"filename": resume.filename, "characters": len(text), "preview": text[:300]}