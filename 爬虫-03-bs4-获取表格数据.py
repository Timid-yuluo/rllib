import requests as req
from bs4 import BeautifulSoup

url = 'http://tianqihoubao.com/aqi/beijing-201812.html'
response = req.get(url)

if response.status_code == 200:
    print('访问成功')
else:
    print('访问失败')

html = response.text
soup = BeautifulSoup(html,'lxml')
table = soup.find('table',class_='b')
print(table)
trs = table.find_all('tr')  # trs 列表
columns =''  #表头信息
datas =''    #表中数据

columns_names=trs[0].find_all('td')  # 观察得第一个tr存储的是表头

#表头信息单独获取
for name in columns_names:
    columns += name.get_text().strip()
    columns += ','

#获取除表头之外的信息
for tr in trs[1:]:    # trs是列表，遍历trs中的每个元素（tr）
    tds = tr.find_all('td')    # 每一个tr 里面都有很多td,获得td列表tds
    for td in tds:
        datas+=td.get_text().strip()
        datas+=','
    datas += '\n'    # 每遍历完一个tr里面的所有td，就回车换行
print(columns)
print(datas)