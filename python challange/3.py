"""http://www.pythonchallenge.com/pc/def/equality.html"""
import re
import requests

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
r = requests.get(url).text
final_text = r.split("<!--", 2)
# 用了比较蠢的方法，用“<!--"当做分隔符，[:-3]是为了清除最后的"-->"

# 正则表达式的构建 [范围]{次数} r加“字符”

a = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', final_text[1])

# ans = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", final_text[1]))
# message = re.search(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', final_text[1])
print(a)

