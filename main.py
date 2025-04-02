from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient
import json
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
import requests
import pydantic
app = FastAPI()

# use pydanitc to validate the input
class Product(pydantic.BaseModel):
    item_id: str
    name: str
    price: float
    quantity: int
    description: str

# home root
@app.get("/")
def read_root():

    Product(item_id="xxxxxxx", name="test", price=1.0, quantity=1, description="test")




    return {"Hello": "World"}

# get single product
@app.get("/getSingleProduct/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    

    Product(item_id="xxxx", name="test", price=1.0, quantity=1, description="test")
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA  
    collection = db.products
    
    
    results = dumps(collection.find_one({"Product ID": item_id}))
    return json.loads(results)



# getAll products
@app.get("/getAll")
def read_items(q: Union[str, None] = None):
        Product(item_id="item_id", name="test", price=1.0, quantity=1, description="test")
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.CA
        collection = db.products
        results = dumps(collection.find())
        return json.loads(results)


# add New
@app.post("/addNew/{item_id}/{name}/{price}/{quantity}/{description}")
def create_item(item_id: str, name: str, price: float, quantity: int, description: str):
    Product(item_id="item_id", name="test", price=1.0, quantity=1, description="test")
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA
    collection = db.products
    
    #insert the data through the parameters 
    collection.insert_one({"Product ID": item_id, "Name": name, "Price": price, "Quantity": quantity, "Description": description})

    return {"item_id": item_id, "name": name, "price": price, "quantity": quantity, "description": description}

# deleteOne
@app.delete("/deleteOne/{item_id}")
def delete_item(item_id: str):
    Product(item_id="test", name="test", price=1.0, quantity=1, description="test")
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA
    collection = db.products
    
    # delete the item with the given id
    collection.delete_one({"Product ID": item_id})
    return {"item_id": item_id}

# startsWith
@app.get("/startsWith/{letter}")
def starts_with(letter: str):
    Product(item_id="test", name="test", price=1.0, quantity=1, description="test")

    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA
    collection = db.products

    # find all the items that start with the given letter
    results = dumps(collection.find({"Name": {"$regex": "^" + letter}}))
    return json.loads(results)


# paginate
@app.get("/paginate/{start_id}/{end_id}")
def paginate(start_id: str, end_id: str):
    Product(item_id="test", name="test", price=1.0, quantity=1, description="test")

    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA
    collection = db.products

    # $gte is greater than or equal to and $lte is less than or equal to and $lte is less than or equal to
    results = dumps(collection.find({"Product ID": {"$gte": start_id, "$lte": end_id}}).limit(10))
    return json.loads(results)


@app.get("/convert/{item_id}")
def convert(item_id: str):
    Product(item_id="test", name="test", price=1.0, quantity=1, description="test")
    
    # Connect to MongoDB
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.CA
    collection = db.products

    # Fetch the product by item_id
    product = collection.find_one({"Product ID": item_id})
    

    # Get the price in USD
    price_usd = product.get("Unit Price", 0.0)
    print(price_usd)

    # Call the exchange rate API to get the USD to EUR conversion rate
    api_url = "https://v6.exchangerate-api.com/v6/8f712c596a2c964c6cac8ecf/latest/USD"
    
    response = requests.get(api_url, params={"base_code": "USD"})
    print(response)


    # Parse the response to get the converted price
    data = response.json()
    
    price_eur = data["conversion_rates"]["EUR"]


    print("----------")
    print(price_eur)

    # parse the data to get the converted price
    price_eur = price_usd * price_eur

    # Return the original and converted prices
    return {
        "item_id": item_id,
        "price_usd": price_usd,
        "price_eur": price_eur
    }