import requests
from getpass import getpass

# endpoint = 'http://www.httpbin.org/status/200/'
# endpoint = 'http://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/'
auth_endpoint = 'http://localhost:8000/api/auth/'
password = getpass()


auth_response = requests.post(auth_endpoint, json={'username': 'admin', 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = 'http://localhost:8000/api/products/'

    get_response = requests.get(endpoint, headers=headers) # HTTP Request
    print(get_response.json())