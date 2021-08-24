import unittest

# 收集所有用例文件
s = unittest.TestLoader().discover(r'D:\学习资料\test_python\day14_unittest框架应用')
runner = unittest.TextTestRunner()

if __name__ == '__main__':
    runner.run(s)   # 运行收集到的所有用例