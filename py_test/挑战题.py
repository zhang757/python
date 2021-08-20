"""
题目：实现冒泡排序（不要求提交，面试之前背熟，什么是冒泡排序需要自己了解）

具体需求：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法

编码提示：

1、先写出第一轮比较的代码哦。如在a当中，将最大的一个数据放在列表最后。

2、再写出第二轮比较的代码：在1之后的列表当中，将第二大的数据，放在列表的倒数第二

3、以此类推

4、比对以上所写的代码，有何相同，有何不同之处。再考虑使用外层for来替换
"""

a=[1, 7, 4, 89, 34, 2]

for i in range(1, len(a)):
    for j in range(0, len(a) - i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1], a[j]        # 从小到大

        # if a[j] < a[j+1]:
        #     a[j], a[j+1] = a[j+1], a[j]         # 从大到小
print(a)



"""
用户从键盘输入一行字符，编写一个程序，统计并输出其中英文字符，数字，空格和其他字符的个数。
提示：遍历字符串，通过字符串方法判断字符类型，然后统计
"""
# letter = 0
# num = 0
# blank = 0
# other = 0
# char_str = input("请随机输入字符串：")
# for i in char_str:
#     if i.isalpha():     # isalpha() 所有字符都是字母
#         letter += 1
#     elif i.isdigit():   # isdigit() 所有字符都是数字
#         num += 1
#     elif i.isspace():       # isspace() 所有字符都是空白字符
#         blank += 1
#     else:
#         other += 1
#
# print(f"中英文字符个数：{letter} \n数字字符个数：{num} \n空格字符个数：{blank} \n其他字符个数：{other}")



"""
使用print函数和循环结构输出如下由*组成的金字塔（可以尝试根据层数动态输出）
   *
  ***
 *****
*******
"""
print(' '*3 + '*'*1)    # i = 1   (1+2*0) 星号数量规律：1+2*(i-1) 简化 2 * i -1
print(' '*2 + '*'*3)    # i = 2  (1+2*1)
print(' '*1 + '*'*5)    # i = 3 (1+2*2)
print(' '*0 + '*'*7)

# 第一个方法
num = int(input("请输入金字塔层数："))
for i in range(1, num+1):
    print(' ' * (num-i) + '*' * (2*i-1), end='\n')

# 倒着的金字塔
num = int(input("请输入金字塔层数："))
for i in range(num, 0, -1):
    print(' ' * (num-i) + '*' * (2*i-1), end='\n')


# 第二个方法
num = int(input("请输入金字塔层数："))
for i in range(1, num +1):      # 循环金字塔层数
    for j in range(1, num +1):
        j = ' ' * (num-i)
        # print(' ' * (num-i))
        for k in range(1, num +1):
            k = '*' * (2*i-1)
            # print('*' * (2*i-1))
    print(j+k)


