import requests as req
from bs4 import BeautifulSoup
import pandas
url = 'http://tianqihoubao.com/aqi/beijing-201812.html'
response = req.get(url)

if response.status_code == 200:
    print('访问成功')
else:
    print('访问失败')

html = response.text
soup = BeautifulSoup(html,'lxml')
table = soup.find('table',class_='b')

# prettify()美化的作用
df=pandas.read_html(table.prettify(),header=0) # 得到一个列表
print(df[0])

#保存数据，.csv保存的是excel表格，.txt是文档，'a'是指用a的方式写文件
df[0].to_csv(r'C:\Users\ASUS PC\Desktop\result.csv',header=None,encoding='utf-8-sig',mode='a')