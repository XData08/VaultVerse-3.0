from flask import (
    Blueprint, render_template,
    url_for, redirect, request,
    flash
)
from flask_login import (
    login_required, login_user, 
    logout_user, current_user
)
from flask_mail import Message
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from App.Forms.code import GenerateCode
from App.models import User, Verification
from App import db, mail
from App.config import EMAIL


Forms : Blueprint = Blueprint("Forms", __name__)
VERIFICATION_CODE : str = ""


@Forms.route("/vaultverse-signin", methods=["POST", "GET"])
def LoginPage() -> str:
    global VERIFICATION_CODE
    
    try:
        if request.method == "POST":
            emailAddress = request.form.get("emailAddress")
            password = request.form.get("password")

            _emailAddress = User.query.filter_by(emailAddress = emailAddress).first()
            
            if emailAddress != "" or password != "":
                if len(emailAddress) < 10 or emailAddress == "":
                    flash("Email Address is invalid or already taken.", "warning")
                elif len(password) < 8 or password == "":
                    flash("Please Enter a Password.", "warning")
                else:
                    if _emailAddress:
                        if check_password_hash(_emailAddress.password, password):
                            if VERIFICATION_CODE == "":
                                VERIFICATION_CODE = GenerateCode()
                            msg = Message(
                                "Verification Code",
                                sender = EMAIL,
                                html = render_template("components/message.html", code = VERIFICATION_CODE, UserName=_emailAddress.userName),
                                recipients=[emailAddress]
                            )
                            mail.send(msg)
                            login_user(_emailAddress, remember=True)
                            return redirect(url_for("Forms.VerificationPage", EmailAddress=emailAddress))
                        else:
                            flash("Password does not match" , "error")
                    else:
                        flash("User does not exist" , "error")
            else:
                flash("Please complete all required fields.", "error")
    except Exception as e:
        return redirect(url_for('Front.ErrorPage', path="/error/", errmsg=e))
                
    return render_template(
        "login.html",
        isFooterClose  = True
    )
    

@Forms.route("/vaultverse-signup", methods=["POST", "GET"])
def SignupPage() -> str:
    global VERIFICATION_CODE

    try:
        if request.method == "POST":
            userName = request.form.get("userName")
            emailAddress = request.form.get("emailAddress")
            password = request.form.get("password")
            confirmPassword = request.form.get("confirmPassword")

            _userName = User.query.filter_by(userName = userName).first()
            _emailAddress = User.query.filter_by(emailAddress = emailAddress).first()

            
            if userName != "" or emailAddress != "" or password != "" or confirmPassword != "":
                if _userName:
                    flash("Username already exists.", "warning")
                elif _emailAddress:
                    flash("Email Address is invalid or already taken.", "warning")
                elif len(userName) < 5 or userName == "":
                    flash("Username must be at least 5 characters long.", "warning") 
                elif len(emailAddress) < 10 or emailAddress == "":
                    flash("Email Address is invalid or already taken.", "warning")
                else:  
                    if password == "" or confirmPassword == "":
                        flash("Please enter a strong password.", "warning")
                    else:
                        if not len(password) < 8:
                            if password == confirmPassword:
                                if VERIFICATION_CODE == "":
                                    VERIFICATION_CODE = GenerateCode()
                                new_user = User(
                                    userName = userName,
                                    emailAddress = emailAddress,
                                    password = generate_password_hash(password, "sha256")
                                )
                                db.session.add(new_user)
                                db.session.commit()

                                msg = Message(
                                    "Verification Code",
                                    sender = EMAIL,
                                    html = render_template("components/message.html", code = VERIFICATION_CODE, UserName=userName),
                                    recipients=[emailAddress]
                                )
                                mail.send(msg)
                                login_user(new_user)
                                return redirect(url_for("Forms.VerificationPage", EmailAddress=emailAddress))
                            else:
                                flash("Password does not match.", "error")
                        else:
                            flash("Password must be at least 8 characters long.", "warning")
            else:
                flash("Please complete all required fields.", "error")

    except Exception as e:
        return redirect(url_for('Front.ErrorPage', path="/error/", errmsg=e))

    return render_template(
        "signup.html",
        isFooterClose  = True
    )


@Forms.route("/vaultverse-logout")
@login_required
def LogoutPage() -> str:
    logout_user()
    return redirect(url_for("Forms.LoginPage"))


@Forms.route("/vaultverse-verification/<string:EmailAddress>", methods=["POST", "GET"])
@login_required
def VerificationPage(EmailAddress : str) -> str:
    global VERIFICATION_CODE

    try:
        if request.method == "POST":
    
            user = User.query.filter_by(emailAddress = EmailAddress).first()
            userCode : str = ""

            for i in range(1, 7):
                userCode += request.form.get(f"code{i}")
    
            if userCode != " ":
                if userCode == VERIFICATION_CODE:
                    VERIFICATION_CODE = ""
                    if user.id == 1:
                        return redirect(url_for("Dashboard.AdminPage",
                            UserName=user.userName, code=userCode))
                    else:
                        return redirect(url_for("Dashboard.DashboardPage", 
                            UserName=user.userName, code=userCode))
                else:
                    flash("Verification code does not match.", "warning")
            else:
                flash("Please input the verification code sent to your email.", "error")

    except Exception as e:
        return redirect(url_for('Front.ErrorPage', path="/error/", errmsg=e, verified="False"))


    return render_template(
        "verification.html",
        isFooterClose  = True,
        isNavigationClose = True,
        EmailAddress = EmailAddress
    )


@Forms.route("/vaultverse-forgotpassword", methods=["POST", "GET"])
def ForgotPasswordPage() -> str:

    if request.method == "POST":
        try:
            emailAddress = request.form.get("emailAddress")
            question = request.form.get("question")
            answer = request.form.get("answer")

            if question != "0" or emailAddress != "" or answer != "":
                user = User.query.filter_by(emailAddress=emailAddress).first()
                if user:
                    # need to verify answer
                    msg = Message(
                        "Temporary Password",
                        sender = EMAIL,
                        html = render_template("components/forgotpassword.html", code = GenerateCode(), UserName=user.userName),
                        recipients=[emailAddress]
                    )
                    mail.send(msg)
                    return redirect(url_for("Forms.LoginPage"))

                else:
                    flash("User does not exist", "warning")
            else:
                flash("Please complete all required fields.", "error")
     
        except Exception as e:
            return redirect(url_for('Front.ErrorPage', path="/error/", errmsg=e))


    return render_template(
        "forgotpassword.html",
        isFooterClose  = True
    )


@Forms.route("/resend")
@login_required
def ResendEmail():
    global VERIFICATION_CODE

    VERIFICATION_CODE = GenerateCode()
    msg = Message(
        "Verification Code",
        sender = EMAIL,
        html = render_template("components/message.html", code = VERIFICATION_CODE, UserName=current_user.userName),
        recipients=[current_user.emailAddress]
    )
    mail.send(msg)

    return redirect(url_for('Forms.VerificationPage', EmailAddress=current_user.emailAddress))