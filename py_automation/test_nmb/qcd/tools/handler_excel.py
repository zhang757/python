"""
====================
Author: 张崽崽
Time  : 2021/9/16 17:57
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import openpyxl


class CaseFile:

    def __init__(self, file_path):
        """

        :param file_path: 被读取文件的绝对路径
        """
        try:
            # 读取文件内容
            self.wb = openpyxl.load_workbook(file_path)
        except:
            raise
        # 表单数据默认为None
        self.sheet_data = None



    def select_sheet_data(self, sheet_name):
        """

        :param sheet_name: excel文件里面的sheet表单名称
        :return:
        """
        # 获取指定表单数据
        self.sheet_data = self.wb[sheet_name]

    def select_all_rows_data(self):
        # 使用.values方法获取self.sheet_data表单的所有数据
        # self.sheet_data.values 数据是对象，所以需要转换成列表才能看到数据
        all_data = list(self.sheet_data.values)

        # 定义一个空列表接受，后期字典的keys数据与value数据
        list_data = []

        # 把all_data变量中索引为0的数据作为 字典的key
        key = all_data[0]

        for value in all_data[1:]:
            # 通过zip()函数，把key跟value组装成一个字典
            data = dict(zip(key, value))
            # 组装成字典后，放入列表
            list_data.append(data)
        return list_data



if __name__ == '__main__':
    pass