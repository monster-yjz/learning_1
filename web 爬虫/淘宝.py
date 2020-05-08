from selenium import webdriver
import time
import csv


def search_product(key):
    driver.find_element_by_id('q').send_keys(key)
    driver.find_element_by_class_name('btn-search').click()
    driver.maximize_window()
    time.sleep(15)


def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        price = div.find_element_by_xpath('.//strong').text + '元'
        per = div.find_element_by_xpath('.//div[@class ="deal-cnt"]').text
        name = div.find_element_by_xpath('.//div[@class ="shop"]/a').text
        print(info, price, per, name, sep='|')
        with open('data_taobao.csv', mode='a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([info, price, per, name])


def main():
    search_product(keyword)
    get_product()


if __name__ == '__main__':
    keyword = input('请输入你要搜索的关键字：')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    main()
