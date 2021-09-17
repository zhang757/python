"""
====================
Author: 张崽崽
Time  : 2021/9/17 11:22
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest, ddt
from tools.handler_path import case_file
from tools.handler_excel import CaseFile
from tools.handler_request import HandlerRequest
from tools.handler_assert import assert_req
from tools.handler_log import logger


# 获取用例文件绝对路径
file_path = case_file("api_data.xlsx")

# 读取用例文件数据
cases = CaseFile(file_path)
cases.select_sheet_data("登陆")
values = cases.select_all_rows_data()
print(values)



@ddt.ddt
class TestCrm(unittest.TestCase):

    @ddt.data(*values)
    def test_case(self, value):
        logger.debug(f"用例标题：{value['title']}")
        self._testMethodDoc = value['title']
        hr = HandlerRequest()
        res = hr.send_request(value["method"], value["url"], value["data"])
        resp = res.json()
        assert_resp = assert_req(resp, value["assert_excpt"])
        self.assertTrue(assert_resp)


if __name__ == '__main__':
    unittest.main()