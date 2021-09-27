"""
====================
Author: 张崽崽
Time  : 2021/9/14 15:58
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import os

# 获取当前文件的目录
dir_name = os.path.dirname(os.path.abspath(__file__))

# 获取项目的父级目录
parent_dir= os.path.dirname(dir_name)

# 拼接获取配置文件，绝对路径
def conffiguration_file(filename: str):
    conf_path = os.path.join(parent_dir, 'conf')
    conf_file_path = os.path.join(conf_path, filename)
    return conf_file_path

# 拼接获取日志文件，绝对路径
def log_file(filename: str):
    log_path = os.path.join(parent_dir, 'log')
    log_file_path = os.path.join(log_path, filename)
    return log_file_path

# 拼接用例数据文件，绝对路径
def case_file(filename: str):
    log_path = os.path.join(parent_dir, 'cases_data')
    log_file_path = os.path.join(log_path, filename)
    return log_file_path


if __name__ == '__main__':
    # print(case_file("api_data.xlsx"))
    pass