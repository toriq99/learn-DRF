import requests

# endpoint = 'http://www.httpbin.org/status/200/'
# endpoint = 'http://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/'


get_response = requests.get(endpoint) # HTTP Request

print(get_response.json())