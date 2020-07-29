import requests

url = "https://language.chinadaily.com.cn/"
html = requests.get(url).text
print(html)
str = input("请输入要查找的字符串：")
if str in html:
    print("你找到了字符串：{}".format(str))
else:
    print("你要找的字符串没有出现在该网站！")
