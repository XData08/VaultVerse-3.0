from blinker import receiver_connected
from flask import (
    Blueprint, render_template,
    request, redirect, url_for,
    flash
)
from flask_mail import Message
from App.config import EMAIL
from App import mail


Front : Blueprint = Blueprint("Front", __name__)


@Front.route("/", methods=["POST", "GET"])
def IndexPage() -> str:
    
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        try:
            msg = Message(
                "Thank you! For Subscribing.",
                sender=EMAIL,
                html=render_template("components/newsletter.html"),
                recipients=[emailAddress]
            )
            mail.send(msg)
            flash("Thank you for Subscribing to VaultVerse! Check Email for Newsletter.", "success")
            
        except Exception as e:
            return redirect(url_for("Front.ErrorPage", path="/error/", error=e))

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