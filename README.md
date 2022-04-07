# shopbridge-api
 Exmaple Product Inventory API for ShopBridge made using Flask, SQLite, SQLAlchemy and Marshmallow. Basic GET/POST/PUT/DELETE endpoints showing the integration between Flask, SQLite, SQLAlchemy and Marshmallow.
 
## Endpoints:

| Endpoint | HTTP Method | Usage | Returns |
| :---         |     :---:      |  :---: | ---:|
| /item   | POST | Enter new item into Inventory   | Returns JSON of item added |
| /allitems | GET | Return all items in the inventory | Return JSON of all items in the inventory |
| /item/<item_id> | GET | Fetch data for a single item based on ID | Returns JSON of Item based on ID |
| /item/<item_id> | PUT | Update fields for item based on ID | Returns JSON of item containing updated data |
| /item/<item_id> | DELETE | Delete item from Inventory based on ID | Returns JSON of deleted Item |

## Setup:
* Clone the repo to the target directory.
* Create a virtual environment using the `python -m venv venv` command in the target directory.
* Navigate to the `/venv/Scripts` folder and run the `activate` batch file to start the virtual environment.
* Use `pip install -r requirements.txt` to get all the requirements installed to run the API.
* use `python run.py` to run the API.
* use `pytest test_ProductAdmin.py` to run the testing module.



