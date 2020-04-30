import requests as re
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                         '78.0.3904.108 Safari/537.36'}
base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'


for page in range(0, 9):
    print('==========正在爬取' + '第' + str(page) + '的数据')
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': str(page),
        'pageSize': '10'
    }
    """注意所有字典的逗号间隔"""
    response = re.post(base_url, headers=headers, data=data)
    json_data = response.json()
    data_list = json_data['Table1']
    for li in data_list:
        storeName = li['storeName']
        addressDetail = li['addressDetail']
        ctiyName = li['cityName']
        pro = li['pro']
        print("正在爬取" + storeName)
        with open('data.csv', mode='a', newline='') as csvfile:
            """newline 新行写一下行""" """注意程序的缩进"""
            #   文件分隔符号
            csvwriter = csv.writer(csvfile, delimiter=',')
            #  序列化写入顺序
            csvwriter.writerow([storeName, ctiyName, addressDetail, pro])
