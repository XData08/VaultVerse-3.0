from flask import Blueprint, render_template


Dashboard : Blueprint = Blueprint("Dashboard", __name__)


@Dashboard.route("/vaultverse-dashboard/<string:FullName>")
def DashboardPage(FullName : str) -> str:
    return render_template(
        "user/dashboard.html",
        FullName = FullName
    )