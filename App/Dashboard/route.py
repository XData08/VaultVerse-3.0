from flask import Blueprint, render_template


Dashboard : Blueprint = Blueprint("Dashboard", __name__)


@Dashboard.route("/vaultverse-dashboard/<string:UserName>")
def DashboardPage(UserName : str) -> str:
    return render_template(
        "user/dashboard.html",
        UserName = UserName
    )