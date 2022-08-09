import datetime
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pywinauto
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class base_selenium:
    def __init__(self, driver):
        self.driver = driver

    # 打开指定页面
    def Open_Url(self, url):
        if self.driver:
            if "http://" in url:
                self.driver.get(url)
            else:
                print("url格式错误")
        else:
            print("LOG：打开浏览器失败")
        time.sleep(3)

    # 等待页面元素可见
    def wait_eleVisible(self, loc, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(loc))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            print('等待页面元素显示，共耗时：' + str(wait_time))
            # logger.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except:
            # logger.info('{0},等待页面元素:{1} 失败！！！'.format(doc, locator))
            # self.save_pictuer(doc)
            print("页面显示元素失败")

    # 获取页面元素
    def local_element(self, loc, doc=''):
        element = None
        try:
            self.wait_eleVisible(loc, doc)
            element = self.driver.find_element(*loc)
            return element
        except:
            print("获取页面元素失败")

    # input输入
    def input_value(self, loc, value):
        self.local_element(loc).send_keys(value)

    # 点击事件
    def click_event(self, loc):
        self.local_element(loc).click()

    # 下拉框选择定位
    def select_value(self, loc, value):
        select_element = self.local_element(loc)
        Select(select_element).select_by_visible_text(value)

    # 非input标签上传
    # input标签上传直接使用send_keys
    # path 路径使用 / or \\
    def upload_value(self, path):
        app = pywinauto.Desktop()
        win = app["打开"]
        win['Edit'].type_keys(path)
        win['Button'].click()

    # iframe切换
    def switch_to_iframe(self, loc):
        self.driver.switch_to.frame(self.local_element(loc))

    # 切出iframe
    def back_iframe(self):
        self.driver.switch_to.default_content()

    # 移动鼠标到指定位置
    def mouse_moveto_element(self, loc):
        element = self.local_element(loc)
        ActionChains(self.driver).move_to_element(element).perform()

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
            time.sleep(3)

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



