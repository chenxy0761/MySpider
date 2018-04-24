# -*- coding:utf-8 -*-
import re

pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "Traceback (most recent call last)"
result = re.search(pattern, string,)
print(result)
for i in range(0,200):
    print(i)
