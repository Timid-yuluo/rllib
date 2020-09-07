import re
import requests

url1 = 'http://sc.chinaz.com/tupian/dongman.html'
url2 = 'http://sc.chinaz.com/tupian/dongman_%d.html'

# 解决第一页面无规律，第二个以后有规律问题
num = 0
for i in range(1,15):
    if i == 1:
        url = url1
    else:
        url = url2%(i)

    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    # print(data)

    res = re.compile(r'<img src2="(.*?)"')
    srcs = re.findall(res,data)
    # print(srcs)


    for src in srcs:
        #a为二进制数据
        a = requests.get(src)
        #print(a)
        # 需要手动创建文件夹名为11，不然报错
        with open(r'C:\Users\ASUS PC\Desktop\11\%s.jpg'%num,mode = 'ab') as f:
            f.write(a.content)
        print('获取第%s张图片'%num)
        num += 1
print('获取图片完成')



