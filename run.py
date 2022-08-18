import pytest
import os
import time


if __name__ == '__main__':
    pytest.main(['-s', './Test_cases/test_case01.py', '--alluredir', './Output/Reports/allure-results'])
    os.system('allure generate ./Output/Reports/allure-results -o'
              ' ./Output/Reports/report_{0}'.format(time.strftime('%Y-%m-%d')))
