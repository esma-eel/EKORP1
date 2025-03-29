from .database_ex import db, migrate, init_db
from .login_ex import login_manager, init_login
from .mail_ex import mail, init_mail


def init_extensions(app):
    init_db(app)
    init_login(app)
    init_mail(app)
