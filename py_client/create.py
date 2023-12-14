import requests

endpoint = "http://localhost:8000/api/products/"
# http://localhost:8000/admin/
# session -> post data
# selenium

data = {
    "title": "This field is done!",
    "price": 20.00,
}

get_response = requests.post(endpoint, json=data) # HTTP Request
print(get_response.json()) 