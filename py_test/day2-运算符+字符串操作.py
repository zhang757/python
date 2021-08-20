"""
题目：现在有字符串：str1 = 'python cainiao 666'
"""
# 请使用代码找出第 5 个字符
str1 = 'python cainiao 666'
print(str1[4])

# 请复制一份字符串，保存在变量 str_two 当中(赋值运算符)
str1 = 'python cainiao 666'
str_two = str1  # 把str1变量值赋值给str_two
print(str_two == str1)      # 查看str1跟str_two的值是否相等
print(str1)
print(str_two)




"""
题目：卖橘子的计算器（字符串转化）
写一段代码，用户输入橘子的价格，和重量，计算出应该支付的金额！（提示：不需要校验数据，默认传入数字就可以了。使用input函数获取用户输入哦，并且input 得到的数据都是字符串类型）
"""
# 整数写法
price = int(input("请输入价格(请输入整数)"))     # 使用int()整数函数强制转换字符串数据
weight = int(input("请输入重量(请输入整数)"))    # 使用int()整数函数强制转换字符串数据
money = price * weight
print(f"橘子{price}元/斤，买了{weight}斤,一共花了{money}元")     # f"{}"写法为占位符写法

# 浮点数写法
price = float(input("请输入价格"))   # 使用float()浮点数函数强制转换字符串数据
weight = float(input("请输入重量"))  # 使用float()浮点数函数强制转换字符串数据
money = price * weight
print(f"橘子{price}元/斤，买了{weight}斤,一共花了{money}元")     # f"{}"写法为占位符写法





"""
题目：字符串综合演练 （字符串索引和切片。注意位置和索引的区别）
my_hobby = "Never stop learning!"
说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”）；“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）；开始位置 ，是指字符串起始，即下标为0开始；末尾，是指字符串最后。
"""
# 截取从 位置2 ~ 位置6 的字符串(含 位置2和6)
my_hobby = "Never stop learning!"
print(my_hobby[1:6])    # 位置2~6即索引为 1~5，但是切片有个规则取头不取尾，所以5要+1

# 截取完整的字符串
my_hobby = "Never stop learning!"
print(my_hobby)     # 直接打印输出所有字符串
print(my_hobby[::]) # 通过切片，默认获取所有字符串

# 从 索引3 开始，每2个字符中取一个字符(含索引3，步长为2)
my_hobby = "Never stop learning!"
print(my_hobby[3::2])   # 默认最终长度根据规则切片
print(len(my_hobby))
print(my_hobby[3:len(my_hobby):2])    # 自动获取索引长度，根据规则切片（len函数获取了位置长度为偶数，步长也为偶数，所以势必要取最后一个值，故没有-1）

# 截取字符串末尾两个字符
my_hobby = "Never stop learning!"
print(my_hobby[-2:])  # 从-2索引开始往右默认取值
print(my_hobby[len(my_hobby)-2:])   # len（my_hobby）-2 获取倒数第二位数的索引，
print(my_hobby[len(my_hobby)-2:len(my_hobby)])  # len（my_hobby）-2 获取倒数第二位数的索引，len(my_hobby)获取字符串总长度，因为要取尾故没有-1

# 字符串的倒序
my_hobby = "Never stop learning!"
print(my_hobby[::-1])




"""
题目：有字符串s如下:   s = 'python'
"""
# 请编写代码打印字符串s的第一个字符
s = 'python'
print(f"打印字符串s的第一个字符:{s[0]}")   # f"{}"写法为占位符写法

# 请编写代码打印字符串s的最后一个字符
s = 'python'
print(f"打印字符串s的最后一个字符:{s[-1]}")     # f"{}"写法为占位符写法




"""
题目：有字符串s如下:  s = '1234567890'
"""
# 请编写代码用切片的方式打印出'13579'
s = '1234567890'
print(s[::2])   # 从索引0开始，每2个步长取一个值

# 请编写代码用切片的方式打印出'97531'
s = '1234567890'
print(s[::-1][1::2])    # s[::-1]倒序数字，然后在倒叙的基础上从索引1开始每2个步长取一个值
print(s[-2::-2])    # 从-2索引开始，往左边每2个步长取一个值

# 请编写代码用切片的方式打印出'24680'
s = '1234567890'
print(s[1::2])  # 从索引1开始，每2个步长取一个值




"""
题目：将"hello world"转为字母大写"HELLO WORLD"
"""
str1 = "hell world"
print(str1.upper()) # upper()函数将字符串中的小写字母转为大写字母




"""
题目： 将字符串"I Love Java" 变成"I Love Python"（替换）
"""
java = "I Love Java"
python = java.replace("Java", "Python")     # 为什么要生成新的变量，是因为字符串是不允许修改的，所以针对替换操作，需要用新的变量来接收，非则会报错
print(java)
print(python)