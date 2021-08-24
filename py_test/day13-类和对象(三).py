"""
1、总结类和对象的知识点(了解的可以暂时先不管)
"""



"""
编写一个工具箱类和工具类

工具类：需要有工具具的名称、功能描述、价格。

工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。

实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。

工具比如锤子、斧头、螺丝刀等工具。

提示：不需要用到继承。
"""


# 工具箱类
class Tool_cabinet:

    def __init__(self):
        self.tool_list = []     # 定义初始化工具箱没有工具

    # 查看工具
    def select_tool(self):
        print(f'工具箱中的工具有：{self.tool_list}')


    # 新增工具
    def add_tool(self, tool_name):
        print(f'新增工具:{tool_name}')

    # 删除工具
    def del_tool(self, tool_name):
        if len(self.tool_list)>0:       # 先判断工具箱工具数量，大于0则代表有工具，小于0则代表没有工具
            if tool_name in self.tool_list:     # 判断要删除的工具，工具箱内是否存在，存在则删除，不存在则提示
                self.tool_list.remove(tool_name)
                print(f'删除工具:{tool_name}')
            else:
                print(f'工具箱中没有{tool_name}工具')
        else:
            print('工具箱中没有工具')


    # 获取工具总数
    def sum_tool(self):
        print(f'工具总数:{len(self.tool_list)}')


# 工具类
class Instrument:

    # 初始化 工具
    def __init__(self, name, func_desc, money):
        self.name = name
        self.func_desc = func_desc
        self.money = money

    # 获取实例属性 name 的值
    def get_name(self):
        return self.name

    # 获取实例属性 func_desc 的值
    def get_func_desc(self):
        return self.func_desc

    # 获取实例属性 money 的值
    def get_money(self):
        return self.money

# 实例化一个锤子
ins1 = Instrument('锤子', '敲击物品', 20)

# 实例化一个斧头
ins2 = Instrument('斧头', '砍伐树木', 30)

# 实例化一个螺丝刀
ins3 = Instrument('螺丝刀', '转动螺丝', 5)


a = Tool_cabinet()

# 工具箱新增锤子
a.add_tool(ins1.get_name())
a.tool_list.append(ins1.get_name())

# 工具箱新增斧头
a.add_tool(ins2.get_name())
a.tool_list.append(ins2.get_name())

# 工具箱新增螺丝刀
a.add_tool(ins3.get_name())
a.tool_list.append(ins3.get_name())

# 查看工具
a.select_tool()
# 查看工具数量
a.sum_tool()

# 删除指定工具
a.del_tool('斧头')

# 查看工具
a.select_tool()
# 查看工具数量
a.sum_tool()

