import requests
import jsonpath
import json
url = "https://reqres.in/api/users/2"

#read input json file

file = open('F:\\Python_API_Testing\\createuser.json','r')
json_input=file.read()
request_json = json.loads(json_input)

#make PUT request with json input body

response = requests.put(url,request_json)

print(response.content)

assert response.status_code == 200 #validating response code


#fetch header form response

print(response.headers)

print(response.headers.get('Content-Length'))

# parse response to json format

response_json = json.loads(response.text)

#pick id using json path

updated_li = jsonpath.jsonpath(response_json,'updatedAt')

print(updated_li[0])
