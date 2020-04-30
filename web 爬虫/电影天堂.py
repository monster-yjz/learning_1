import requests
import parsel

url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

response = requests.get(url=url, headers=headers)
#  忽略错误参数的结果，减少报错
html_base = response.content.decode(encoding='gbk', errors='ignore')
html = parsel.Selector(html_base)
text_base = html.xpath('//div[@class="bd3r"]//ul//tr/td/b/a/@href').extract()

for text in text_base:
    html_ues = 'https://www.dytt8.net' + text
    html_movie = requests.get(url=html_ues, headers=headers).content.decode(encoding='gbk', errors='ignore')
    html_movie_base = parsel.Selector(html_movie)

    html_movie_text = html_movie_base.xpath('//div[@class="title_all"]//hl/font[@color="#07519a"]')
    print(html_movie_text)
