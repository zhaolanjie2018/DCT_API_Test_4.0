# import requests
#
# from bs4 import BeautifulSoup
#
# import re
#
# from selenium import webdriver
#
# import time
#
#
# def getHTMLText(url):
#     driver = webdriver.PhantomJS(executable_path='C:\\Users\\Z\\Downloads\\phantomjs-2.1.1-windows (2)\\phantomjs-2.1.1-windows\\bin\\phantomjs')  # phantomjs的绝对路径
#
#     time.sleep(2)
#
#     driver.get(url)  # 获取网页
#
#     time.sleep(2)
#
#     return driver.page_source
#
#
# def fillUnivlist(html):
#     soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
#
#     tag = soup.find_all('div', attrs={'class': 'listInfo'})
#
#     print(str(tag[0]))
#
#     return 0
#
#
# def main():
#     url = 'https://language.chinadaily.com.cn/'  # 要访问的网址
#
#     html = getHTMLText(url)  # 获取HTML
#
#     fillUnivlist(html)
#
#
# if __name__ == '__main__':
#     main()
#
#
# import requests
# import json
# url = 'https://language.chinadaily.com.cn/'
# wbdata = requests.get(url).text
#
# data = json.loads(wbdata)
# news = data['data']['pc_feed_focus']
# for n in news:
#     title = n['title']
#     img_url = n['image_url']
#     url = n['media_url']
#     print(url,title,img_url)
#
#

import requests, random
from ulits import config

url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2020-01-13&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CQW&purpose_codes=ADULT'

headers = {
    'User-Agent': random.choice(config.USER_AGENT_POOL),
    'Cookie': 'JSESSIONID=B709F9775E72BDED99B2EEBB8CA7FBB9; BIGipServerotn=1910046986.24610.0000; RAIL_EXPIRATION=1579188884851; RAIL_DEVIC'
}

res = requests.get(url=url, headers=headers)
res_info = res.json()
print(res_info)
