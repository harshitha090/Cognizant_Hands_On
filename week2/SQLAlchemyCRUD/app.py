from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///students.db")

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    marks = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# CREATE
student1 = Student(name="Harshitha", department="CSE", marks=90)
student2 = Student(name="Rahul", department="ECE", marks=82)

session.add(student1)
session.add(student2)
session.commit()

print("Students inserted successfully!")

# READ
print("\nStudent Records:")
students = session.query(Student).all()

for s in students:
    print(s.id, s.name, s.department, s.marks)

# UPDATE
student = session.query(Student).filter_by(name="Rahul").first()

if student:
    student.marks = 95
    session.commit()
    print("\nRahul's marks updated!")

# READ AFTER UPDATE
print("\nStudent Records After Update:")
students = session.query(Student).all()

for s in students:
    print(s.id, s.name, s.department, s.marks)

# DELETE
student = session.query(Student).filter_by(name="Harshitha").first()

if student:
    session.delete(student)
    session.commit()
    print("\nHarshitha deleted!")

# READ AFTER DELETE
print("\nFinal Student Records:")
students = session.query(Student).all()

for s in students:
    print(s.id, s.name, s.department, s.marks)

session.close()