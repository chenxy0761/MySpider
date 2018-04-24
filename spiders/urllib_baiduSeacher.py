# -*- coding:utf-8 -*-
import urllib.request

url = "http://www.baidu.com/s?wd="
key = "阿特兹"
key_code = urllib.request.quote(key)
url_get = url+key_code
# print(url_get)
req = urllib.request.Request(url_get)
data = urllib.request.urlopen(req).read()
fh = open("D:\\tts9\\MySpider\\data\\atezi2.html","wb")
fh.write(data)
fh.close()
