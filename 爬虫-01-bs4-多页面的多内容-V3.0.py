import requests as req
from bs4 import BeautifulSoup

a = 0

def acquire():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
    }
    response = req.get(url, headers = headers)
    #print(response)
    html = response.text


    soup = BeautifulSoup(html,'html.parser')
    movies_list = soup.find('ol', class_='grid_view')
    #print(movies_list)
    movies = movies_list.find_all('li')
    #print(movies)

    movies_dict = {}
    result = []
    for movie in movies:
        name = movie.find('span', class_='title').get_text()
        net = movie.find('a')['href']
        movies_dict = {'name':name, 'url':net}    # movies_dict[name] = net
        result.append(movies_dict)

    with open(r'C:\Users\ASUS PC\Desktop\my.txt','a') as f:
        for single in result:
            f.write(single['name'] + '  :  ' + single['url'] + '\n')

for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(a) +'&filter='
    acquire()
    a += 25
print('爬取成功')
