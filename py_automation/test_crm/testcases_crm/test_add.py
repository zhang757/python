"""
====================
Author: 张崽崽
Time  : 2021/9/23 11:46
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest, ddt
from tools.handler_path import case_file
from tools.handler_excel import CaseFile
from tools.handler_request_crm import HandlerRequest_crm
from tools.handler_assert import assert_req
from tools.handler_log import logger
from faker import Faker

fake = Faker(locale="zh-CN")  # 把Faker类实例化

@ddt.ddt
class TestCrm(unittest.TestCase):


    # 获取用例文件绝对路径
    file_path = case_file("api_data.xlsx")

    # 读取用例文件数据
    cases = CaseFile(file_path)
    cases.select_sheet_data("新建")
    values = cases.select_all_rows_data()

    @ddt.data(*values)
    def test_case(self, value):

        if value["data"].find("#email#") != -1:
            email = fake.email()
            value["data"] = value["data"].replace("#email#", email)

        if value["data"].find("#url#") != -1:
            url = fake.url()
            value["data"] = value["data"].replace("#url#", url)

        if value["data"].find("#phone#") != -1:
            phone = fake.phone_number()
            value["data"] = value["data"].replace("#phone#", phone)

        logger.debug(f"用例标题：{value['title']}")
        self._testMethodDoc = value['title']
        hr = HandlerRequest_crm()
        res = hr.send_request(value["method"], value["url"], value["data"])
        resp = res.json()
        assert_resp = assert_req(resp, value["assert_excpt"])
        self.assertTrue(assert_resp)


if __name__ == '__main__':
    unittest.main()