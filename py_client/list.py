import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done!",
    "price": 20.00,
}

get_response = requests.get(endpoint,) # HTTP Request
print(get_response.json())