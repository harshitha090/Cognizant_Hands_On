from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student API",
    description="FastAPI CRUD using Pydantic Models",
    version="1.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    new_student = models.Student(
        name=student.name,
        department=student.department,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()