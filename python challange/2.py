# http://www.pythonchallenge.com/pc/def/ocr.html
from os.path import join

import requests
# from collections import Counter

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
r = requests.get(url).text
final_text = r.split("<!--")[2][:-3]
# 用了比较蠢的方法，用“<!--"当做分隔符，[:-3]是为了清除最后的"-->"

# q = Counter(final_text)
# """统计成一个字典"""
# t = [i for i in q if q[i] == 1]

text = list(final_text)
message = ''

for i in text:
    if i.isalpha():
        message = message + i
    else:
        pass

print(message)

