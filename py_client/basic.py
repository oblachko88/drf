import requests, json

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "Danila", "content":"Hello world!", "price": 20.00}) # HTTP Request

print(get_response.json())


# print(get_response.status_code)
# print(get_response.text) # print raw text response