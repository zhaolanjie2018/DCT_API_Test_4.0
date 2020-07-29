#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 15:11
# @Author  : yuantup
# @Site    :
# @File    : jdshouji_image.py
# @Software: PyCharm

import urllib.request
import re
import os


def open_url(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/5'
                          '37.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    # print(response.getcode())
    html = response.read()
    return html


def get_img_addr(html):
    html_str = html.decode('utf-8')
    # print(html_str)
    img_addrs =[]
    pattern1 = '<img width="220" height="220" data-img="1" src="(.+?[.jpg|.png])"'
    pattern2 = '<img width="220" height="220" data-img="1" data-lazy-img="done"  title=.+? src="(.+?[.jpg|.png])"'
    pattern2 = '<img width="220" height="220" data-img="1" data-lazy-img="(.+?[.jpg|.png])"'
    img_addrs1 = re.compile(pattern1).findall(html_str)
    # print(img_addrs)
    img_addrs2 = re.compile(pattern2).findall(html_str)
    # print(len(img_addrs))
    img_addrs.extend(img_addrs1)
    img_addrs.extend(img_addrs2)
    print(img_addrs)
    return img_addrs


def save_img(img_addrs):
    i = 0
    for each in img_addrs:
        i = i+1
        img_name = each.split("/")[-1]
        with open(img_name, 'wb') as f:
            correct_url = 'http:' + each
            img = open_url(correct_url)
            f.write(img)
    return i


def main():
    path = 'D:\spiser_sons\shouji_img'
    a = os.getcwd()
    print(a)
    if os.path.exists(path):
        os.chdir(path)
        print(os.getcwd())
    else:
        os.mkdir(path)
    # os.chdir(path)

    for i in range(1, 11):
        url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
        html = open_url(url)
        img_addrs = get_img_addr(html)
        print(url)
        save_img(img_addrs)


if __name__ == '__main__':
    main()