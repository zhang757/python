"""
====================
Author: 张崽崽
Time  : 2021/9/26 11:20
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest
from tools.handler_excel import CaseFile
from tools.handler_path import case_file
from unittestreport import ddt, list_data
from tools.handler_nmb_request import HandlerRequest_nmb
from faker import Faker
from tools.handler_assert import assert_req
from tools.handler_mysql import HandlerMysql


fake = Faker(locale="zh-CN")

@ddt
class TestRegister(unittest.TestCase):
    # 获取excel用例文件绝对路径
    file_path = case_file("nmb_cases.xlsx")

    # 实例化用例文件，方便下面读取数据
    cf = CaseFile(file_path)
    cf.select_sheet_data("注册")  # 读取注册sheet表单数据
    values = cf.select_all_rows_data()      # 获取注册表单数据，并转换成标题：数据的字典

    @list_data(values)
    def test_register(self, value):
        # find()方法，匹配到返回【要搜索字符串的第一个索引值】， 未匹配到则返回 -1
        if value["data"].find("#mobile_phone#") != -1:
            while True:
                mobile_phone = fake.phone_number()
                # 实例化数据库类
                hm = HandlerMysql()
                sql = "select * from member where mobile_phone = '{}';".format(mobile_phone)
                # 通过sql语句查询当前手机号码是否已经注册过，注册则为1，未注册为 0
                count = hm.get_database_data(sql)
                if count == 0:
                    value["data"] = value["data"].replace("#mobile_phone#", mobile_phone)
                    break

        self._testMethodDoc = value["title"]
        hr_nmb = HandlerRequest_nmb()
        res = hr_nmb.send_request(value["method"], value["url"], value["data"])
        resp = res.json()
        self.assertTrue(assert_req(resp, value["assert_excpt"]))


if __name__ == '__main__':
    unittest.main()