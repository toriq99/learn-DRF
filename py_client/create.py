import requests

# endpoint = 'http://www.httpbin.org/status/200/'
# endpoint = 'http://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/'

data = {
    "title" : "This field has done"
}

get_response = requests.post(endpoint, json=data) # HTTP Request

print(get_response.json())