import urllib
from urllib import request
from urllib import parse

# 网址和get时不一样
url = 'http://httpbin.org/post'

params = {'name':'刘', 'age':'20'}
# encode() 是编码 ，把str >>> bytes
params = urllib.parse.urlencode(params).encode()

response = urllib.request.urlopen(url=url, data=params)
print(response.read().decode())



#tip:抓包工具能看请求时传入的数据