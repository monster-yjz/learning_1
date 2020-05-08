import parsel
import requests


for j in range(1, 7):
    print('正在下载第' + str(j) + '页的数据')
    base_url = 'http://www.win4000.com/mobile_2340_0_0_{}.html'.format(str(j))
    response = requests.get(url=base_url)
    html_data = response.text

    html = parsel.Selector(html_data)
    text_first = html.xpath('//div[@class="Left_bar"]//ul/li/a/@href').extract()

    for data in text_first:
        text_base = requests.get(data).text
        text_url = parsel.Selector(text_base)
        img_url = text_url.xpath('//div[@class="main"]//img/@src').extract_first()
        img_data = requests.get(img_url).content
        file_name = img_url.split('/')[-1]
        with open('img\\' + file_name, mode='wb') as file:
            file.write(img_data)
            print('正在保存' + file_name)
            print('保存成功')
