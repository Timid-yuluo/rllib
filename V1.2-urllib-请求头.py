import urllib
from urllib import request

url = 'https://movie.douban.com/top250'

request1 = request.Request(url)
#注意下面的请求头不是键值对
request1.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400')

response = urllib.request.urlopen(request1)
print(response.read().decode())