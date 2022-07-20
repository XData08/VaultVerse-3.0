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


@Front.route("/<path:path>/<string:errmsg>/<string:verified>/<int:code>")
@Front.route("/<path:path>/<string:errmsg>/<string:verified>")
@Front.route("/<path:path>/<string:errmsg>")
@Front.route("/<path:path>")
def ErrorPage(path, errmsg : str, verified : str = "False", code : int = 0) -> str:
    return render_template(
        "error.html",
        isFooterClose=True, 
        isNavigationClose = True, 
        verified=verified,
        errmsg = errmsg,
        code=code
    )