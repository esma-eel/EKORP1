from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from apps.extensions import mail
from apps.utils.tokens import get_reset_password_token


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    app = current_app._get_current_object()
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    token = get_reset_password_token(user)
    send_email(
        "[EKORP1] Reset Your Password",
        sender=current_app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template(
            "auth/email/reset_password.txt", user=user, token=token
        ),
        html_body=render_template(
            "auth/email/reset_password.html", user=user, token=token
        ),
    )
