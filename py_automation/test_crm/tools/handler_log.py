"""
====================
Author: 张崽崽
Time  : 2021/9/14 15:54
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import loguru
from tools.handler_path import log_file

# 获取文件的绝对路径
log_path = log_file("mylog.log")
print(log_path)

logger = loguru.logger
logger.add(log_path, encoding='utf-8')



if __name__ == '__main__':
    logger.info("1111111111")
    logger.error('报错了！！！赶紧看看什么情况！！')
    pass