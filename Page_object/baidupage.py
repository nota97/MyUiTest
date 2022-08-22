import time

from Base.base_selenium import base_selenium
from selenium.webdriver.common.by import By
from selenium import webdriver


class baidupage(base_selenium):
    url = "http://www.baidu.com"
    search_value = (By.ID, 'kw')
    search_button = (By.ID, 'su')
    login_link_button = (By.XPATH, '//*[@id="s-top-loginbtn"]')
    login_name = (By.NAME, 'userName')
    password = (By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]')
    login_button = (By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]')

    def baidusearch(self, value):
        self.Open_Url(self.url)
        self.input_value(self.search_value, value)
        self.click_event(self.search_button)
        time.sleep(1)
        # 可添加return值用于断言

    def baidulogin(self, login_name, password):
        self.Open_Url(self.url)
        self.click_event(self.login_link_button)
        self.input_value(self.login_name, login_name)
        self.input_value(self.password, password)
        self.click_event(self.login_button)
        time.sleep(10)


if __name__ == '__main__':
    driver = webdriver.Edge()
    txt = '抖音'
    a = baidupage(driver)
    a.baidusearch(txt)
