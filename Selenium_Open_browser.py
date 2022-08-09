from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SeleniumDriver:
    def __init__(self, browser):
        self.driver = self.Open_Browser(browser)

    def Open_Browser(self, browser):
        try:
            if browser == "Edge":
                driver = webdriver.Edge()
            return driver
        except:
            print("LOG：打开浏览器失败")
            return None

    def Open_Url(self, url):
        if self.driver:
            if "http://" in url:
                self.driver.get(url)
            else:
                print("url格式错误")
        else:
            print("LOG：打开浏览器失败")
        time.sleep(3)

    def handle_windows(self, *args):
        if self.driver:
            if len(args) == 1:
                if args[0] == "max":
                    self.driver.maximize_window()
                elif args[0] == "min":
                    self.driver.minimize_window()
                elif args[0] == "forward":
                    self.driver.forward()
                elif args[0] == "back":
                    self.driver.back()
                elif args[0] == "fresh":
                    self.driver.refresh()
                else:
                    print("无匹配动作")
            elif len(args) == 2:
                self.driver.set_window_size(args[0], args[1])
            else:
                print("参数有误")
            time.sleep(5)

    def assert_title(self, title=None):
        get_title = EC.title_is(title)
        return get_title(self.driver)

    def Open_url_is_True(self, url, title=None):
        self.Open_Url(url)
        result = self.assert_title(title)
        if result:
            print("页面正确")
        else:
            print("页面错误")

    def Switch_windows(self, title=None):
        handle_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        print(handle_list)
        for i in handle_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)
                time.sleep(1)
                if self.assert_title(title):
                    break
            else:
                if self.assert_title(title):
                    break
        time.sleep(2)
        # self.driver.find_element(By.ID, 'kw').send_keys('hello')

    def get_element(self, key, value):
        element = None
        if key == 'id':
            element = self.driver.find_element(By.ID, value)
        elif key == 'name':
            element = self.driver.find_element(By.NAME,value)
        elif key == 'class':
            element = self.driver.find_element(By.CLASS_NAME, value)
        elif key == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, value)
        else:
            element = self.driver.find_element(By.XPATH, value)
        return element

    def get_elements(self, key, value):
        elements = None
        if key == 'id':
            elements = self.driver.find_elements(By.ID, value)
        elif key == 'name':
            elements = self.driver.find_elements(By.NAME, value)
        elif key == 'class':
            elements = self.driver.find_elements(By.CLASS_NAME, value)
        elif key == 'css':
            elements = self.driver.find_elements(By.CSS_SELECTOR, value)
        else:
            elements = self.driver.find_elements(By.XPATH, value)
        return elements

    def get_level_elements(self, key, value, node_key, node_value):
        # 层级获取元素定位
        element = None
        element = self.get_element(key, value)
        if node_key == 'id':
            element = element.find_element(By.ID, node_value)
        elif node_key == 'name':
            element = element.find_element(By.NAME, node_value)
        elif node_key == 'class':
            element = element.find_element(By.CLASS_NAME, node_value)
        elif node_key == 'css':
            element = element.find_element(By.CSS_SELECTOR, node_value)
        else:
            element = element.find_element(By.XPATH, node_value)
        return element

    def get_list_element(self, key, value, index):
        # list元素定位
        element = None
        element = self.get_elements(key, value)
        if len(element) > index:
            return None
        return element[index]

    def check_box_isselected(self, key, value, check=None):
        element = self.get_element(key, value)
        flag = element.is_selected()
        if flag:
            if check != 'check':
                element.click()
        else:
            if check == 'check':
                element.click()


    def Close_driver(self):
        # self.driver.quit()
        self.driver.close()


#css 定位 标签（input）     id（#）     class(.)
sdriver = SeleniumDriver("Edge")
sdriver.Open_url_is_True("http://www.baidu.com", "百度一下，你就知道")
time.sleep(10)
sdriver.Switch_windows('百度一下，你就知道')
time.sleep(10)
sdriver.Close_driver()
