from time import time
import jwt
from flask import current_app

from apps.core.extensions import db
from apps.core.db import User


def generate_token(payload_data):
    return jwt.encode(
        payload_data,
        current_app.config.get("SECRET_KEY"),
        algorithm="HS256",
    )


def generate_expirable_token(payload_data, expires_in=600):
    payload_data_with_exp = {**payload_data, "exp": time() + expires_in}
    return generate_token(payload_data_with_exp)


def verify_token(token):
    payload_data = jwt.decode(
        token, current_app.config.get("SECRET_KEY"), algorithms=["HS256"]
    )
    return payload_data


def get_reset_password_token(user, expires_in=600):
    payload_data = {"reset_password": user.id}
    return generate_expirable_token(payload_data, expires_in=expires_in)


def verify_reset_password_token(token):
    try:
        payload_data = verify_token(token)
        id = payload_data["reset_password"]
    except:
        return
    return db.session.get(User, id)
