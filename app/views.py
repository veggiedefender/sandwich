from flask import render_template, jsonify, request, Response
from datetime import datetime
from app.models import User, Order, Item
from app.emails import send_email, get_activation_link
from app.forms import OrderForm, AdminForm, validate_email
from dateutil.relativedelta import relativedelta, TH
from datetime import datetime, time
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
    epoch = datetime.now().date() - relativedelta(days=1) + relativedelta(weekday=TH(-1))
    epoch = datetime.combine(epoch, time.max)
    orders = Order.query.filter(db.and_(Order.timestamp >= epoch, Order.confirmed))
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
    items.headers["Access-Control-Allow-Origin"] = "*"
    items.headers["Cache-Control"] = "max-age=2628000, public"
    return items    

@app.route("/admin/")
def admin():
    response = Response(render_template("admin.html"))

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    return response

@app.route("/submit", methods=["POST"])
def submit():
    form = OrderForm()
    for error in form.errors.items():
        print(error)
    import sys
    sys.stdout.flush()
    if request.method == "POST" and form.validate():
        email = form.email.data
        if validate_email(email):
            import sys
            sys.stdout.flush()
            user = User.get_or_create(email)
            orders = request.get_json()["order"]
            orders = [ Order(user, order["id"], order["in_half"], order["notes"])
                       for order in orders ]
            place_order(email, orders)
            return jsonify({"success": True})
    return jsonify({"success": False})

@app.route("/", methods=["GET", "POST"])
def index():
    response = Response(render_template("index.html", title="THUNCH"))

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    return response

def split(query):
    length = len(query)
    middle = int(length/2)
    return [query[:middle]] + [query[length - middle:]]