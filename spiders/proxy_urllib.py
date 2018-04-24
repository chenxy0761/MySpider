# -*- coding:utf-8 -*-
import urllib.request

def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = "119.115.235.131:8118"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))