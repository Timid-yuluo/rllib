import re
import requests

#第一个页面为url1，第二页面为url2,则不能通过简单的字符串拼接，解决多页面问题
# url1 = 'http://sc.chinaz.com/tupian/dongman.html'
# url2 = 'http://sc.chinaz.com/tupian/dongman_2.html'
flag = False
count = 1
num = 0

def picture():
    #将num置为全局变量，解决num重复计数问题
    global num
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    # print(data)

    res = re.compile(r'<img src2="(.*?)"')
    srcs = re.findall(res,data)
    # print(srcs)

    #如果num放此处，每调用一次函数就会重新计数
    # num =0
    for src in srcs:
        #a为二进制数据
        a = requests.get(src)
        #print(a)
        #需要手动创建文件夹名为11，不然报错
        with open(r'C:\Users\ASUS PC\Desktop\11\%s.jpg'%num,mode = 'ab') as f:
            f.write(a.content)
        print('获取第%s张图片'%num)
        num += 1

# 解决第一个网址无规律，从第二个网址开始到最后存在规律问题
for i in range(14): # [0, 14)
    if flag:
        url = 'http://sc.chinaz.com/tupian/dongman_' + str(count)+  '.html'
        picture()
        count+= 1
    if not flag:
        url  = 'http://sc.chinaz.com/tupian/dongman.html'
        picture()
        flag = True
        count += 1

print('获取图片完成')
