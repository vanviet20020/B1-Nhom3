from app import db
from app import login
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    transcripts = db.relationship(
        "Transcript",
        backref="student",
        lazy="dynamic",
        cascade="all, delete",
        passive_deletes=True,
    )


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    child = db.relationship("Subject", backref="teachers", uselist=False)
    subjects = db.relationship(
        "Subject",
        backref="teacher",
        lazy="dynamic",
        # cascade="all, delete",
        # passive_deletes=True,
    )


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    credit_number = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=False)
    transcripts = db.relationship(
        "Transcript",
        backref="subject",
        lazy="dynamic",
        # cascade="all, delete",
        # passive_deletes=True,
    )


class Transcript(db.Model):
    __tablename__ = "transcripts"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    score_C = db.Column(db.Float)
    score_B = db.Column(db.Float)
    score_A = db.Column(db.Float)
    summation_points = db.Column(db.Float)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Integer, default=0)

    def set_password(self, password_input):
        self.password = generate_password_hash(password_input)

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
