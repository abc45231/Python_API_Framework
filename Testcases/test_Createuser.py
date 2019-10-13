import requests
import jsonpath
import json
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open('F:\\Python_API_Testing\\createuser.json', 'r')

@pytest.mark.Smoke
def test_create_new_user(start_exec):

    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201  # validating response code
    response_json = json.loads(response.text)
    id1 = jsonpath.jsonpath(response_json, 'id')
    print(id1[0])

@pytest.mark.Sanity
def test_create_other_user(start_exec):
        file = open('F:\\Python_API_Testing\\createuser.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        response = requests.post(url, request_json)
        assert response.status_code == 201  # validating response code
        response_json = json.loads(response.text)
        id1 = jsonpath.jsonpath(response_json, 'id')
        print(id1[0])










