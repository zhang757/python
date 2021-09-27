"""
====================
Author: 张崽崽
Time  : 2021/9/26 17:30
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
from jsonpath import jsonpath
from tools.handler_log import logger
from tools.handler_global import Global


def set_variable(resp, extract):
    """
    该函数功能：把前置所提取的数据，设置成全局变量类，方便其他接口调用数据
    :param resp: 接口返回的响应体
    :param extract: excel里面的前置提取数据
    :return:
    """
    ext_dict = eval(extract)
    logger.info(f"前置条件提取的数据字典:\n{ext_dict}")
    for key in ext_dict.keys():
        value = jsonpath(resp, ext_dict[key])   # jsonpath获取的值类型为【列表】
        logger.info(f"要提取的字段与值：\n{key} ：{value[0]}")
        if value:   # 判断数据是否为空，有值返回 True，无值返回False

            # 设置全局变量属性，并预防因为int类型报错，全部使用str()方法
            setattr(Global, key, str(value[0]))

            logger.info(f"全局变量设置成功！")
            logger.info(f"全局变量有：\n{Global.__dict__}")
        else:
            logger.exception("全局变量设置错误！！！")


if __name__ == '__main__':
    resp = {
        "code": 0,
        "msg": "OK",
        "data": {
            "id": 1236918855,
            "leave_amount": 600.0,
            "mobile_phone": "15133181962",
            "reg_name": "小柠檬",
            "reg_time": "2021-09-26 14:53:00.0",
            "type": 1,
            "token_info": {
                "token_type": "Bearer",
                "expires_in": "2021-09-26 17:27:36",
                "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEyMzY5MTg4NTUsImV4cCI6MTYzMjY0ODQ1Nn0.y6ssWXiqn0po09BofU0I-ZtbawP0dLOMa1AVh4D_ptAdy_aU6-Auwg7ehI0Ehimsk_c6dQpySecQBN3puqNaEQ"
            }
        },
        "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
    }

    extract = '{"token":"$..token", "member_id":"$..id","leave_amount":"$..leave_amount"}'
    print(set_variable(resp, extract))