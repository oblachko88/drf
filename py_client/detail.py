import requests, json

endpoint = "http://localhost:8000/api/products/1/"

get_response = requests.get(endpoint) # HTTP Request
print(get_response.json())