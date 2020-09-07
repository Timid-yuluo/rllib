import requests
from lxml import etree

#第一个页面为url1（里面没有数字1），第二个页面为url，有数字2，第三个，3， 第四个，4...........
#除了第一个网址外，第n个网址，则有数字n，则可把n设为%d
#url = 'http://xiaohua.zol.com.cn/lengxiaohua/2.html'
url1 = 'http://xiaohua.zol.com.cn/lengxiaohua/'
url2 = 'http://xiaohua.zol.com.cn/lengxiaohua/%d.html'

# [1,100) 当i为1，网址为url1，i为2,3...时，%d为2,3.....
for i in range(1,101):
    if i == 1:
        url = url1
    else:
        url = url2%(i)

    response = requests.get(url)
    response.encoding='gbk'
    data = response.text
    #print(data)

    #把data转化为HTML对象，变量名为html(可任意取)
    html = etree.HTML(data)

    #tostring可以把传入的数据，HTML标准化
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

    #获取ul标签中所有的li标签，得到的lis是一个列表
    lis = html.xpath('//ul[@class="article-list"]/li')

    for li in lis:
        #获取li标签中的span标签的子标签a的文本内容，li.xpath(...)得到的是列表，[0]表示取第一个元素
        title = li.xpath('./span/a/text()')[0]
        # print(title)

        #每个li标签中都有一个div class="summary-text"标签（简称div）.而div标签中又有很多p标签
        #获取li中的div中的所有p
        contens = li.xpath('./div[@class="summary-text"]/p/text()')

        results = []
        for conten in contens:
            #strip()去掉所有无效字符（空格），strip('\n')去掉回车
            results.append(conten.strip().strip('\n'))

        # print(title, results)

        with open(r'C:\Users\ASUS PC\Desktop\222.txt',mode ='a') as f:
            #先写标题，回车
            f.write(str(title) + '\n')
            #在写results的每个元素，写完每个元素回一次车
            for result in results:
                f.write(str(result) + '\n')
            #写完results的元素再回车
            f.write('\n')
    #第i次循环完成
    print('第%d页获取成功'%(i))
print('全部获取成功')
