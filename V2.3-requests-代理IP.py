import requests

url = 'http://httpbin.org/get'

# 设置响应时间为2s，2s内没响应跳出
# 普通IP
response = requests.get(url, proxies = {'http':'183.166.96.49:9999'}, timeout = 2)
print(response.text)

#独享IP，需要设置账号（如：ABC）和密码（如：123）
# response = requests.get(url, proxies = {'http':'http://ABC:123@183.166.96.49:9999'}, timeout = 2)