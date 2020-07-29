import urllib
import bs4
import re
import os


# 获取当前页面子网站子网站
def get_urls(url, baseurl, urls):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        link = bs(data).find_all('a')
        for i in link:
            suffix = i.get('href')
            # 设置排除写入的子连接
            if suffix == '#' or suffix == '#carousel-example-generic' or 'javascript:void(0)' in suffix:
                continue
            else:
                # 构建urls
                childurl = baseurl + suffix
                if childurl not in urls:
                    urls.append(childurl)



# 获取整个网站URL
def getallUrl(url, baseurl, urls):
    get_urls(url, baseurl, urls)
    end = len(urls)
    start = 0
    while(True):
        if start == end:
            break
        for i in range(start, end):
            get_urls(urls[i], baseurl, urls)
            time.sleep(1)
        start = end
        end = len(urls)


    # 获取当前网页代码
    with request.urlopen(url) as f:
        html_source = f.read().decode()
        # css，js，img正则表达式，以获取文件相对路径
        patterncss = '<link rel="stylesheet" href="(.*?)"'
        patternjs = '<script src="(.*?)"'
        patternimg = '<img src="(.*?)"'
        titleStr = re.compile(pattertitil
        # 使用re模块通过正则规则获取相对路径
        cssHerf = re.compile(patterncss, re.S).findall(html_source)
        jsHref = re.compile(patternjs, re.S).findall(html_source)
        imgHref = re.compile(patternimg, re.S).findall(html_source)


        # 获取css文件名并选择本地保存路径（使用了正则）
        patternCssTitle = '(/?.*?.css?)'
        filename = path + '\\' + re.compile(patternCssTitle, re.S).findall(url)[1][1:]
        # 使用split方法
        filename = path + '\\' + href[i].split('/')[-1]
        # 获取js文件名并选择本地保存路径
        filename = path + '\\' + href[i].split('/')[-1]
        # 获取img文件名并选择本地保存路径
        filename = path + '\\' + href[i].split('/')[-1]
        # 保存html
        try:
            with open(filename, 'w') as f:
                f.write(html_source)
        except:
            print("文件无法保存，请检查参数配置")
            exit(1)

        # 保存CSS文件
        try:
            with request.urlopen(url) as w:
                css_source = w.read().decode()
                with open(filename, 'w') as f:
                    f.write(css_source)
                print(re.compile(patternCssTitle, re.S).findall(url)[1][1:] + " css文件保存成功！")
                time.sleep(1)
        except:
            print("该" + re.compile(patternCssTitle, re.S).findall(url)[1][1:] + " css文件无法下载")

        # 保存js文件
        try:
            with request.urlopen(url) as w:
                js_source = w.read().decode()
                with open(filename, 'w') as f:
                    f.write(js_source)
                print(href[i].split('/')[-1] + " js文件保存成功")
                time.sleep(1)
        except:
            print("该" + href[i].split('/')[-1] + " js文件无法下载")
            # 这里使用continue是因为遇到cdn的js文件报错没办法保存，直接跳过
            continue

        # 保存img文件
        try:
            with request.urlopen(url) as w:
                img_source = w.read()
                with open(filename, 'wb') as f:
                    f.write(img_source)
                print(href[i].split('/')[-1] + " 图像文件保存成功")
                time.sleep(1)
        except:
            print("该" + href[i].split('/')[-1] + " 图像无法下载")
