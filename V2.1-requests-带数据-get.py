import requests

url = 'http://httpbin.org/get'

response = requests.get(url, data = {'name':'刘', 'age':20})

print(response.text)