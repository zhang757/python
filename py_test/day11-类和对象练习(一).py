"""
封装一个学员类StudentStudy

属性：姓名，年龄、所在城市、期望薪资

方法一：打印学员正在学习的课程，课程作为参数传递。  XXX学员正在学习XXX课程

方法二：打印学员的期望薪资。XXX学员学完后的期望薪资为XXX

实例化2个学员，分别调用方法一和方法二
"""
class StudentStudy:     # 封装一个学员类
    # 初始化属性值
    def init(self, name, age, city, salary):
        """
        :param name: 初始化属性 name（名字）的值
        :param age: 初始化属性 age（年龄）的值
        :param city: 初始化属性 city（所在城市）的值
        :param salary: 初始化属性 salary（期望薪资）的值
        :return:
        """
        self.name = name
        self.age = age
        self.city = city
        self.salary = salary


    # 方法一：打印学员正在学习的课程，课程作为参数传递。
    def course(self, lesson):
        print(f'{self.name}学员正在学习{lesson}课程')


    # 方法二：打印学员的期望薪资。
    def salary_expectation(self):
        print(f'{self.name}学员学完后的期望薪资为{self.salary}')


# stu_study = StudentStudy()        # 把类实例成对象
#
# # 实例化第一个学员
# stu_study.init('张三', '18', '绿藤', '20k')       # 先初始化属性值函数
# stu_study.course('Python汇编')      # 调用具体方法
# stu_study.salary_expectation()       # 调用具体方法
#
# print("-" * 25, f'我是分割线',"-" * 25)
#
# # 实例化第二个学员
# stu_study.init('李四', '30', '绿藤', '30K')        # 先初始化属性值函数
# stu_study.course('Python汇编')      # 调用具体方法
# stu_study.salary_expectation()       # 调用具体方法




"""
封装一个员工类Employee:

属性：员工姓名、工作年限、户籍城市、薪资、岗位名称

方法一：计算员工的一年薪资总额(不用含年终奖)

方法二：打印员工的姓名和工作年限： 员工XXX 工作年限为 XX

             (通过self访问员工名字和员工工作年限)

实例化2个员工，分别调用方法一(打印员工的年度薪资总额)和方法二  
"""

class Employee:
    # 初始化属性值
    def init(self, name, years_work, hukou_city, salary, post):
        """
        :param name: 初始化属性 name（名字）的值
        :param years_work: 初始化属性 years_work（工作年龄）的值
        :param hukou_city: 初始化属性 hukou_city（户籍城市）的值
        :param salary: 初始化属性 salary（期望薪资）的值
        :param post: 初始化属性 post（岗位）的值
        :return:
        """
        self.name = name
        self.years_work = years_work
        self.hukou_city = hukou_city
        self.salary = salary
        self.post = post


    # 方法一：计算员工的一年薪资总额(不用含年终奖)
    def salary_sum(self):
        if type(self.salary) == int:
            sum = self.salary * 12
            print(f'{self.name}员工的一年薪资总额为：{sum}')
        else:
            print(f"期望薪资输入的类型程序计算不了，请输入整数即纯数字。")

    # 方法二：打印员工的姓名和工作年限： 员工XXX 工作年限为 XX
    def staff_years(self):
        print(f"{self.name}员工的工作年限：{self.years_work}")


# a = Employee()      # 把类实例成对象
#
# # 实例化成员张三的年薪与工作年限
# a.init('张三', '10年', '绿藤', 10000, '测试')   # 先初始化属性值
# a.salary_sum()  # 调用具体方法
# a.staff_years() # 调用具体方法
#
# print("-" * 25, f'我是分割线',"-" * 25)
#
# # 实例化成员李四的年薪与工作年限
# a.init('李四', '8年', '绿藤', 9000, '测试')     # 先初始化属性值
# a.salary_sum()  # 调用具体方法
# a.staff_years() # 调用具体方法





"""
封装一个学生类Student， -

属性：姓名，年龄，性别，英语成绩，数学成绩，语文成绩，

方法一：计算总分，

方法二：计算三科平均分

方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。

请定义此类，并实例化2个学生,并打印每个学生的个人信息，计算总分、计算平均分！
"""

class Student:
    def init(self, name, age, sex, english_score, mathe_score, language_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.english_score = english_score
        self.mathe_score = mathe_score
        self.language_score = language_score

    def sum_score(self):
        sum = self.english_score + self.mathe_score +self.language_score
        print(f'{self.name}同学的总分成绩为{sum}')


    def avg_score(self):
        sum = self.english_score + self.mathe_score + self.language_score
        score_avg = sum / 3
        print(f'{self.name}同学的平均成绩为{score_avg}')


    def student_messages(self):
        print(f"我的名字叫{self.name},年龄：{self.age},性别：{self.sex}")



student = Student()      # 把类实例成对象

# 实例化学生张三
student.init('张三', 18, '男', 90, 100, 81)    # 先初始化属性值
student.student_messages()  # 调用具体方法
student.sum_score() # 调用具体方法
student.avg_score() # 调用具体方法

print("-" * 25, f'我是分割线',"-" * 25)

# 实例化学生小孙
student.init('小孙', 18, '女', 90, 100, 99)    # 先初始化属性值
student.student_messages()  # 调用具体方法
student.sum_score() # 调用具体方法
student.avg_score() # 调用具体方法