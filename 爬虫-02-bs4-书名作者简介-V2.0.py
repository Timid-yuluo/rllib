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
            # 当数据为None或[] 时，无法get_text(),会报错，可以用try过滤

            # try里面发生异常则执行except里面代码，没有异常则执行else里面代码
            try:
                author  = book.find('p').find('a').get_text()
            except Exception:
                continue
            else:
                author = book.find('p').find('a').get_text()
            note = book.select('p[class="disc eps"]')[0].string  #[0].get_text()
            f.write(title + '   ' + author + '\n' + note + '\n' + '\n')
        print('第%d个页面写入成功'%i)
    else:
        print('访问服务器失败')
f.close()
print('获取成功')