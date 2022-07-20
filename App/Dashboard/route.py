from flask import (
    Blueprint, render_template, request,
    url_for, redirect
)
from flask_login import (
    login_required, 
    current_user
)
from App.config import EMAIL, PASSWORD
from App import db

Dashboard : Blueprint = Blueprint("Dashboard", __name__)


@Dashboard.route("/vaultverse-dashboard/<int:code>/<string:UserName>", methods=["POST", "GET"])
@login_required 
def DashboardPage(UserName : str, code : int) -> str:

    if request.method == "POST":
        try:
            x = 23 
            x /= 0
        except Exception as e:
            return redirect(url_for('Front.ErrorPage', path="/error/", errmsg=e, verified="True", code=code))


    return render_template(
        "user/dashboard.html",
        UserName = UserName
    )