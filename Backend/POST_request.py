import requests

url = 'http://localhost:5000/api/get_data'

data = {
    "name": "Product 1",
    "description": "This is product 1",
    "price": 150.0,
    "qty": 20
}

req = requests.post(url, json=data)