from app.models import Item

items = Item.query.order_by(Item.id).all()

for item in items:
    print("%s\t%s\t%s\t%s" % (item.name, item.category, item.price, item.price_half))