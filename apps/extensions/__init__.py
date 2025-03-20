from .database import db, migrate, init_db
from .login import login_manager, init_login


def init_extensions(app):
    init_db(app)
    init_login(app)
