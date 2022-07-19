from cmath import log
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from App.config import Config, DB_NAME
from os.path import exists


db : SQLAlchemy = SQLAlchemy()
mail : Mail = Mail()
login_manager : LoginManager = LoginManager()
login_manager.login_view = "Forms.LoginPage"


def create_app(class_config : Config = Config) -> Flask:

    app : Flask = Flask(__name__)
    app.config.from_object(class_config)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    Bootstrap(app)


    from App.Front.route import Front
    from App.Dashboard.route import Dashboard
    from App.Forms.auth import Forms
    from App.models import User, Verfication


    app.register_blueprint(Front, url_prefix="/")
    app.register_blueprint(Dashboard, url_prefix="/")
    app.register_blueprint(Forms, url_prefix="/")

    create_db(app)

    return app


def create_db(app : Flask) -> None:
    if not exists("database/" + DB_NAME):
        db.create_all(app=app)
        print("====== SUCCESSFULLY CREATED DATABASE ======")

    return 
        