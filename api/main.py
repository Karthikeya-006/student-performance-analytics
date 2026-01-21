from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import StudentMarks
from service import calculate_internal

app = FastAPI(title="Student Performance API")

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/calculate-internal")
def calculate_internal_marks(student: StudentMarks):
    internal_marks = calculate_internal(student)
    return {
        "internal_marks_out_of_30": internal_marks
    }
import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
