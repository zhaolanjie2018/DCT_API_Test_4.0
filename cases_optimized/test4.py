# 判断网页中是否含有指定文字
import urllib.request
url = 'https://language.chinadaily.com.cn/'
test = urllib.request.urlopen(url).read()
print(test)
if '中文' in test.decode():
    print("1包含指定文字。")
else:
    print("2不包含指定文字。")