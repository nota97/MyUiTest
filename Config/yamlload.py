import yaml
import os
from Config.log_set import Log

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(BASE_DIR, 'Output/log/').replace('/', '\\')
logger = Log(log_path)


def yamlload(filename):
    files = open(filename, 'r', encoding='utf-8')
    try:
        data = yaml.load(files, Loader=yaml.FullLoader)
        logger.info('读取测试用例名称：{0}  数据数量：{1}'.format(filename, len(data)))
        return data
    except:
        logger.error('###测试数据读取失败 请检查格式###')
        raise


