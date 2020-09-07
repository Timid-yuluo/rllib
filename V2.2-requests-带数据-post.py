import requests

url = 'http://httpbin.org/post'

response = requests.post(url, data = {'name':'刘', 'age':20})

print(response.text)