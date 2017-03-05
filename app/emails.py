from flask import abort, redirect, flash, url_for, render_template
from itsdangerous import URLSafeSerializer, BadSignature
from flask_mail import Message
from app.decorators import async
from app.models import Order, User
from app import mail, app, db

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/confirm/<payload>')
def confirm_order(payload):
    s = get_serializer()
    try:
        order_ids = s.loads(payload)
    except BadSignature:
        abort(404)

    for order_id in order_ids:
        order = Order.query.get_or_404(order_id)
        order.confirm()
        db.session.add(order)
    db.session.commit()
    return render_template("confirmed.html")

def send_email(subject, recipients, body):
    sender=app.config["MAIL_USERNAME"]
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body
    send_async_email(app, msg)

def get_activation_link(orders):
    s = get_serializer()
    payload = s.dumps([order.id for order in orders ])
    return url_for('confirm_order', payload=payload, _external=True)

def get_serializer(secret_key=None):
    if secret_key is None:
        secret_key = app.secret_key
    return URLSafeSerializer(secret_key)
