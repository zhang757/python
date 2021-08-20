"""
题目：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：

一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。
"""

def special_offer(money):
    """
    :param money:   原始价格
    :return:
    """
    if 50 <= money <= 100:
        preferrntial = money * 0.9
        print("打10%的折扣，优惠后的价格：{}元".format(preferrntial))
    elif money > 100:
        preferrntial = money * 0.8
        print("打20%的折扣，优惠后的价格：{}元".format(preferrntial))
    else:
        print("没有折扣，原价：{}元".format(money))


# special_offer(20)



"""
题目：不定长参数
定义函数，将输入的所有数字相乘之后对20取余数，用户输入的数字个数不确定。
"""

def remainder(*args):
    """
    :param args:    不定长参数，输入任意数字，都能以元组的形式接受
    :return:
    """
    product = 1     # 因为是数字相乘，所以先定义积为1，如果是sum则为0
    for i in args:      # 遍历输入的数据
        if type(i) == int or type(i) == float:      # 用if判断 i 的数据类型，符合要求则进行相乘，不符合则跳过，python中的计算，必须是数字类型才可以，否则会报错
            product *= i
        else:
            continue        # 跳过该条件数据，继续下一个操作
    surplus = product % 20
    print('余数为：{}'.format(surplus))


# remainder(1, 2, 3, 4,'你好')




"""
题目：列表去重函数
定义一个函数 def remove_element(a_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素(不能用集合去重，要使用for循环)。
def remove_repeatitive_elements(a_list):
    ...

my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
remove_repeatitive_elements(my_list)
"""

def remove_repeatitive_elements(a_list):
    """
    :param a_list:      列表类型数据
    :return:
    """
    test_list = []      # 定义一个新的空列表
    for i in a_list:        # 遍历列表数据
        if not i in test_list:      # 通过判断来辨别数据有没有重复，重复的数据则过滤
            test_list.append(i)     # 满足条件的则把数据新增到列表里
    print(test_list)

# remove_repeatitive_elements([10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1])




"""
题目：通过定义一个计算器函数，调用函数传递两个参数，
然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
"""
def calculator(a, b):
    operation = input("请选择操作(【1】加、【2】减、【3】乘、【4】除)：")
    if operation == '1':
        sum =  a + b
    elif operation == '2':
        sum = a - b
    elif operation == '3':
        sum = a * b
    elif operation == '4':
        sum = a / b
    else:
        print("其他操作敬请期待！")
    return sum

# print(calculator(1, 2))




"""
题目：BMI 计算
使用函数完成以下操作
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 : 65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25： 正常 25-28： 过重 28-32： 肥胖 高于32： 严重肥胖
def get_bmi(height, weight):
    ...
"""

def get_bmi(height, weight):
    """
    :param height:  身高以 m 为单位
    :param weight:  体重以 kg 为单位
    :return:
    """
    BMI = weight / height ** 2
    if BMI < 18.5:
        print("您的BMI指数过轻！")
    elif 18.5 <= BMI < 25:
        print("您的BMI指数正常。")
    elif 25 <= BMI < 28:
        print("您的BMI指数过重！")
    elif 28 <= BMI < 32:
        print("您的BMI指数肥胖！")
    else:
        print("您的BMI指数严重肥胖！")


# get_bmi(1.60, 220)




"""
题目：挑选足球运动员
一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
编写一个程序，根据用户的姓名，性别和年龄，打印这个人是否可以加入球队，询问10次后，打印满足条件的所有人的名字。
（要求：定义函数处理逻辑)
"""
# 题目没修改前的接替思路
# def football_player():
#     offer_letter = []
#     for i in range(1, 11):
#         sex = input("请输入性别：")
#         if sex == '女':
#             age = int(input("请输入年龄："))
#             if 15 <= age <= 22:
#                 name = input("请输入姓名：")
#                 offer_letter.append(name)
#             else:
#                 print("对不起，你的年龄不符合招收标注")
#         else:
#             print("对不起，你的性别不符合招收标注")
#     print(f"符合标注名单：{offer_letter}")

# football_player()




# 题目修改后的解题思路
def football_menber(sex, age, name):
    if sex == '女':
        if 15 <= age <= 22:
            return name
        else:
            print("对不起，你的年龄不符合招收标准")
    else:
        print("对不起，你的性别不符合招收标准")

offer = []
for i in range(4):      # 10次太长了，暂时用4次测试
    sex = input("请输入性别：")
    age = int(input("请输入年龄："))
    name = input("请输入姓名：")
    if football_menber(sex=sex, age=age, name=name) == name:
        offer.append(football_menber(sex=sex, age=age, name=name))
    else:
        continue
print(offer)



"""
题目：列表和字典数据类型转换
# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
"""

# # 要求一：把上述数据转换为以下格式
# res1 = [
#     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

#
# list1 = []  # 定义新列表接受数据
# for values in range(1, len(cases)):     # 从索引 1 开始遍历后面的列表数据，方便后期获取字典的value值
#     dict1 = {}      # 定义一个空字典，接受下面遍历完后的字典数据
#     for key in range(len(cases[0])):    # 遍历索引 0 的数据，作为字典的key值
#         dict1[cases[0][key]] = cases[values][key]       # 已经获取了key值，value值 组合成字典数据
#     list1.append(dict1)     # 每遍历完一条新字典，则新增到列表中
# print(list1)
#
# # # 方便查看list1的数据
# # for i in list1:
# #     print(i)
#
#
#
#
# # 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
# res = [
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]
#
# list2 = []
# for i in list1:
#     if i['case_id'] > 3:
#         list2.append(i)
# print(list2)