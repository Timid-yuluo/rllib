import urllib
from urllib import request

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
}
#构建请求头
request1 = request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request1)
print(response.read().decode())
