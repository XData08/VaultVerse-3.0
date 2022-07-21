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


@Front.route("/<string:errmsg>/<string:verified>/<int:code>/<path:path>/")
@Front.route("/<string:errmsg>/<string:verified>/<path:path>/")
@Front.route("/<string:errmsg>/<path:path>/")
@Front.route("/<path:path>")
def ErrorPage(path, errmsg : str = "", verified : str = "False", code : int = 0) -> str:

    if errmsg == "":
        errmsg = """
            Web Page does not Exists.
        
        """

    return render_template(
        "error.html",
        isFooterClose=True, 
        isNavigationClose = True, 
        verified=verified,
        errmsg = errmsg,
        code=code
    )