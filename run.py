import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s', './Test_cases/test_case01.py', '--alluredir', './allure-results'])
    os.system('allure generate ./allure-results -o ./Reports')
