import logging
import os
import time


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(BASE_DIR, 'Output/log/').replace('/', '\\')


class Log:
    def __init__(self, log_save_path):
        self.log_name = os.path.join(log_save_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def _print_console(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.log_name, 'a+', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self._print_console('debug', message)

    def info(self, message):
        self._print_console('info', message)

    def warning(self, message):
        self._print_console('warning', message)

    def error(self, message):
        self._print_console('error', message)


if __name__ == '__main__':
    Log(log_path).info("fjdaflkasjflkasjfklasjflkasfj")