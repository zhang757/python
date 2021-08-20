# class Animal:
#     name = ""
#     colour = ""
#     age = 0
#     sex = ""
#
#     def running(self):  # 跑函数
#         print("它们会跑")
#
#
#     def cry(self):      # 叫函数
#         print("它们会叫")
#
#
# class Cat(Animal):      # 创建子类，继承父类
#     hair = "短毛"         # 添加新属性
#
#     def __init__(self):
#         super(Cat, self).__init__()
#
#     def cat_mouse(self):        # 添加新方法
#         print("它会抓老鼠")
#
#     # def cry(self):          # 重写父类
#     #     print("它会喵喵叫")
#
#     def cry(self):
#         print("它会喵喵叫")
#
#
# cat = Cat()
# cat.cry()


# class Dog:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = None
#         print(self.__name, "生成成功")
#
# dog = Dog("旺财")
# print(dog)


# a = 1
# b = 2
# def fn1():
#     global a
#     a = 12
#     b = 34
#
# def fn2():
#     global a
#     print(a)
#
# def fn3():
#     b = 3
#     print(b)
#
# if __name__=="__mian__":
#     fn1()
#     fn2()
#     fn3()
import copy


def test():
    a = ['word', 2, 3]
    b = a
    data = [3, [55, 44], (7, 8, 9)]
    temp = list(data)
    data[1].append(33)
    data[2] +=(10, 11)
    print(b)
    print(data)
    print(temp)

# # 代码块一
# a = {1: [1, 2, 3]}
# b = a.copy()
# a[1].append(4)
# print("a:", a)
# print("b:", b)
#
# # 代码块二
# d ={1:[1, 2, 3]}
# c = copy.deepcopy(a)
# a[1].append(5)
# print("d:", d)
# print("c:", c)
