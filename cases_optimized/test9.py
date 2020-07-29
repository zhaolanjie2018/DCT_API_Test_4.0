import urllib
import urlparse
import HTMLParser
import re
r=urllib.urlopen(u"http://v.youku.com/v_show/id_XNjA4Mzg2MDg4.html")
content=r.fp.read()
#value
title=re.findall(r'<h1 class="title".+.</h1>',content)
s = re.findall(r'http://player.youku.com.*.swf',content)
print(title[0].decode('utf-8').encode('utf-8'))
print(s[0])

