# urllib 是python自带库
import urllib
from urllib import request

url = 'http://www.baidu.com/'

response = urllib.request.urlopen(url)
# decode设置编码格式
text = response.read().decode('utf-8')
#print(text)
with open(r'C:\Users\ASUS PC\Desktop\my.html', mode='w', encoding='utf-8') as f:
    f.write(text)