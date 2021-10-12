"""
====================
Author: 张崽崽
Time  : 2021/9/26 11:21
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import unittest
from unittestreport import ddt, list_data
from tools.handler_excel import CaseFile
from tools.handler_path import case_file
from tools.handler_nmb_request import HandlerRequest_nmb
from tools.handler_variable import set_variable
from tools.handler_log import logger
from tools.handler_global import Global
from tools.handler_assert import assert_req
from tools.handler_replace import variable_replace


@ddt
class TestRecharge(unittest.TestCase):

    # 获取用例文件excel的绝对路径
    file_path = case_file("nmb_cases.xlsx")

    # 实例化读取excel文件的对象
    cf = CaseFile(file_path)
    # 通过select_sheet_data()方法读取指定sheet表单数据
    cf.select_sheet_data("充值")
    # 通过select_all_rows_data()方法把数据转换成字典方式
    values = cf.select_all_rows_data()

    @list_data(values)
    def test_recharge(self, value):

        hr = HandlerRequest_nmb()

        """第一步：先处理替换数据"""
        value = variable_replace(value)
        # # 替换1:member_id数据
        # if value["data"].find("#member_id#") != -1:
        #     value["data"] = value["data"].replace("#member_id#", getattr(Global, "member_id"))
        # # 替换2:leave_amount数据
        # if value["assert_excpt"].find("#leave_amount#") != -1:
        #     value["assert_excpt"] = value["assert_excpt"].replace("#leave_amount#", getattr(Global, "leave_amount"))

        """第二步：通过全局变量中是否存在token变量来做判断，执行不同的接口请求（有token则把token加入headers中，无则不需要）"""
        if hasattr(Global, "token"):
            hr.rs.headers["authorization"] = f'Bearer {getattr(Global, "token")}'
            res = hr.send_request(value["method"], value["url"], value["data"])
            resp = res.json()
        else:
            res = hr.send_request(value["method"], value["url"], value["data"])
            resp = res.json()

        """第三步：判断前置条件是否存在，存在则把获取的数据设置成全局变量，无则不做操作"""
        if value["extract"]:
            set_variable(resp, value["extract"])

        """第四步：以上都执行完成后，执行数据断言"""
        self.assertTrue(assert_req(resp, value["assert_excpt"]))


if __name__ == '__main__':
    unittest.main()