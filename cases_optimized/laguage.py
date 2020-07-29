'''
import urllib.request


def getHtml(url):
    html = urllib.request.urlopen(url).read()

    return html
def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /

    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码

        f.write(file_content)
aurl = "https://language.chinadaily.com.cn/"

html = getHtml(aurl)

saveHtml("sduview", html)

print("下载成功")
'''


# 请求库
import requests
# 用于解决爬取的数据格式化
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 爬取的网页链接
r= requests.get("https://language.chinadaily.com.cn/")
# 类型
# print(type(r))
print(r.status_code)
# 中文显示
# r.encoding='utf-8'
r.encoding=None
print(r.encoding)
print(r.text)
result = r.text