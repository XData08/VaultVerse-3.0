from flask import Blueprint, render_template


Dashboard : Blueprint = Blueprint("Dashboard", __name__)


@Dashboard.route("/dashboard")
def DashboardPage() -> str:
    return render_template("dashboard.html")