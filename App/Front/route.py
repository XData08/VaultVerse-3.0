from flask import Blueprint, render_template


Front : Blueprint = Blueprint("Front", __name__)


@Front.route("/")
def IndexPage() -> str:
    return render_template("index.html")