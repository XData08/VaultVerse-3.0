from flask import (
    Blueprint, render_template, request,
    url_for, redirect
)
from flask_login import (
    login_required, 
    current_user
)
from flask_mail import Message
from App.config import EMAIL, PASSWORD
from App import db, mail

Dashboard : Blueprint = Blueprint("Dashboard", __name__)


@Dashboard.route("/vaultverse-dashboard/<int:code>/<string:UserName>", methods=["POST", "GET"])
@login_required 
def DashboardPage(UserName : str, code : int) -> str:

    if request.method == "POST":
        msg = Message(
            "Hello",
            sender = EMAIL,
            html = render_template("components/message.html", code="980234", UserName="WannaCry081"),
            recipients=["liraedata59@gmail.com"]
        )
        mail.send(msg)


    return render_template(
        "user/dashboard.html",
        UserName = UserName,
        user = current_user
    )