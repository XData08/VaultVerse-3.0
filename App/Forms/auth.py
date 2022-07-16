from flask import (
    Blueprint, render_template,
    url_for, redirect
)


Forms : Blueprint = Blueprint("Forms", __name__)


@Forms.route("/vaultverse-signin")
def LoginPage() -> str:
    return render_template(
        "login.html",
        isFooterClose  = True
    )
    

@Forms.route("/vaultverse-signup")
def SignupPage() -> str:
    return render_template(
        "signup.html",
        isFooterClose  = True
    )


@Forms.route("/vaultverse-logout")
def LogoutPage() -> str:
    return redirect(url_for("Forms.LoginPage"))


@Forms.route("/vaultverse-verification")
def VerificationPage() -> str:
    return render_template(
        "verification.html",
        isFooterClose  = True
    )


@Forms.route("/vaultverse-forgotpassword")
def ForgotPasswordPage() -> str:
    return render_template(
        "forgotpassword.html",
        isFooterClose  = True
    )