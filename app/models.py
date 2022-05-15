from app import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    transcript = db.relationship(
        "Transcripts", backref="subjects", cascade="all, delete", passive_deletes=True
    )


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    child = db.relationship("Subject", backref="teachers", uselist=False)


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    credit_number = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=False)
    parent = db.relationship("Teacher", backref="subjects")
    # transcript = db.relationship(
    #     "Transcripts", backref="subjects", cascade="all, delete", passive_deletes=True
    # )


class Transcripts(db.Model):
    __tablename__ = "transcripts"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    score_C = db.Column(db.Float)
    score_B = db.Column(db.Float)
    score_A = db.Column(db.Float)
    summation_points = db.Column(db.Float)
