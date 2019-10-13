import requests
import jsonpath
import json
import openpyxl
from DataDriven import Library


def test_add_multiple_students():

    #API part
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    json_request = json.loads(file.read())  # type casting a simple text file to json format

    obj = Library.Common('F:\\Python_API_Testing\\Api_testing.xlsx',"Sheet1")
    col= obj.fetch_column_count()
    keylist=obj.fetch_key_names()
    row=obj.fetch_row_count()


    for i in range(2,row+1):
        updated_json_request = obj.update_request_with_data(i,json_request,keylist)
        response = requests.post(API_URL,updated_json_request)
        print(response)






