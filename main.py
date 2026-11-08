from fastapi import FastAPI, UploadFile ,File

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Resume-JD Analyzer is running"}

@app.post("/analyze")
async def analyze(resume: UploadFile = File(...)):
    return {"filename": resume.filename}


