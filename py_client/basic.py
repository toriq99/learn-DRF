import requests

# endpoint = 'http://www.httpbin.org/status/200/'
# endpoint = 'http://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'


get_response = requests.get(endpoint, params={
    "test": 123,
    "query":"insert query Here"})

print(get_response.json())
# print(get_response.text)
print(get_response.status_code)