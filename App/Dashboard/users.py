from flask import (
    Blueprint, render_template
)


Users = Blueprint("Users", __name__)


@Users.route("/vaultverse-user-credentials/<int:code>/<string:UserName>")
def CredentialsPage(UserName : str, code : int) -> str:
    return render_template(
        "user/user_pages/credential.html",
        code=code
    )


@Users.route("/vaultverse-user-records/<int:code>/<string:UserName>")
def RecordsPage(UserName : str, code : int) -> str:
    return render_template(
        "user/user_pages/record.html",
        code=code
    )


@Users.route("/vaultverse-user-files/<int:code>/<string:UserName>")
def FilesPage(UserName : str, code : int) -> str:
    return render_template(
        "user/user_pages/files.html",
        code=code
    )


@Users.route("/vaultverse-user-gallery/<int:code>/<string:UserName>")
def GalleryPage(UserName : str, code : int) -> str:
    return render_template(
        "user/user_pages/gallery.html",
        code=code
    )


@Users.route("/vaultverse-user-help/<int:code>/<string:UserName>")
def HelpPage(UserName : str, code : int) -> str:
    return render_template(
        "user/user_pages/help.html",
        code=code
    )

