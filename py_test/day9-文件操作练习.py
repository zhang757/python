"""
题目：把以下字典分行添加到文件当中：

person_info = [
    {
        "name": "明鹏程",
        "age": 22,
        "gender": "男",
        "hobby": "学习",
        "motto": "学习使我快乐"
    },
    {
        "name": "萌笑天",
        "age": 20,
        "gender": "女",
        "hobby": "拿30K offer",
        "motto": "下次拿个40K 的"
    },
]


得到一个 info.txt 的文件：

name,age,gender,hobby,motto
明鹏程,22,男,学习, 学习使我快乐
萌笑天,20,女,拿30K offer,下次拿个40K 的
"""

person_info = [
    {
        "name": "明鹏程",
        "age": 22,
        "gender": "男",
        "hobby": "学习",
        "motto": "学习使我快乐"
    },
    {
        "name": "萌笑天",
        "age": 20,
        "gender": "女",
        "hobby": "拿30K offer",
        "motto": "下次拿个40K 的"
    },
]


# # 方法一
# # map()函数 使用方法： map(函数, 可迭代对象)可迭代对象例如：列表、元组、字符串、字典等
# key = ','.join(map(str, person_info[0].keys()))         #
# value1 = ','.join(map(str, person_info[0].values()))
# value2 = ','.join(map(str, person_info[1].values()))
# file = open(r'D:\学习资料\test_python\test\info.txt', mode='w', encoding='utf-8')
# file.write(f'{key}\n')
# file.write(f'{value1}\n')
# file.write(f'{value2}\n')


# # 方法二
# def list_dict(info):
#     keys = person_info[0].keys()         # 获取字典内的所有keys
#     str_keys = ','.join(keys)            # 用逗号隔开变量，整体转成字符串: 'name,age,gender,hobby,motto'
#     list1 = []
#     list1.append(str_keys)               # 把字符串数据放进列表中：['name,age,gender,hobby,motto',]
#     for i in range(len(info)):
#         value = []
#         for va in info[i].values():      # 获取字典内的所有values
#             value.append(va)
#         values = [str(j) for j in value]        # 列表推导式，把数据全部转换成字符串，用新列表接收
#         str_values = ','.join(values)   # 用逗号隔开变量，整体转成字符串: '萌笑天,20,女,拿30K offer,下次拿个40K 的'
#         list1.append(str_values)        # 把字符串放进外部循环的 list1 列表中
#     return list1      # 最终列表数据：['name,age,gender,hobby,motto', '明鹏程,22,男,学习,学习使我快乐', '萌笑天,20,女,拿30K offer,下次拿个40K 的']
#
#
# data = list_dict(person_info)
# file = open(r'D:\学习资料\test_python\test\info.txt', mode='a', encoding='utf-8')
# for add_to in data:
#     file.write(f'{add_to}\n')







"""
题目：手工准备cases.txt 文件，文件中手工复制 2 行数据：

url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:/futureloan/mvc/api/member/recharge@mobile:18866668888@pwd:1000
 

请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）

列表当中，有2个字典 

每一行的数据，就是一个字典。

字典的key分别是：url,mobile,pwd
"""
# # 方法一
# r_file = open(r'D:\Github_File\py_test\cases.txt', encoding='utf-8')
# r_data = r_file.readlines()     # 读取文件全部内容
#
# data_value_list = []
# for strip_n in r_data:
#     sp_r_data = strip_n.strip().split('@')      # 先用strip()函数去除\n，再用split()函数以 @ 切割字符串
#     key_list = []
#     value_list = []
#     for data_list in sp_r_data:     # 遍历列表：['url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456', 'url:/futureloan/mvc/api/member/recharge@mobile:18866668888@pwd:1000']
#         for data_str in data_list:  # 遍历字符串： 'url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456'
#             if data_str == ':':
#                 key = data_list[:data_list.index(data_str)]     # 取：左边的数据作为key   index()获取 : 的索引， 索引含头不含尾
#                 value = data_list[data_list.index(data_str)+1:]     # 取：右边的数据作为value   index()获取 : 的索引， 索引含头不含尾
#                 key_list.append(key)
#                 value_list.append(value)
#     data_value_list.append(value_list)
#
# list_dice = []
# for values in data_value_list:      # 遍历value列表
#     data_dict = dict(zip(key_list, values))     # 使用zip()函数拆包，然后使用dict函数转换成字典
#     list_dice.append(data_dict)     # 把字典数据，放进列表
# print(list_dice)




# 方法二
def list_dict(file):
    r_file = open(file, encoding='utf-8')
    r_data = r_file.read().splitlines()     # read()读取所有数据，splitlines() 直接在行结尾中断，分割成列表
    str_list = []           # 定义新列表接收下面的字典数据
    for str_i in r_data:    # 遍历列表里的字符串
        a = str_i.split("@")        # 去除字符串中的 @ 符号后以 列表类型 展示
        a_dict = {}     # 定义新字典，接收下面组成的键值对
        for a_single in a:      # 这里的 a 是列表，所以需要遍历出字符串
            dict_list = a_single.split(':')     # 通过 ” : “ 符号分割成列表 ['pwd', '123456']
            a_dict[dict_list[0]] = dict_list[1]         # dict_list[0] 作为字典的key，dict_list[1] 作为字典的value  键值对格式往字典中加数据
        str_list.append(a_dict)     # 获取出来的字典，追加到列表中
    return str_list


print(list_dict(file=r'D:\Github_File\py_test\cases.txt'))