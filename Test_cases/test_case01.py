import time

import pytest
from selenium import webdriver
from Page_object.baidupage import baidupage
from Config.yamlload import yamlload
import os
from Config.log_set import Log


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(BASE_DIR, 'Output/log/').replace('/', '\\')
logger = Log(log_path)


class TestBaidu:
    def setup_class(cls) -> None:
        print("~~~~~~~~~~测试开始执行~~~~~~~~~~")
        logger.info('~~~~~~~~~~测试开始执行~~~~~~~~~~')
        # 多页面业务流使用一个driver串联
        cls.driver = webdriver.Edge()
        cls.bd = baidupage(cls.driver)

    def teardown_class(cls) -> None:
        print("~~~~~~~~~~测试结束执行~~~~~~~~~~")
        logger.info('~~~~~~~~~~测试结束执行~~~~~~~~~~')
        time.sleep(3)
        cls.driver.close()

    @pytest.mark.skip
    @pytest.mark.parametrize('value', yamlload('./Data/search.yaml'))
    def test_01_search(self, value):
        logger.info('执行测试用例数据：{0}'.format(value['searchname']))
        self.bd.baidusearch(value['searchname'])

    @pytest.mark.parametrize('login_value', yamlload('./Data/baidulogin.yaml'))
    def test_02_login(self, login_value):
        logger.info('执行测试用例数据：账号 {0}'.format(login_value['loginname']))
        self.bd.baidulogin(login_value['loginname'], login_value['password'])


if __name__ == '__main__':
    pytest.main()




