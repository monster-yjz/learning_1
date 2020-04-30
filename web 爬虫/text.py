import requests
import parsel
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
html_ues = 'https://www.dytt8.net/html/gndy/dyzz/20200507/60012.html'


#  href = "(.*?)" >


html_movie = requests.get(url=html_ues, headers=headers).content.decode(encoding='gbk', errors='ignore')
html_movie_base = str(html_movie)

html_movie_text = re.search(r'[#7519a>(.*?)</font]', html_movie_base)

print(html_movie_text)
