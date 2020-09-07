import re
import requests

url = 'http://sc.chinaz.com/tupian/dongman.html'

response = requests.get(url)
response.encoding = 'utf-8'
data = response.text
# print(data)

#compile设置正则表达式
#  <img src2="(.*?)"  表示获取 <img src2= 里面的内容
res = re.compile(r'<img src2="(.*?)"')
srcs = re.findall(res,data)
# print(srcs)

num = 0
for src in srcs:
    #a为二进制数据
    a = requests.get(src)
    #print(a)
    with open(r'C:\Users\ASUS PC\Desktop\11\%s.jpg'%num,mode = 'ab') as f:
        f.write(a.content)
    print('获取第%s张图片'%num)
    num += 1
print('获取图片完成')


'''tip:该网址很怪，通过浏览器的检查功能点击一张图片,会调到src标签，但通过正则匹配str会匹配不到元素
        可以通过 response = requests.get(url)
                response.encoding = 'utf-8'
                data = response.text
                print(data)
        打印网页的文本内容，在文本内容中，ctrl + f 查询 src ,这时发现没有src内容，但有src2，且str2
        标签内容正是图片链接地址，在程序中用正则匹配str2，可以获得图片。
        当使用正则，直接匹配浏览器标签，得不到内容，可使用该方法。
'''

