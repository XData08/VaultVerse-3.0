from flask import (
    Blueprint, render_template,
    url_for, redirect
)


Forms : Blueprint = Blueprint("Forms", __name__)


@Forms.route("/Forms/login")
def LoginPage() -> str:
    return render_template(
        "login.html",
        isFooterClose  = True
    )
    

@Forms.route("/Forms/signup")
def SignupPage() -> str:
    return render_template(
        "signup.html",
        isFooterClose  = True
    )


@Forms.route("/Forms/logout")
def LogoutPage() -> str:
    return redirect(url_for("Forms.LoginPage"))


@Forms.route("/Forms/verification")
def VerificationPage() -> str:
    return render_template(
        "verification.html"
    )