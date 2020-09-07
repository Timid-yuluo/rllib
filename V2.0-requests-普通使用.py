import requests

url = 'https://movie.douban.com/top250'

# 伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
}

response = requests.get(url, headers = headers)
response.encoding = 'utf-8'

# 状态码 200 访问成功
print(response.status_code)
#打印数据文本
print(response.text)
print('------------------')
#二进制打印数据
print(response.content)