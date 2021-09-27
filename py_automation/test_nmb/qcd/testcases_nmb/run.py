"""
====================
Author: 张崽崽
Time  : 2021/9/26 14:45
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest
import os
from unittestreport import TestRunner

# 获取用例执行模块的文件夹绝对路径
file_path = os.path.dirname(os.path.abspath(__file__))

# 通过用例套件文件夹搜集所有用例
cases_suite = unittest.defaultTestLoader.discover(file_path)

runner = TestRunner(cases_suite)

if __name__ == '__main__':
    runner.run()