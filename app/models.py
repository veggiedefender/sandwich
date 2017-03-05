from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    #basic user info
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True, nullable=False, unique=True)
    orders = db.relationship("Order", backref="user", lazy="dynamic")

    @staticmethod
    def get_or_create(email):
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
        return user

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    in_half = db.Column(db.Boolean, index=True, default=False)
    notes = db.Column(db.String, index=True, nullable=True)
    cost = db.Column(db.Float, index=True, nullable=False)

    user_id =   db.Column(db.Integer, db.ForeignKey("users.id"))
    
    confirmed = db.Column(db.Boolean, index=True, default=False)
    def confirm(self):
        self.confirmed = True

    def __init__(self, user, item_id, in_half, notes=None):
        with db.session.no_autoflush:
            self.timestamp = datetime.utcnow()
            self.user = user
            self.item_id = item_id
            self.item = Item.query.get(item_id)
            self.in_half = in_half
            if self.item.price == self.item.price_half:
                self.in_half = False
            self.notes = notes
            self.cost = self.calculate_cost()

    def calculate_cost(self):
        if self.in_half:
            return self.item.price_half
        else:
            return self.item.price

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    category = db.Column(db.String, index=True, nullable=False)
    price = db.Column(db.Float, index=True, nullable=False)
    price_half = db.Column(db.Float, index=True, nullable=True)
    orders = db.relationship("Order", backref="item", lazy="dynamic")

    def __init__(self, id, name, category, price_half, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.price_half = price_half
        db.session.add(self)
