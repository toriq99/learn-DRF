import requests

# endpoint = 'http://www.httpbin.org/status/200/'
# endpoint = 'http://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/1/update'

data = {
    "title": "Update title",
    "price": 123.5
}

get_response = requests.put(endpoint, data) # HTTP Request

print(get_response.json())