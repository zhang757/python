"""
题目：删除如下列表中的"矮穷丑"，写出 2 种或以上方法：

info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
"""

# 方法一
info1 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info1.remove("矮穷丑")     # 通过指定数据进行匹配删除，返回值为None
print("remove用法删除：", info1)



# 方法二
info2 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]

# # 索引使用①
# del info2[3]    # 通过列表索引来进行匹配删除
# print("del用法删除：", info2)

# 索引使用②
del info2[info2.index("矮穷丑")]
print("del用法删除：", info2)



# 方法三
info3 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]

# # 索引使用①
# info3.pop(3)   # 通过列表索引来进行匹配删除，返回值为指定索引数据
# print("pop(索引)用法删除：", info3)

# 索引使用②
info3.pop(info3.index("矮穷丑"))   # 通过index()函数获取指定数据索引，来进行匹配删除，返回值为指定索引数据
print("pop(索引)用法删除：", info3)



# 方法四
info4 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]

# # 索引使用①
# info4.append(info4[3])
# print("新增数据之后的列表：", info4)
# info4.remove(info4[3])
# print("删除数据之后的列表：", info4)  # 通过append方法与remove方法配合把"矮穷丑"数据更换位置挪至列表末尾
# info4.pop()     # pop方法默认删除列表末尾数据
# print("指定数据更换位置之后的列表：", info4)

# 索引使用②
info4.append(info4[info4.index("矮穷丑")])
print("新增数据之后的列表：", info4)
info4.remove(info4[info4.index("矮穷丑")])     # 这时列表里是有两个"矮穷丑"，但是index()函数的特性是显示从右往左，匹配到的第一个数据索引（也是本次要删除的数据）
print("删除数据之后的列表：", info4)  # 通过append方法与remove方法配合把"矮穷丑"数据更换位置挪至列表末尾
info4.pop()     # pop方法默认删除列表末尾数据
print("指定数据更换位置之后删除数据的最终列表：", info4)



"""
题目：现在有一个列表 li2=[1，2，3，4，5]，

请通过相关的操作改成 li2 = [0，1，2，3，66，4，5，11，22，33]。
"""
# 方法一
li2=[1, 2, 3, 4, 5]
# 索引使用①
li2.insert(0, 0)    # insert()函数，在指定位置新增数据，在索引为0的位置加了个数据 0
li2.insert(4, 66)   # insert()函数，在指定位置新增数据，在索引为4的位置加了个数据 66 （在期望结果中66就是在3的后面，3的索引为 3，所以66的索引就为 4）
li2.append(11)      # append()函数，在末尾新增数据，一次只能增加一个，不能批量添加
li2.append(22)
li2.append(33)
print(li2)

# # 索引使用②
# li2.insert(0, 0)    # insert()函数，在指定位置新增数据，在索引为0的位置加了个数据 0
# li2.insert(li2.index(4), 66)   # 先使用使用index()函数获取数据 66 的指定位置，在通过insert()函数在指定位置新增数据 66
# li2.append(11)      # append()函数，在末尾新增数据，一次只能增加一个，不能批量添加
# li2.append(22)
# li2.append(33)
# print(li2)


# 方法二
li2_1=[1, 2, 3, 4, 5]
li3 = [0, 66, 11, 22, 33]
li2_set = set(li2_1)    # 把列表转化成集合，用新变量接收值
li3_set = set(li3)      # 把列表转化成集合，用新变量接收值
li2_set.update(li3_set)     # 把集合li3_set集合的数据插入li2_set集合里
print("两集合合并后的数据：", li2_set)
li4 = list(li2_set)       # 把合并数据的li2_set数据转化成列表数据
print("合并的集合转化成列表：", li4)
li4.insert(li4.index(4), 66)    # 先使用index()函数获取数据 66 要插入的索引位置，在通过insert()函数在指定位置插入数据 66
li4.append(33)      # append()函数，在列表末尾新增数据 33
# del_value = li4[li4.index(33, li4.index(5))]    # index()函数嵌套使用获取指定索引值【列表中有多个相同数据，指定删除数字5 后面的 33】，函数用法：列表名.index(匹配数据, 开始匹配索引)--内部函数是获取"开始匹配索引"的值，外部函数是在内部函数的基础上完善函数用法
# print(del_value)
# del  del_value   # del方法使用 删除指定值
del li4[li4.index(33, li4.index(5))]    # (上面 96行至98行代码为该代码的拆解)
del li4[li4.index(66, li4.index(5))]
print("打印改变数据位置后的列表：", li4)




"""
题目：下面列表定义正确的是 (A、C)

A. ['a' 'b' 'c']

B. [1:2:3]

C. [1,[],2.5,'a']
"""



