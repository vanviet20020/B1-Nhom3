from app import app
from app import form
from app.models import *
from app.form import *
from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required


@app.route("/")
def index():
    return render_template("index.html")


# -----------Sign up-----------
@app.route("/signUp", methods=["GET", "POST"])
def signUp():
    form = SignUpForm()

    # sau khi signUp_form.html submit
    if form.validate_on_submit():
        code = form.code.data
        password = form.password.data
        if code.find("Tea") >= 0:
            role = "teacher"
        else:
            role = "student"

        NewUser = User(code=code, password=password, role=role)

        NewUser.set_password(password)

        def validate_code(self, code):
            code = User.query.filter_by(code=code.data).first()
            if code is not None:
                raise ValidationError(
                    "Code has been already used! Please use a different code."
                )

        db.session.add(NewUser)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("index"))
    return render_template("signUp.html", form=form)


# -----------Login-----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(code=form.code.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid code or password")
            return redirect(url_for("login"))
        login_user(user)
        next_page = request.args.get("next")  # lấy giá trị next trên URL=L
        if not next_page:
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logout success!")
    return redirect(url_for("index"))


@app.route("/pageManagement")
def pageManagement():
    return render_template("pageManagement.html")


@app.route("/pageManagement/users")
def pageManagementUsers():
    users = User.query.all()
    return render_template("pageManagementUser.html", users=users)


@app.route("/pageManagement/transcripts")
def pageManagementTranscripts():
    transcripts = Transcripts.query.all()
    return render_template("pageManagementTranscripts.html", transcripts=transcripts)
