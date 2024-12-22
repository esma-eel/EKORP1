from flask_login import LoginManager
from apps.extensions.database import db
from apps.users.models import User

login_manager = LoginManager()


def init_login(app):
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please Login and try again."


@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
