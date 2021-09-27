"""
====================
Author: 张崽崽
Time  : 2021/9/26 11:20
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest
from unittestreport import ddt, list_data
from tools.handler_excel import CaseFile
from tools.handler_path import case_file
from tools.handler_nmb_request import HandlerRequest_nmb
from tools.handler_assert import assert_req


@ddt
class TestLogin(unittest.TestCase):

    # 获取用例excel文件的绝对路径
    file_path = case_file("nmb_cases.xlsx")

    # 实例化文件对象
    cf = CaseFile(file_path)
    # 获取指定sheet表单数据
    cf.select_sheet_data("登陆")
    values = cf.select_all_rows_data()

    @list_data(values)
    def test_login(self, value):
        self._testMethodDoc = value["title"]
        hr_nmb = HandlerRequest_nmb()
        res = hr_nmb.send_request(value["method"], value["url"], value["data"])
        resp = res.json()
        self.assertTrue(assert_req(resp, value["assert_excpt"]))


if __name__ == '__main__':
    unittest.main()