"""
题目：有列表如下
"""
# 请用列表索引的方式输出'妹子'
ls = ['心蓝',18,['健身','妹子'],[['刘德华',56],['张学友',57]]]
print(ls[2][1])



# 请用列表索引的方式输出'刘德华'
ls1 = ['心蓝',18,['健身','妹子'],[['刘德华',56],['张学友',57]]]
print(ls1[3][0][0])




# 请编写代码在ls的最后添加元素'd'，
# 方法一
ls2 = ['b','c']
ls2.append('d')     # append()函数，在列表末尾新增数据 d
print(ls2)

# 方法二
ls3 = ['b','c']
ls3.insert(len(ls3), 'd')   # 通过len()函数，获取整体列表长度，该长度就是要插入数据的索引
print(ls3)

# 方法三
ls4 = ['b','c']
ls4.extend(['d',])  # 用extend()加追函数，把数据d 追加进入
print(ls4)




# 请编写代码在ls的开头添加元素'a'
# 方法一
ls5 = ['b','c']
ls5.insert(0, 'a')      # insert()函数，指定把字符串 a 插入到索引为0的位置
print(ls5)

# 方法二
ls6 = ['b','c']
ls7 = ['a',]
ls7.extend(ls6)         # 使用两个列表变量，然后用extend()加追函数，把数据追加进入
print(ls7)





# 请编写代码，删除元素'b'
# 方法一
ls8 = ['a','b','c']
# ls8.pop(1)      # 索引使用①     pop(索引) 删除指定元素
ls8.pop(ls8.index('b'))     # 索引使用②    index()与pop()函数配套使用，更智能
print(ls8)

# 方法二
ls9 = ['a','b','c']
# del ls9[1]        # 索引使用①
del ls9[ls9.index('b')]     # 索引使用②   index()与del方法配套使用，更智能
print(ls9)






# 请编写代码修改心蓝的不良爱好'妹子'为'阅读'
# 方法一
ls10 = ['心蓝',18,['健身','妹子'],[['刘德华',56],['张学友',57]]]
ls10[2][1] = '阅读'
print(ls10)





请编写代码对ls进行从大到小排序
# 方法一
ls11 = [2,1,3]
ls11.sort(reverse=True)     # 使用sort(revese=True)函数  降序
print(ls11)

# 方法二
ls12 = [2,1,3]
ls12_set = set(ls12)    # 通过set()函数把列表转化成集合，集合自带数字升序
ls13 = list(ls12_set)   # 把升序过的集合转化成列表
print(ls13[::-1])       # 列表数据反转显示

# 方法三
ls14 = [2,1,3]
ls14_set = set(ls14)    # 通过set()函数把列表转化成集合，集合自带数字升序
ls15 = list(ls14_set)   # 把升序过的集合转化成列表
ls15.reverse()          # 通过reverse()函数，反转列表数据
print(ls15)

# 方法四
ls16 = [2,1,3]
ls16.sort()     # 使用sort()函数，把列表数据升序
ls16.reverse()      # 通过reverse()函数，反转列表数据
print(ls16)






# 请编写代码将ls中的字符串元素拼接成字符串'我爱学习天天向上'
# 方法一
ls17 = ['我', '爱', '学', '习', '天', '天', '向', '上']
str1 = ''       # 定义一个字符串
print(str1.join(ls17))       # join()函数使用：字符串变量名(字符串).join(列表变量名或元组变量名)

# 方法二
ls18 = ['我', '爱', '学', '习', '天', '天', '向', '上']
print(''.join(ls17))    # join()函数使用：字符串变量名(字符串).join(列表变量名或元组变量名)

"""
题目：简述元组与列表的区别

元组：
    ① 有序的
    ② 可读不可修改
    ③ 元组的使用方法: tulpe()
    ④ 可以存储任意数据类型
    ⑤ 可以通过索引访问
    ⑥ 元组不可以拷贝
    ⑦ 元组的查询速度比列表快
    ⑧ 元组使用符号： ()
    
列表：
    ① 有序的
    ② 允许修改
    ③ 支持拷贝
    ④ 可以通过索引访问
    ⑤ 列表查询速度比列表慢
    ⑥ 列表使用方法： list()
    ⑦ 列表使用符号： []
    ⑧ 可以存储任意数据类型
"""



"""
题目：有下面的代码

a = [[1,2,3],(4,5,6),7,8,9]
print(len(a))
输出正确的是： C

A. 9

B. 3

C. 5

D. 4

"""



"""
题目（字符串和列表）：

利用下划线将列表li=["python","java","php"]的元素拼接成一个字符串，然后将所有字母转换为大写 PYTHON_JAVA_PHP
"""
#  方法一
li=["python","java","php"]
str2 = '_'
li1 = str2.join(li)     # join()函数使用：字符串变量名(字符串).join(列表变量名或元组变量名)
print("打印拼接后结果", li1)
print("在拼接的基础上打印转换字母后的结果：", li1.upper())

