from app import app
from app import form
from app.models import *
from app.form import *
from flask import render_template, request, redirect, flash, url_for


@app.route("/")
def index():
    return render_template("index.html", title="Trang chủ")


@app.route("/management_page/transcripts/create")
def create_transcript():
    students = Student.query.all()
    subjects = Subject.query.all()
    return render_template(
        "createTranscipt.html",
        title="Tạo bảo điểm cho môn học mới",
        students=students,
        subjects=subjects,
    )


@app.route("/management_page/transcripts")
def management_page_transcripts():
    transcripts = Transcripts.query.all()
    return render_template(
        "managementPageTranscripts.html",
        title="Trang quản lý bảng điểm",
        transcripts=transcripts,
    )
