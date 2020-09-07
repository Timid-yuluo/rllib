import requests as req  # 导入requests模块，并定义为req 下次使用requests模块时可直接简写成req
from bs4 import BeautifulSoup

# 原链接是 url = 'https://movie.douban.com/top250'，但发现翻到第二页会多出'?start=25&filter='，把25改成0是第一页，
# 就是每页都加25，才会有后面的V1.2操作
url = 'https://movie.douban.com/top250?start=0&filter='
# 设置 请求头，攻破简单的反爬
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
}
response = req.get(url, headers = headers)
print(response)  # 打印响应情况，判断服务器是否响应 （200 代表响应）
html = response.text  # 把响应的文本内容（就是HTML内容）赋值给 html （可是任意符号）

# 用 parser 的方式解析 html 的内容 【parser可解析HTLM的内容，lxml 可解析 HTML 和 mxl 的内容】
soup = BeautifulSoup(html,'html.parser')
movies_list = soup.find('ol', class_='grid_view')  # class 是 ol 的属性 ,因区别关键字写成 class_
# print(movies_list)

movies = movies_list.find_all('li') # movies 是一个列表，这里的 li 没有属性
#print(movies)

names = []
for movie in movies:
    name = movie.find('span', class_='title').get_text() # ol li span 都是标签 取决于浏览器的标签名
    names.append(name)

# 储存数据
with open(r'C:\Users\ASUS PC\Desktop\my.txt','w') as f:
    for name in names:
        f.write(name + '\n')