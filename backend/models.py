from __future__ import annotations
from typing import List

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Date, Integer, String
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///hours_tracker.db", echo=True)

class Base(DeclarativeBase):
    pass

class Subject(Base):
    __tablename__ = "subjects"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    # class_subjects: Mapped[List["ClassSubject"]] = relationship("ClassSubject", back_populates="subjects")
    classes = relationship(
        "Class",
        secondary="class_subjects",
        back_populates="subjects"
    )

class SubjectCode(Base):
    __tablename__ = "subject_codes"

    id = mapped_column(Integer, primary_key=True)
    code = mapped_column(String, unique=True)
    subject_id = mapped_column(ForeignKey("subjects.id"))

class Class(Base):
    __tablename__ = "classes"

    id = mapped_column(Integer, primary_key=True)
    classname = mapped_column(String, unique=True)
    level = mapped_column(Integer)
    # class_subjects: Mapped[List["ClassSubject"]] = relationship("ClassSubject", back_populates="classes")
    subjects = relationship(
        "Subject",
        secondary="class_subjects",
        back_populates="classes"
    )

class Teacher(Base):
    __tablename__ = "teachers"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)

class ClassSubject(Base):
    __tablename__ = "class_subjects"

    id = mapped_column(Integer, primary_key=True)
    class_id = mapped_column(ForeignKey("classes.id"))
    subject_id = mapped_column(ForeignKey("subjects.id"))
    teacher_id = mapped_column(ForeignKey("teachers.id"))

class Record(Base):
    __tablename__ = "records"

    id = mapped_column(Integer, primary_key=True)
    date = mapped_column(Date)
    hours_taught = mapped_column(Integer)
    class_subject_id = mapped_column(ForeignKey("class_subjects.id"))

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        subjects = ["Advanced Python Programming", "Data Analysis", "Advanced Object-Oriented Programming", "Introduction to Artificial Intelligence"]
        classes = {
            1: ["SE3A","SE3B"] 
        }
        teachers = ["Nguh Prince"]

        for subject in subjects:
            new_subject = Subject(name=subject)
            session.add(new_subject)
            session.commit()

        for level, classnames in classes.items():
            for classname in classnames:
                session.add( Class(classname=classname.upper(), level=level) )
                session.commit()

        for teacher in teachers:
            session.add( Teacher(name=teacher) )
            session.commit()
    # Subject code, Subject, Class, Class Subject, Teacher, Teacher Class Subject, Teacher Class Subject Record
