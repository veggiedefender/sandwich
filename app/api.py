from flask import jsonify, request, render_template
from app.models import User, Order, Item
from app.views import place_order
from app.forms import validate_email
from app import app, db, csrf_protect

@app.route("/api/order", methods=["GET", "POST"])
@csrf_protect.exempt
def api_order():
    if request.method == "POST":
        try:
            data = request.get_json()
            email = data["email"]
            if validate_email(email):
                user = User.get_or_create(email)
                orders = data["order"]        
                orders = [ Order(user, order["id"], order.get("in_half"), order.get("notes"))
                           for order in orders ]
                place_order(email, orders)
            return jsonify({"success": True})
        except:
            return jsonify({"success": False})
    else:
        return render_template("api_error.html",
            message="This endpoint only accepts POST requests!",
            link="https://github.com/veggiedefender/sandwich/blob/master/api.md#apiorder"
        ), 405