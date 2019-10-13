import json

import requests
import jsonpath
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)



json_response = json.loads(response.text)

for i in range(0,3):
    first_names = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_names[0])