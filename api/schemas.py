from pydantic import BaseModel, Field

class StudentMarks(BaseModel):
    mid1: float = Field(..., ge=0, le=18)
    mid2: float = Field(..., ge=0, le=18)
    assign1: float = Field(..., ge=0, le=12)
    assign2: float = Field(..., ge=0, le=12)
    quiz1: float = Field(..., ge=0, le=12)
    quiz2: float = Field(..., ge=0, le=12)
    attendance: float = Field(..., ge=0, le=100)