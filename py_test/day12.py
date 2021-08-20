"""
题目1：

定义一个类Triangle用来表示三角形

定义初始化方__init__法接收三个点作为参数

（点可以用二元元组来表示，也可以使用课堂上的Point类的实例来表示，注意判断是否三个点不同）

定义方法isosceles用来判断三角形是否是等腰三角形，输出True 或False（提示，计算三个点的距离，有两个距离相等就是等腰三角形）

定义方法is_equal_sides用来判断三角形是否等边三角形，输出True或False（提示，计算三个点的距离，三个距离相等）



实例化2个对象
"""
# 方法一（直接使用边长方式）
class Triangle:
    def __init__(self, a, b, c):      # 定义3个实例属性
        self.trilateral1 = a
        self.trilateral2 = b
        self.trilateral3 = c


    def isosceles(self):  # 判断是否为等腰三角形
        if (self.trilateral1 + self.trilateral2 > self.trilateral3) and (self.trilateral1 + self.trilateral3 > self.trilateral2) and (self.trilateral2 + self.trilateral3 > self.trilateral1):  # 先判断这三边是否为三角形
            if (self.trilateral1 == self.trilateral2) or (self.trilateral1 == self.trilateral3) or (self.trilateral2 == self.trilateral3):
                print(True)     # 是等腰三角形则输出True
            else:
                print(False)    # 不是等腰三角形则输出False
        else:
            print("该三边不能组成三角形。")


    def is_equal_sides(self):   # 判断是否为等边三角形
        if (self.trilateral1 + self.trilateral2 > self.trilateral3) and (self.trilateral1 + self.trilateral3 > self.trilateral2) and (self.trilateral2 + self.trilateral3 > self.trilateral1):  # 先判断这三边是否为三角形
            if self.trilateral1 == self.trilateral2 == self.trilateral3:
                print(True)     # 是等边三角形则输出True
            else:
                print(False)    # 不是等边三角形则输出False
        else:
            print("该三边不能组成三角形。")

# # 实例化一个等腰三角形
# tar = Triangle(2, 2, 3)
# tar.isosceles()     # 等腰三角形
#
#
# # 实例化一个等边三角形
# tar1 = Triangle(2, 2, 2)
# tar1.is_equal_sides()  # 等边三角形



import math
# 方法二（使用点轴方式）
class Tar:

    def __init__(self, a_tuple, b_tuple ,c_tuple):
        # 获取a点与b点的x轴与y轴距离
        ab_x = a_tuple[0] - b_tuple[0]
        ab_y = a_tuple[1] - b_tuple[1]

        # 获取a点与c点的x轴与y轴距离
        ac_x = a_tuple[0] - c_tuple[0]
        ac_y = a_tuple[1] - c_tuple[1]

        # 获取b点与c点的x轴与y轴距离
        bc_x = b_tuple[0] - c_tuple[0]
        bc_y = b_tuple[1] - c_tuple[1]

        # 获取a点与b点直线的距离
        self.ab = math.sqrt((ab_x ** 2) + (ab_y ** 2))

        # 获取a点与c点直线的距离
        self.ac = math.sqrt((ac_x ** 2) + (ac_y ** 2))

        # 获取b点与c点的直线距离
        self.bc = math.sqrt((bc_x ** 2) + (bc_y ** 2))

        # 判断这三条线能否组成三角形
        if (self.ab + self.ac > self.bc) and (self.ab + self.bc > self.ac) and (self.ac + self.bc > self.ab):   # 为真则运行对象方法
            self.isosceles()
            self.is_equal_sides()
        else:
            print("很遗憾，这些坐标点不能组成三角形！")


    def isosceles(self):        # 等腰三角形
        if (self.ab == self.ac) or (self.ab == self.bc) or (self.ac == self.bc):    # 判断等腰三角形的依据是两边相等
            print(f"是否为等腰三角形：",True)
        else:
            print(f"是否为等腰三角形：",False)

    def is_equal_sides(self):   # 等边三角形
        if self.ab == self.bc == self.ac:       # 判断等边三角形的依据是三边相等，他也是特殊的等腰三角形
            print(f"是否为等边三角形：",True)
        else:
            print(f"是否为等边三角形：",False)


a = (0,1)
b = (0,-1)
c = (2,0)
# 实例化一：等腰三角形
d = Tar(a, b, c)

print("------------------   我是分割线    ---------------------")

# 实例化二：等边三角形
f = Tar((0,6), (0,-6), (-6*math.sqrt(3),0))



"""
题目2：

题目：定义一个登录的测试用例类LoginCase。每一个实例对象都是一个登陆测试用例。

属性：用例名称 预期结果 实际结果(初始化时不确定值哦)

方法：

运行用例

说明：有2个参数：用户名和密码。 能够登录成功的用户名：py37, 密码：666666。

通过用户名和密码正确与否来判断，是否登录成功。并返回实际结果。

ps: 可以在用例内部考虑处理不符合的情况哦：密码长度不是6位/密码不正确/用户名不正确等。。

获取用例比对结果(比对预期结果和实际结果是否相等，并输出成功or失败)

实例化2个测试用例 ，并运行用例(调用方法) ，呈现用例结果(调用方法)
"""

class LoginCase:
    def __init__(self, case_name, expected):
        self.case_name = case_name      # 定义属性 case_name  用例名称
        self.expected = expected        # 定义属性 expected   预期结果
        self.actual = None           # 定义属性 actual  实际结果


        # 初始化，用户数据库，假装后台有这些用户
        user_dict = [{"user_name": 'zhangsan', "password": '123456'},
                     {"user_name": 'zhangsi', "password": '123456'},
                     {"user_name": 'lisi', "password": '654321'},
                     {"user_name": 'wangwu', "password": 'zZ1234'},
                     {"user_name": 'py37', "password": '666666'}]

        list_key = []  # 定义两个空列表
        list_value = []
        for i in user_dict:     # 遍历列表里的字典数据
            list_key.append(i["user_name"])     # 把遍历出的字典里的key为 user_name的数据放进list_key列表中
            list_value.append(i["password"])    # 把遍历出的字典里的key为 password的数据放进list_value列表中
        case_dict = dict(zip(list_key, list_value))     # 通过zip()函数，拆包，再用dict()函数转化成新的字典
        self.users = case_dict      # 重新组成新的字典，用户名：密码（方便后续判断值）定义成实例属性



    def run_case(self, user_name, password):        # 跑用例
        if user_name in self.users.keys():      # 判断 user_name 数据是否在 实例属性 users中
            if len(password) >= 6:              # 判断输入的密码长度是否大于等于6
                if self.users[user_name] == password:       # 判断 user_name 用户的 password输入的密码是否与数据库的密码一致
                    return "登陆成功"
                else:
                    return "密码不正确"
            else:
                return "密码长度不是6位"
        else:
            return "用户名不存在/用户名错误"



# # 实例化用例1：登陆成功
# case1 = LoginCase('用例1', '登陆成功')
# act1 = case1.run_case('py37', '666666')
# case1.actual = act1
# if case1.expected == case1.actual:
#     print("比对成功")
# else:
#     print("比对失败")
#
# print("------------------   我是分割线    ---------------------")
#
# # 实例化用例2：：密码不正确
# case2 = LoginCase('用例1', '登陆成功')
# act2 = case2.run_case('py37', '6666661')
# case2.actual = act2
# if case2.expected == case2.actual:
#     print("比对成功")
# else:
#     print("比对失败")