from flask import (
    Blueprint, render_template
)


Admin = Blueprint("Admin", __name__)


@Admin.route("/vaultverse-admin-users/<int:code>/<string:UserName>")
def UsersPage(UserName : str, code : int) -> str:
    return render_template(
        "user/admin_pages/users.html",
        code=code,
        IsAdmin = True
    )


@Admin.route("/vaultverse-admin-feedback/<int:code>/<string:UserName>")
def FeedbackPage(UserName : str, code : int) -> str:
    return render_template(
        "user/admin_pages/feedback.html",
        code=code,
        IsAdmin = True
    )