import requests
import json
import jsonpath

# 找到接口网址，对其规律进行分析
# url = 'https://www.xfz.cn/api/website/articles/?p=1&n=20&type='
urln = 'https://www.xfz.cn/api/website/articles/?p=%d&n=20&type='

# 实测网页数据只有37页，往后为空
for i in range(1, 38):
    url = urln % i
    response = requests.get(url)
    data = response.text
    # print(data)

    f = open(r'C:\Users\ASUS PC\Desktop\news.txt', mode='a', encoding='utf-8')
    if response.status_code == 200:
        json_obj = json.loads(data, encoding='utf-8')
        # print(json_obj)

        titles = jsonpath.jsonpath(json_obj, '$..[title]')
        author_ids = jsonpath.jsonpath(json_obj, '$..[author_id]')
        names = jsonpath.jsonpath(json_obj, '$..[name]')
        # print(titles)
        # print(author_ids)
        # print(names)

        try:
            # 数据 = titles + author_ids + names  【三个列表的长度一致】
            for j in range(len(titles)):
                f.write(str(author_ids[j]) + names[j] + '\n' + titles[j] + '\n' + '\n')
        except Exception as result:
            print('page%d获取错误' % i, 'because: ', result)
            continue
    else:
        print('访问服务器失败')
    print('page%d' % i)
f.close()

'''
tip: try中for循环模型

a,b 列表长度一致
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
for i in range(len(a)):
    print(a[i],b[i])

1 1
2 2
3 3
4 4
5 5
6 6
'''