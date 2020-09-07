import requests
from lxml import etree
import os

url1 = 'http://sc.chinaz.com/tupian/dongman.html'
url2 = 'http://sc.chinaz.com/tupian/dongman_%d.html'
num = 0

for i in range(1, 2):
    if i == 1:
        url = url1
    else:
        url = url2%(i)
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        data = response.text
        html = etree.HTML(data)
        # print(etree.tostring(html, encoding = 'utf-8').decode('utf-8'))

        divs = html.xpath('//*[@id="container"]/div')
        # print(len(divs))
        for div in divs:
            # !!!找src找不到，必须去看HTML源码，ctrl+f,找src,发现不是想要的数据,留意 src**,或 **src
            picture = div.xpath('./div/a/img/@src2')[0]
            #print(picture)

            img = requests.get(picture).content

            #判断文件夹是否存在，不存在则创建，存在则写入数据
            path = r'C:\Users\ASUS PC\Desktop\img'
            dir = os.path.exists(path)
            if not dir:
                os.mkdir(path)
            else:
                with open(r'C:\Users\ASUS PC\Desktop\img\%s.jpg'%num, mode='ab') as f:
                    f.write(img)
                print('%d'%num)
                num += 1
    else:
        print('访问错误')