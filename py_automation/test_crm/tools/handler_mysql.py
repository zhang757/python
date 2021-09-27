"""
====================
Author: 张崽崽
Time  : 2021/9/22 17:16
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import pymysql
from tools.handler_path import conffiguration_file
from configparser import ConfigParser
from tools.handler_log import logger


class HandlerMysql:

    # 连接数据库
    def __init__(self):
        conf_file = conffiguration_file("mysql.ini")
        conf = ConfigParser()
        conf.read(conf_file, encoding='utf-8')
        conf.get("mysql", "host")
        try:
            self.conn = pymysql.connect(
                host=conf.get("mysql", "host"),
                database=conf.get("mysql", "database"),
                port=conf.getint("mysql", "port"),
                user=conf.get("mysql", "user"),
                password=conf.get("mysql", "password"),
                cursorclass=pymysql.cursors.DictCursor
            )
            logger.info("数据库连接成功！")

        except:
            logger.warning("数据库连接失败!!!")
            raise

        # 创建游标
        self.cur = self.conn.cursor()

    # 查询数据库数据
    def get_database_data(self, sql):
        """

        :param sql: sql语句
        :return:
        """
        logger.info(f"查询sql语句:\n{sql}")
        count = self.cur.execute(sql)
        logger.info(f"查询数据条目数:{count} 条")
        return count

    # 数据显示条数方式
    def get_data_way(self, sql, size=1):
        """

        :param sql: 要查询的sql语句
        :param size:
                    1：表示只查询游标所在位置的数据（1条）-----字典类型展示
                    -1：表示查询游标以下所有数据（包含游标当前位置）----列表嵌套字典展示
                    大于1： 表示游标所在位置往下查询的范围数据（包含游标当前位置）----列表嵌套字典展示
        :return:
        """

        count = self.cur.execute(sql)
        if count > 0:
            if size == 1:
                res = self.cur.fetchone()
            elif size > 1:
                res = self.cur.fetchmany(size)
            elif size == -1:
                res = self.cur.fetchall()
            logger.info(f"获取sql数据:\n{res}")
            return res
        else:
            logger.info(f"要执行的语句为0条")
            return False

    def close(self):
        self.cur.close()
        self.conn.close()





if __name__ == '__main__':
    hm = HandlerMysql()
    sql = "select * from member where type=0 limit 10;"
    print(hm.get_database_data(sql))
    print(hm.get_data_way(sql, size=5))
    hm.close()