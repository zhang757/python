"""
====================
Author: 张崽崽
Time  : 2021/9/16 10:48
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
from jsonpath import jsonpath
from tools.handler_log import logger







excel_assert_data = '[{"actual":"$..code", "expect": 0, "assert_type": "=="},{"actual":"$..message", "expect": "", "assert_type": "=="}]'

resp = {
	"code": 0,
	"message": "",
	"data": {
		"token": "4w5eayuefd8z9rtvfbhet4k2gnqeiolw9vvg1mhxtc4k3uu6vf",
		"userId": "75",
		"orgId": "202505060582035456",
		"orgName": "testcustomer",
		"orgCode": "",
		"name": "张崽崽",
		"avatar": "",
		"needInitOrg": False
	}
}

def assert_req(resp, excel_assert_data):
    """
    jsonpath()函数获取出来的值，都是列表形式的！！！
    :param resp: 响应结果
    :param excel_assert_data: excel中获取的断言对比结果,数据类型：
            [
                {"actual":"$..code", "expect": 0, "assert_type": "=="},
                {"actual":"$..message", "expect": "", "assert_type": "=="}
            ]
    :return:
    """
    assert_data = eval(excel_assert_data)
    for i in assert_data:       # 遍历对比列表数据
        logger.info(f"断言表达式、期望结果和比对方式为：\n{i}")
        logger.info(f"提取实际结果的jsonpath表达式：{jsonpath(i, '$..actual')[0]}")
        logger.info(f"响应数据：\n{resp}")
        actual = jsonpath(resp, jsonpath(i, "$..actual")[0])     # 获取实际结果中的值，以列表接收
        logger.info(f"实际结果：{actual[0]}")
        logger.info(f"期望结果：{jsonpath(i, '$..expect')[0]}")
        if jsonpath(i, '$..assert_type')[0] == "==":   # 判断assert_type字段值的类型做对应的断言
            try:
                assert actual[0] == jsonpath(i, "$..expect")[0]
                logger.info("断言成功。")
            except:
                logger.exception("实际值与期望值不相等。")
                return False
    return True



if __name__ == '__main__':
    print(assert_req(resp, excel_assert_data))
