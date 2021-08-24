import unittest
from day14_unittest框架应用 import 注册需求和用例要求 as a
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 针对当前 类 整体执行之前的前置条件函数，只运行一次
        print('\n'+'*'*20, '注册功能类的前置条件，只运行一次','*'*20)

    @classmethod
    def tearDownClass(cls) -> None:
        # 针对当前 类 整体执行之后的后置条件函数，只运行一次
        print('*' * 20, '注册功能类的后置条件，只运行一次', '*' * 20)

    def setUp(self) -> None:
        # 针对用例执行之前的前置条件函数，每条用例都执行
        print('\n'+'-'*20, '用例前置条件，每条用例都执行', '-'*20)

    def tearDown(self) -> None:
        # 针对用例执行之后的后置条件函数，每条用例都执行
        print('-' * 20, '用例后置条件，每条用例都执行', '-' * 20)

    def test_register_001(self):
        # 正常注册，账号6位，password1输入6位，password2与password1一致
        res = a.register('123456', '123456', '123456')
        expect_res = {"code": 1, "msg": "注册成功"}
        self.assertEqual(expect_res, res)
        print('用例：正常注册，账号6位，password1输入6位，password2与password1一致。')


    def test_register_002(self):
        # 正常注册，账号18位，password1输入18位，password2与password1一致
        res = a.register('zhangsan1234567890', '123456789012345678', '123456789012345678')
        expect_res = {"code": 1, "msg": "注册成功"}
        self.assertEqual(expect_res, res)
        print('用例：正常注册，账号18位，password1输入18位，password2与password1一致。')


    def test_register_003(self):
        # 账户为空
        res = a.register('', '123456', '123456')
        expect_res = {"code": 0, "msg": "所有参数不能为空"}
        self.assertEqual(expect_res, res)
        print('用例：账户为空。')

    def test_register_004(self):
        # 账户已存在
        res = a.register('python26', '123456', '123456')
        expect_res = {"code": 0, "msg": "该账户已存在"}
        self.assertEqual(expect_res, res)
        print('用例：账户已存在。')


    def test_register_005(self):
        # 账户输入5个字符
        res = a.register('zhang', '123456', '123456')
        expect_res = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        self.assertEqual(expect_res, res)
        print('用例：账户输入5个字符。')

    def test_register_006(self):
        # 账户输入19个字符
        res = a.register('1234567890123456789', '123456', '123456')
        expect_res = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        self.assertEqual(expect_res, res)
        print('用例：账户输入19个字符。')

    def test_register_007(self):
        # 密码为空
        res = a.register('zhangsan', '', '123456')
        expect_res = {"code": 0, "msg": "所有参数不能为空"}
        self.assertEqual(expect_res, res)
        print('用例：密码为空。')

    def test_register_008(self):
        # 密码位数为 5
        res = a.register('zhangsan', '12345', '12345')
        expect_res = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        self.assertEqual(expect_res, res)
        print('用例：密码5位数。')


    def test_register_009(self):
        # 密码位数为 19
        res = a.register('zhangsan', '1234567890123456789', '1234567890123456789')
        expect_res = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        self.assertEqual(expect_res, res)
        print('用例：密码位数为 19。')

    def test_register_010(self):
        # 密码位数为 19，确认密码为 6 位数（password1跟password2都为异常的情况下的对比，情况特殊）
        res = a.register('zhangsan', '1234567890123456789', '123456')
        expect_res = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        self.assertEqual(expect_res, res)
        print('用例：密码为 19位，确认密码为 6 位。')

    def test_register_011(self):
        # password2 为空
        res = a.register('zhangsan', '123456', '')
        expect_res = {"code": 0, "msg": "所有参数不能为空"}
        self.assertEqual(expect_res, res)
        print('用例：password2 为空。')

    def test_register_012(self):
        # password2 比 password1少一位数
        res = a.register('zhangsan', '123456', '12345')
        expect_res = {"code": 0, "msg": "两次密码不一致"}
        self.assertEqual(expect_res, res)
        print('用例：password2 比 password1少一位数')

    def test_register_013(self):
        # password2 比 password1多一位数
        res = a.register('zhangsan', '123456', '1234567')
        expect_res = {"code": 0, "msg": "两次密码不一致"}
        self.assertEqual(expect_res, res)
        print('用例：password2 比 password1多一位数')

    def test_register_014(self):
        # password2 与 password1 密码长度相同，数据不一致
        res = a.register('zhangsan', '123456', '654321')
        expect_res = {"code": 0, "msg": "两次密码不一致"}
        self.assertEqual(expect_res, res)
        print('用例：password2 与 password1 密码长度相同，数据不一致')


if __name__ == '__main__':
    unittest.main()
