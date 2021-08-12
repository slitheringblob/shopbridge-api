from flask import Flask,request,jsonify
import flask_restful
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

##initialize the app
app = Flask(__name__)
##setting the current path as basedir to be used as a relative path for all other files
apibase = os.path.abspath(os.path.dirname(__file__))
##base config for the API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(apibase,'inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##initialize sqlalchemy and marhsmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
## DB Model
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

###routes###
#route to add new item to inventory
@app.route('/item',methods=['POST'])
def addItem():
    item_name = request.json['item_name']
    item_desc = request.json['item_desc']
    item_price = request.json['item_price']

    addnewItem = Item(item_name,item_desc,item_price)
    try:
        db.session.add(addnewItem)
        db.session.commit()
        return item_schema.jsonify(addnewItem)

    except:
        return "Couldnt input data into db"

#route to fetch all items from inventory
@app.route('/allitems',methods=["GET"])
def fetchAllItems():
    allItems = Item.query.all()
    printResult = all_item_schema.dump(allItems)
    return jsonify(printResult)

#route to fetch a single item based on ID
@app.route('/item/<item_id>',methods=["GET"])
def fetchItem(item_id):
    result = Item.query.get(item_id)
    return item_schema.jsonify(result)

#route to update single item based on ID
@app.route('/item/<item_id>',methods=["PUT"])
def udpateItem(item_id):
    oldItem = Item.query.get(item_id)
    #get data from body of request
    item_name = request.json['item_name']
    item_desc = request.json['item_desc']
    item_price = request.json['item_price']

    oldItem.item_name = item_name
    oldItem.item_desc = item_desc
    oldItem.item_price = item_price

    db.session.commit()
    return item_schema.jsonify(oldItem)

#route to fetch a single item based on ID
@app.route('/item/<item_id>',methods=["DELETE"])
def deleteItem(item_id):
    result = Item.query.get(item_id)
    db.session.delete(result)
    db.session.commit()
    return item_schema.jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True)