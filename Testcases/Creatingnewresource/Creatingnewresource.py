import requests
import jsonpath
import json
url = "https://reqres.in/api/users"

#read input json file

file = open('F:\\Python_API_Testing\\createuser.json','r')
json_input=file.read()
request_json = json.loads(json_input)

#make post request with json input body

response = requests.post(url,request_json)

print(response.content)

assert response.status_code == 201 #validating response code


#fetch header form response

print(response.headers)

print(response.headers.get('Content-Length'))

# parse response to json format

response_json = json.loads(response.text)

#pick id using json path

id1 = jsonpath.jsonpath(response_json,'id')

print(id1[0])



