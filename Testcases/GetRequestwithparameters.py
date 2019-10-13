import requests

params={'name':'testingworld','email':'kn@gmail.com'}
response = requests.get("https://httpbin.org/get",params=params)

print(response.text)

