import requests
import pytest


def test_getallItems():
     response = requests.get("http://127.0.0.1:5000/allitems")
     assert response.status_code == 200
     assert response.headers["Content-Type"] == "application/json"

#test if single item GET works for /item/{item_id}
singleItemValidData = [("1","footballdesc","football",300.0)]

@pytest.mark.parametrize("id,item_desc,item_name,item_price", singleItemValidData)
def test_single_item_retrival(id,item_desc,item_name,item_price):
    response = requests.get(f"http://127.0.0.1:5000/item/{id}")
    response_body = response.json()
    assert response_body["item_id"] == int(id)

#test if single item GET works for /item/{item_id}
singleItemInvalidData = [("1","footballdesc","football",100)]

@pytest.mark.parametrize("id,item_desc,item_name,item_price", singleItemInvalidData)
def test_invalid_single_item_retrival(id,item_desc,item_name,item_price):
    response = requests.get(f"http://127.0.0.1:5000/item/{id}")
    response_body = response.json()
    assert response_body["item_price"] == item_price

#testing the put request to update single item
headers = ({'content-type': 'application/json'})
@pytest.mark.parametrize("headers",headers)
def test_single_item_update_data(headers):
    singleItemUpdateData = {
    "item_name":"cricketball",
    "item_desc":"cricketdesc",
    "item_price":20.0
    }
    response = requests.put("http://127.0.0.1:5000/item/1", json=singleItemUpdateData)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200

#testing the delete item request
headers = {'content-type': 'application/json'}
@pytest.mark.parametrize("headers",headers)
def test_delete_item(headers):
    response = requests.delete("http://127.0.0.1:5000/item/3")
    assert response.status_code == 200

    
    




