from selenium import webdriver
import time

# 启动浏览器，并访问网页
url = 'https://www.xfz.cn/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

# 打开路径下的文件，若没有则自动创建（该路径为本人电脑桌面路径，若有使用自行修改路径）
f = open(r'C:\Users\ASUS PC\Desktop\news.txt', mode='a', encoding='utf-8')
for i in range(1, 38):
    # 下拉窗口至最底部
    js = 'window.scrollTo(0,document.body.scrollHeight)'
    driver.execute_script(js)

    # !!!!!! elements 找很多标签加 s
    news = driver.find_elements_by_xpath('//*[@id="content"]/div[@class="list-container"]/ul/li')
    # print(news)

    # 捕获异常
    try:
        # 获取数据
        for new in news:
            title = new.find_element_by_xpath('./a/div[2]/div[1]').text
            author = new.find_element_by_xpath('./a/div[2]/div[3]/span[3]').text
            # get_attribute获取标签内某个属性
            num = new.find_element_by_xpath('./a/div[2]/div[3]/span[3]/i').get_attribute('data-id')
            # print(num)
            # print(author)
            # print(title)
            # 写入数据
            f.write(num + ': ' + author + '\n' + title + '\n' + '\n')
    except Exception as result:
        print(result)
        continue

    # 翻页
    next_page = driver.find_element_by_xpath('//*[@id="newsList"]/div[3]')
    next_page.click()
    print('page%d' % i)
    # time.sleep(2)

driver.close()
f.close()