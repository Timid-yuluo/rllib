import urllib
from urllib import request

url = 'http://httpbin.org/ip'

#不使用代理ip
response = urllib.request.urlopen(url=url)
print('ip:',response.read().decode())

#使用代理IP,网址西刺代理,tip:代理ip，有HTTP和HTTPS，且端口前有 ：符号
#构建代理
ph = urllib.request.ProxyHandler({'http':'222.95.240.191:3000'})
opener = urllib.request.build_opener(ph)

#代理打开网址
response = opener.open(url)
print('代理ip:',response.read().decode())



#tip：显示与计算机请求失败，一般是代理IP问题，
# 有些反爬会封IP，所以需要代理IP。