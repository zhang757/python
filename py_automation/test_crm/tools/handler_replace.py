"""
====================
Author: 张崽崽
Time  : 2021/9/28 16:55
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import re
import json
from tools.handler_global import *
from tools.handler_log import logger


def variable_replace(case:dict):
    # 把字符串数据转换成json类型，python中为字典类型：两者的区别在：单双引号
    case_json_str = json.dumps(case)
    logger.info(f"case数据类型：{type(case)}")
    logger.info(f"case数据转换后的类型：{type(case_json_str)}")

    # 第一步：用正则一次获取该条用例中要替换的所有数据变量，获取出来的数据是列表类型
    re_data = re.findall("#(\w+)#", case_json_str)
    logger.info(f"正则获取变量列表：\n{re_data}")

    # 第二步：遍历正则获取的列表数据
    for variable_key in re_data:
        # 第三步：通过判断全局变量类中是否有对应变量来进行值的替换
        if hasattr(Global, variable_key):
            # 注意点：replace()函数是针对字符串，字符串类型是不可变类型，但是想要整条数据被替换，就需要用同样的变量名来接受与继续反馈，否则替换失败！！
            case_json_str = case_json_str.replace(f"#{variable_key}#", getattr(Global, variable_key))
        else:
            logger.warning(f"全局变量类中没有{variable_key}变量数据！！！")

        """以下注释部分，为示例样板，有其他全局变量类，可按照下方书写"""
        # elif hasattr(Data, variable_key):
        #     # 注意点：replace()函数是针对字符串，字符串类型是不可变类型，但是想要整条数据被替换，就需要用同样的变量名来接受与继续反馈，否则替换失败！！
        #     case_json_str = case_json_str.replace(f"#{variable_key}#", getattr(Data, variable_key))
        #
        # elif hasattr(User, variable_key):
        #     case_json_str = case_json_str.replace(f"#{variable_key}#", getattr(User, variable_key))
        #
        # elif hasattr(Pwd, variable_key):
        #     case_json_str = case_json_str.replace(f"#{variable_key}#", getattr(Pwd, variable_key))

    logger.info(f"用例中所有变量替换后最终显示数据：\n{json.loads(case_json_str)}")
    return json.loads(case_json_str)


if __name__ == '__main__':
    case = {
        "phone":"#phone#",
        "password":"#password#",
        "pwd":"#pwd#"
    }

    print(variable_replace(case))