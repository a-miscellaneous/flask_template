from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging
import random
import os

# Create and configure the logger
logger = logging.getLogger("LOGGER")
logger.setLevel(logging.DEBUG)
os.makedirs("../instance", exist_ok=True)
fh = logging.FileHandler("../instance/service.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Create the db
db = SQLAlchemy()
DB_NAME = "database.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"

# random cookie key
SECRET_KEY = ''.join(random.choice(
    'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    db.init_app(app)

    from .home import home
    from .auth import auth

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User

    with app.app_context():
        db.create_all()
        # addAllTrackableItems()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