# 方法二
li2=["python","java","php"]
print('_'.join(li2))    # join()函数使用：字符串变量名(字符串).join(列表变量名或元组变量名)
print('_'.join(li2).upper())    # 多函数覆盖使用，先运行join()函数，拼接成字符串后，在运行upper()函数，字符从小写转换成大写



"""
字典
1、基础级必做题


题目：下面关于字典的定义正确的是：C

A. d = {1,}

B. d = {1,2:3,4}

C. d = {'name':'xinlan','age':18}

D. d = {[1,2]:[3,4],'age':18}
"""



"""
题目：请创建一个字典用来表示你自己的个人信息。有哪些key由你自己来决定 。
"""
# 方法一
message_dict = {
    'name': '张崽崽',
    'sex': '女',
    'age': 18,
    'hobyy': 'Python',
    'city': '上海',
    'grade': 'Python自动化43期'
}
print(f"个人信息简介: {message_dict}")


# 方法二
message_dict2 = dict(name= '张崽崽', sex= '女', age= 18, hobyy= 'Python', city= '上海', grade= 'Python自动化43期')
print(f"个人信息简介: {message_dict2}")





"""
题目：使用字典和列表存储和操作以下数据
"""
# a. 某相亲节目需要获取你的个人信息(字典形式)，请存储你的：姓名、性别、年龄
# 方法一
message_dict3 = {'name': '张崽崽','sex': '女','age': 18}
print(f"个人信息简介: {message_dict3}")

# 方法二
message_dict4 = dict(name= '张崽崽', sex= '女', age= 18)
print(f"个人信息简介: {message_dict4}")





# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# 方法一
message_dict5 = {'name': '张崽崽','sex': '女','age': 18}
message_dict5['height'] = 180           # 该写法的特性：① key值存在则会修改其值   ② 如果key不存在，则会新增键值对  ③  不能批量新增键值对
message_dict5['phone'] = '13300997890'
print(message_dict5)


# 方法二
message_dict6 = {'name': '张崽崽','sex': '女','age': 18}
message_dict6.setdefault('height', 180)         # setdefault(key,value)函数特性：① key值存在则会修改其值   ② 如果key不存在，则会新增键值对  ③  不能批量新增键值对
message_dict6.setdefault('phone', '13300997890')
print(message_dict6)


# c, 平台为了保护你的隐私，需要你删除你的联系方式；
# 方法一
message_dict7 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 180, 'phone': '13300997890'}
del message_dict7['phone']
print(message_dict7)


# 方法二
message_dict8 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 180, 'phone': '13300997890'}
message_dict8.pop('phone')
print(message_dict8)






# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
# 方法一
message_dict9 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 180}
message_dict9['stage_name']= '崽崽'   # 该写法的特性：① key值存在则会修改其值   ② 如果key不存在，则会新增键值对  ③  不能批量新增键值对
message_dict9['height']= 175
print(message_dict9)


# 方法二
message_dict10= {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 180}
message_dict10.setdefault('stage_name', '崽崽')   # setdefault(key,value)函数特性：① key值存在‘不会’修改其值   ② 如果key不存在，则会新增键值对  ③  不能批量新增键值对
message_dict10['height']= 175
print(message_dict10)


# 方法三
message_dict11= {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 180}
message_dict11_2 = {'stage_name': '崽崽', 'height': 175}
message_dict11.update(message_dict11_2)     # update()插入函数，把 ‘message_dict11_2’ 字段数据插入到 ‘message_dict11’ 字典内。字典本身特性：key值存在则新数据覆盖旧数据，key值不存在则新增键值对
print(message_dict11)






# e, 你进一步添加自己的兴趣，兴趣至少包含 3个(注意：兴趣是另外一个列表。请将这个列表作为一个成员，添加到原个人信息列表当中，添加到末尾即可。
# 方法一
message_dict12 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 175, 'stage_name': '崽崽'}
message_dict12['hobyy'] = ['python', '唠嗑', '听音乐', '打游戏']
print(message_dict12)


# 方法二
message_dict13 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 175, 'stage_name': '崽崽'}
message_dict13.setdefault('hobyy', ['python', '唠嗑', '听音乐', '打游戏'])
print(message_dict13)


# 方法三
message_dict14 = {'name': '张崽崽', 'sex': '女', 'age': 18, 'height': 175, 'stage_name': '崽崽'}
message_dict15 = {'hobyy': ['python', '唠嗑', '听音乐', '打游戏']}
message_dict14.update(message_dict15)
print(message_dict14)