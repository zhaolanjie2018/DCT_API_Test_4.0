# import dryscrape
# # 使用dryscrape库 动态抓取页面
# def get_url_dynamic(url):
#     session_req=dryscrape.Session()
#     session_req.visit(url) #请求页面
#     response=session_req.body() #网页的文本
#     #print(response)
#     return response
# get_text_line(get_url_dynamic(url)) #将输出一条文本


def get_url_dynamic2(url):
    driver=webdriver.Firefox() #调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
    driver.get(url) #请求页面，会打开一个浏览器窗口
    html_text=driver.page_source
    driver.quit()
    #print html_text
    return html_text
get_text_line(get_url_dynamic2(url)) #将输出一条文本