import requests
from bs4 import BeautifulSoup

# url = 'https://www.dushu.com/guoxue/1001_1_1.html'

urln = 'https://www.dushu.com/guoxue/1001_1_%d.html'

# 先打开文件，在for循环中写入数据，循环结束关闭文件
f = open(r'C:\Users\ASUS PC\Desktop\my.txt', mode = 'a', encoding = 'utf-8')
for i in range(1,34):
    url = urln%(i)

    response = requests.get(url)
    data = response.text

    if response.status_code == 200:
        soup = BeautifulSoup(data, 'lxml')
        book_list = soup.find('div', class_="bookslist")
        # print(book_list)
        books = book_list.find_all('li')
        # print(books)

        for book in books:
            title = book.find('h3').find('a').get_text()
            # print(title)

            #有些页面的作者不存在数据（ find得到None，select得到[] ）
            #得到[]
            # author = book.select('div[class="book-info"] > p > a')
            #得到None
            # author = = book.find('p').find('a')
            # 当数据为None或[] 时，无法get_text(),会报错，可以用if过滤
            person = book.find('p').find('a')
            if person == None:
                continue
            else:
                author = person.get_text()
            note = book.select('p[class="disc eps"]')[0].string  #[0].get_text()
            f.write(title + '   ' + author + '\n' + note + '\n' + '\n')
        print('第%d个页面写入成功'%i)
    else:
        print('访问服务器失败')
f.close()
print('获取成功')

#'''当获取数据的某些属性报错时，可以先不获取数据的属性，用print把数据打印出来分析
#'''因为数据本身可能是None或[]之类的空数据，取空数据的属性（如get_text）就会报错