DB_NAME : str = "VaultVerse.db"

class Config:
    SECRET_KEY = "6T5JJ5V0XR0PEC3NNDQZ"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False