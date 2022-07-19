DB_NAME : str = "VaultVerse.db"
EMAIL : str = "XDApplication.HelpCenter@gmail.com"
PASSWORD : str = "ytmhweidldndvmhw"


class Config:

    SECRET_KEY = "6T5JJ5V0XR0PEC3NNDQZ"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = EMAIL
    MAIL_PASSWORD = PASSWORD 
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True 
