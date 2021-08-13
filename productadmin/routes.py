from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from productadmin.models import ItemSchema,Item,item_schema,all_item_schema
from productadmin import app,db,ma

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