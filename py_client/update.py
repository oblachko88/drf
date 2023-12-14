import requests, json

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello world.",
    "price": 189.99,
}

get_response = requests.put(endpoint, json=data) # HTTP Request
print(get_response.json())