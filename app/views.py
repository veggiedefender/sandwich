from flask import render_template, jsonify, request
from datetime import datetime
from app.models import User, Order, Item
from app.emails import send_email, get_activation_link
from app.forms import OrderForm, validate_email
from dateutil.relativedelta import relativedelta, TH
from datetime import datetime
from app import app, db

def place_order(email, orders):
    total = 0
    for order in orders:
        db.session.add(order)
        total += order.cost
    db.session.commit()
    activation_link = get_activation_link(orders)
    letter = render_template("emails/confirmation.txt",
        orders=orders,
        link=activation_link,
        total=total
    )
    send_email("Order confirmation", [email], letter)

@app.route("/complete/")
def complete():
    return render_template("complete.html")

@app.route("/orders/")
def orders():
    epoch = datetime.utcnow().date() + relativedelta(weekday=TH(-1))
    #orders = Order.query.filter(db.and_(Order.timestamp >= epoch, Order.confirmed))
    orders = Order.query.filter_by(confirmed=True).all()
    total = sum([ order.cost for order in orders ])
    return render_template("orders.html", orders=orders, epoch=epoch, total=total)

@app.route("/items/")
def items():
    items = Item.query.all()
    items = jsonify([{
        "id": item.id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "price_half": item.price_half
    } for item in items])
    items.headers['Access-Control-Allow-Origin'] = '*'
    return items    

@app.route("/admin/")
def admin():
    pass

@app.route("/submit", methods=["POST"])
def submit():
    form = OrderForm()
    if request.method == "POST" and form.validate():
        email = form.email.data
        if validate_email(email):
            print("yes it is working")
            import sys
            sys.stdout.flush()
            user = User.get_or_create(email)
            orders = request.get_json()["order"]
            orders = [ Order(user, order["id"], order["in_half"], order["notes"])
                       for order in orders ]
            place_order(email, orders)
            return render_template("complete.html")
    return "error", 404

@app.route("/", methods=["GET", "POST"])
def index():
    form = OrderForm()
    if request.method == "POST" and form.validate():
        email = form.email.data
        if validate_email(email):
            print("yes it is working")
            import sys
            sys.stdout.flush()
            user = User.get_or_create(email)
            orders = request.get_json()["order"]
            orders = [ Order(user, order["id"], order["in_half"], order["notes"])
                       for order in orders ]
            place_order(email, orders)
            return render_template("complete.html")
        else:
            return "error", 404
    return render_template("index.html", form=form)

def split(query):
    length = len(query)
    middle = int(length/2)
    return [query[:middle]] + [query[length - middle:]]