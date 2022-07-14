from flask import Blueprint, render_template


Front : Blueprint = Blueprint("Front", __name__)


@Front.route("/")
def IndexPage() -> str:
    return render_template(
        "index.html"
    )


@Front.route("/services")
def ServicesPage() -> str:
    return render_template(
        "services.html"
    )


@Front.route("/about")
def AboutPage() -> str:
    return  render_template(
        "about.html"
    )


@Front.route("/<path:path>/")
def ErrorPage(path, verified=False) -> str:
    return render_template(
        "error.html",
        error=True, 
        verified=verified
    )