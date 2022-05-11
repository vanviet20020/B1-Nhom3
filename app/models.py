from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(db.Model):
    __tablename__ = "users"
    code = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    def set_password(self, password_input):
        self.password = generate_password_hash(password_input)

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    user_code = db.Column(db.String, db.ForeignKey("users.code"), nullable=False)


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    user_code = db.Column(db.String, db.ForeignKey("users.code"), nullable=False)


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    credit_number = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=False)
    transcipts = db.relationship("Transcipts", backref="subject")


class Transcripts(db.Model):
    __tablename__ = "transcripts"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    fullname = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    score_C = db.Column(db.Float)
    score_B = db.Column(db.Float)
    score_A = db.Column(db.Float)
    summation_points = db.Column(db.Float)
    cumulative_credit_number = db.Column(db.Integer)
    GPA = db.Column(db.Float)
