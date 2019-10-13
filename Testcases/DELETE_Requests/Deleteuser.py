import json

import requests
import jsonpath
url = "https://reqres.in/api/users/2"
response = requests.delete(url)

# fetech response code

print(response.status_code)

assert response.status_code == 204 #for validation


