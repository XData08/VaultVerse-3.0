from flask import Blueprint, render_template


Forms : Blueprint = Blueprint("Forms", __name__)


@Forms.route("/Forms/login")
def LoginPage() -> str:
    return render_template("login.html")
    

@Forms.route("/Forms/signup")
def SignupPage() -> str:
    return render_template("signup.html")