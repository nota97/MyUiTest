import time

import pytest
from selenium import webdriver
from Page_object.baidupage import baidupage
from Config.yamlload import yamlload


class TestBaidu:
    def setup_class(cls) -> None:
        print("~~~~~~~~~~测试开始执行~~~~~~~~~~")
        cls.driver = webdriver.Edge()
        cls.bd = baidupage(cls.driver)

    def teardown_class(cls) -> None:
        print("~~~~~~~~~~测试结束执行~~~~~~~~~~")
        time.sleep(3)
        cls.driver.close()

    @pytest.mark.parametrize('value', yamlload('./Data/search.yaml'))
    def test_01_search(self, value):
        self.bd.baidusearch(value['searchname'])


if __name__ == '__main__':
    pytest.main()




