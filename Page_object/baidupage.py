import time

from Base.base_selenium import base_selenium
from selenium.webdriver.common.by import By
from selenium import webdriver


class baidupage(base_selenium):
    url = "http://www.baidu.com"
    search_value = (By.ID, 'kw')
    search_button = (By.ID, 'su')

    def baidusearch(self, value):
        self.Open_Url(self.url)
        self.input_value(self.search_value, value)
        self.click_event(self.search_button)
        time.sleep(3)


if __name__ == '__main__':
    driver = webdriver.Edge()
    txt = '抖音'
    a = baidupage(driver)
    a.baidusearch(txt)
