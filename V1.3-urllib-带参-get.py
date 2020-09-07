import urllib
from urllib import request
from urllib import parse

#  该网址能测试get和post请求
url = 'http://httpbin.org/get?%s'

params = {'name':'刘', 'age':20}
# urlencode()函数把传入的参数对，转化为标准的url格式
params = urllib.parse.urlencode(params)
# get请求，请求内容都是在网址暴露的
response = urllib.request.urlopen(url=url%(params))
print(response.read().decode())



# tip:用Charles抓包工具可以看到，传入的数据
