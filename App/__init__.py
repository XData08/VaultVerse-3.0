from flask import Flask
from App.config import Config

def create_app(class_config = Config) -> Flask:

    app : Flask = Flask(__name__)
    app.config.from_object(class_config)

    from App.Front.route import Front
    from App.Dashboard.route import Dashboard
    from App.Forms.auth import Forms

    app.register_blueprint(Front, url_prefix="/")
    app.register_blueprint(Dashboard, url_prefix="/")
    app.register_blueprint(Forms, url_prefix="/")

    return app