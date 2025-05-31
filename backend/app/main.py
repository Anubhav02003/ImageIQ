from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from .model import VQAModel

app = FastAPI()

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, use ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vqa_model = VQAModel()

@app.post("/vqa/")
async def vqa_endpoint(image: UploadFile = File(...), question: str = Form(...)):
    temp_image_path = f"temp_{image.filename}"
    with open(temp_image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    try:
        answer = vqa_model.answer_question(temp_image_path, question)
    except Exception as e:
        os.remove(temp_image_path)
        return JSONResponse(status_code=500, content={"error": str(e)})
    os.remove(temp_image_path)
    return {"answer": answer}

# Optional: Simple root endpoint for testing
@app.get("/")
async def root():
    return {"message": "API is running"}
