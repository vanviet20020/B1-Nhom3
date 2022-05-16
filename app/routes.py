from this import s
from app import app
from app import form
from app.models import *
from app.form import *
from flask import render_template, request, redirect, flash, url_for


@app.route("/")
def index():
    return render_template("index.html", title="Trang chủ")


@app.route("/transcripts")
def view_list_transcripts():
    students = Student.query.all()
    return render_template(
        "view_list_transcripts.html",
        students=students,
        title="Quản lý điểm các sinh viên",
    )


@app.route("/transcripts/<int:student_id>")
def view_transcripts(student_id):
    student = Student.query.filter_by(id=student_id).first()
    transcripts = Transcripts.query.filter_by(student_id=student_id)
    subjects = Subject.query.all()
    return render_template(
        "view_transcripts.html",
        transcripts=transcripts,
        student=student,
        subjects=subjects,
        title="Quản lý điểm",
    )


@app.route("/transcripts/create/<int:student_id>")
def create_transcripts(student_id):
    student = Student.query.filter_by(id=student_id).first()
    subjects = Subject.query.all()
    return render_template(
        "create_transcripts.html",
        student=student,
        subjects=subjects,
        title="Tạo môn học mới",
    )


@app.route("/transcripts/create/<int:student_id>/success", methods=["POST"])
def create_transcript_success(student_id):
    subject_id = request.form.get("subject_id")
    new_transcript = Transcripts(student_id=student_id, subject_id=subject_id)
    db.session.add(new_transcript)
    db.session.commit()
    flash("Thêm môn học mới cho sinh viên thành công")
    return redirect(url_for("view_transcripts", student_id=student_id))


@app.route(
    "/transcripts/update/<int:student_id>/<int:transcript_id>", methods=["GET", "POST"]
)
def update_transcripts(student_id, transcript_id):
    form = FormUpdateTranscripts()
    if form.validate_on_submit():
        new_score_C = float(form.score_C.data)
        new_score_B = float(form.score_B.data)
        new_score_A = float(form.score_A.data)
        new_summation_points = (new_score_C + new_score_B * 3 + new_score_A * 6) / 10
        # validate score on submit
        def validate_score_C(self, new_score_C):
            if new_score_C < 0 or new_score_C > 100:
                raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

        def validate_score_B(self, new_score_B):
            if new_score_B < 0 or new_score_B > 100:
                raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

        def validate_score_B(self, new_score_B):
            if new_score_B < 0 or new_score_B > 100:
                raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

        # update score
        new_transcripts = Transcripts.query.filter_by(id=transcript_id).first()
        new_transcripts.score_C = new_score_C
        new_transcripts.score_B = new_score_B
        new_transcripts.score_A = new_score_A
        new_transcripts.summation_points = new_summation_points
        db.session.commit()
        flash("Nhập điểm cho sinh viên thành công")
        return redirect(url_for("view_transcripts", student_id=student_id))
    return render_template(
        "update_transcripts.html",
        form=form,
        transcript_id=transcript_id,
        title="Nhập điểm cho sinh viên",
    )


@app.route("/transcripts/delete/<int:student_id>/<int:transcript_id>")
def delete_transscripts(student_id, transcript_id):
    delete_transcripts = Transcripts.query.filter_by(id=transcript_id).first()
    db.session.delete(delete_transcripts)
    db.session.commit()
    flash("Xoá môn học thành công")
    return redirect(url_for("view_transcripts", student_id=student_id))
