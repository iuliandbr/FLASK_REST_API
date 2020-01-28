import requests

url = 'http://localhost:5000/api/get_data/2'

data = {
    "name": "Product 2",
    "description": "This is product 2 - updated",
    "price": 150.0,
    "qty": 20
}

req = requests.put(url, json=data)
