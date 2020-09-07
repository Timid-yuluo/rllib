import requests as req
from bs4 import BeautifulSoup

a = 0

for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(a) +'&filter='
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
    }
    response = req.get(url, headers = headers)
    print(response)
    html = response.text


    soup = BeautifulSoup(html,'html.parser')
    movies_list = soup.find('ol', class_='grid_view')
    #print(movies_list)
    movies = movies_list.find_all('li')
    #print(movies)

    names = []
    for movie in movies:
        name = movie.find('span', class_='title').get_text()
        names.append(name)

    with open(r'C:\Users\ASUS PC\Desktop\my.txt','a') as f:
        for name in names:
            f.write(name + '\n')
    a += 25
    print(url)


# TIP：注意下段代码的使用
'''
a = 0
for i in range(6):
    str1 = 'abc' + str(a) + 'cde'
    a += 25
    print(str1)
'''