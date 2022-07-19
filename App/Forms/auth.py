from flask import (
    Blueprint, render_template,
    url_for, redirect, request,
    flash
)
from flask_login import (
    login_required, login_user, logout_user,
    login_remembered
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from App.models import User
from App import db

Forms : Blueprint = Blueprint("Forms", __name__)


@Forms.route("/vaultverse-signin", methods=["POST", "GET"])
def LoginPage() -> str:

    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        password = request.form.get("password")

        _emailAddress = User.query.filter_by(emailAddress = emailAddress).first()

        if len(emailAddress) < 6 or emailAddress == "":
            flash("Invalid Email Address", "warning")
        elif len(password) < 6 or password == "":
            flash("Invalid Password", "warning")
        else:
            if _emailAddress:
                if check_password_hash(_emailAddress.password, password):
                    login_user(_emailAddress, remember=True)
                    return redirect(url_for("Dashboard.DashboardPage", UserName=_emailAddress.userName))
                else:
                    flash("Password does not match" , "error")
            else:
                flash("User does not exist" , "error")
                
    return render_template(
        "login.html",
        isFooterClose  = True
    )
    

@Forms.route("/vaultverse-signup", methods=["POST", "GET"])
def SignupPage() -> str:

    if request.method == "POST":
        userName = request.form.get("userName")
        emailAddress = request.form.get("emailAddress")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        _userName = User.query.filter_by(userName = userName).first()
        _emailAddress = User.query.filter_by(emailAddress = emailAddress).first()
        
        if _userName:
            flash("userName already exist", "warning")
        elif _emailAddress:
            flash("Email Address already exist", "warning")
        elif len(userName) < 5 or userName == "":
            flash("Invalid Username", "warning") 
        elif len(emailAddress) < 8 or emailAddress == "":
            flash("Invalid Email Address", "warning")
        else:  
            if password == "" or confirmPassword == "":
                flash("Invalid Password", "warning")
            else:
                if not len(password) < 6:
                    if password == confirmPassword:

                        new_user = User(
                            userName = userName,
                            emailAddress = emailAddress,
                            password = generate_password_hash(password, "sha256")
                        )
                        
                        db.session.add(new_user)
                        db.session.commit()
                        login_user(new_user)
                        return redirect(url_for("Dashboard.DashboardPage", UserName=userName))
                    else:
                        flash("Password does not match", "error")
                else:
                    flash("Weak password", "warning")


    return render_template(
        "signup.html",
        isFooterClose  = True
    )


@Forms.route("/vaultverse-logout")
@login_required
def LogoutPage() -> str:
    logout_user()
    return redirect(url_for("Forms.LoginPage"))


@Forms.route("/vaultverse-verification", methods=["POST", "GET"])
def VerificationPage() -> str:
    return render_template(
        "verification.html",
        isFooterClose  = True
    )


@Forms.route("/vaultverse-forgotpassword", methods=["POST", "GET"])
def ForgotPasswordPage() -> str:
    return render_template(
        "forgotpassword.html",
        isFooterClose  = True
    )