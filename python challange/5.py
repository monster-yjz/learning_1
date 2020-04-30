
import pickle   # python 的一个编码库，用于编码
from urllib.request import urlopen

text = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

# print(text)

for line in text:

    print("".join([k*v for k, v in line]))
