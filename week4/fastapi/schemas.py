from pydantic import BaseModel

class Student(BaseModel):
    name: str
    department: str
    marks: int

class StudentResponse(Student):
    id: int

    class Config:
        from_attributes = True