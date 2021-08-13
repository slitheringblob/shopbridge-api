from productadmin import db,ma

# DB Model
class Item(db.Model):
    item_id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.String(200), nullable=False, unique=True)
    item_desc = db.Column(db.String(200))
    item_price = db.Column(db.Float,nullable=False)

    def __init__(self, item_name, item_desc, item_price):
        self.item_name = item_name
        self.item_desc = item_desc
        self.item_price = item_price

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('item_id','item_name','item_desc','item_price')

item_schema = ItemSchema()
all_item_schema = ItemSchema(many=True)