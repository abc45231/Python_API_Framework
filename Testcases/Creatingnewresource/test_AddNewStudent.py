import requests
import jsonpath
import json

def test_add_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    json_request=json.loads(file.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147050"
    response=requests.get(API_URL)
   # json_response = json.loads(response.text)

    json_response = response.json()
    id=jsonpath.jsonpath(json_response,'data.id')

    assert id[0] == 147054

def test_put_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/147054"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    json_request=json.loads(file.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147054"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147050"
    response=requests.get(API_URL)

