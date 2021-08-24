import unittest
from day14_unittest框架应用 import 注册需求和用例要求 as a


"""
该文件用例是用来测试收集功能，无须关注
"""
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 针对当前 类 整体执行之前的前置条件函数,只运行一次
        print('\n'+'*' * 20, '注册功能类的前置条件，只运行一次', '*' * 20)

    @classmethod
    def tearDownClass(cls) -> None:
        # 针对当前 类 整体执行之后的后置条件函数,只运行一次
        print('*' * 20, '注册功能类的后置条件，只运行一次', '*' * 20)

    def setUp(self) -> None:
        # 针对用例执行之前的前置条件函数，每条用例都执行
        print('\n'+'-' * 20, '用例前置条件，每条用例都执行', '-' * 20)

    def tearDown(self) -> None:
        # 针对每一条用例执行之后的后置条件函数，每条用例都执行
        print('-' * 20, '用例后置条件，每条用例都执行', '-' * 20)

    def test_register_001(self):
        # 正常注册，账号6位，password1输入6位，password2与password1一致
        res = a.register('123456', '123456', '123456')
        expect_res = {"code": 1, "msg": "注册成功"}
        self.assertEqual(expect_res, res)
        print('用例：正常注册，账号6位，password1输入6位，password2与password1一致。')


if __name__ == '__main__':
    unittest.main()
