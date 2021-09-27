"""
====================
Author: 张崽崽
Time  : 2021/9/17 12:03
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest
import os
from unittestreport import TestRunner
from tools.handler_path import parent_dir

# 获取执行用例的文件夹绝对路径
dir_path = os.path.join(parent_dir, "tools_crm")

# 通过执行用例文件夹绝对路径收集所有测试用例
a = unittest.defaultTestLoader.discover(dir_path)
b = TestRunner(a)


if __name__ == '__main__':
    b.run()