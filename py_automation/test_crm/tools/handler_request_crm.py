"""
====================
Author: 张崽崽
Time  : 2021/9/14 15:54
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import requests
from tools.login import Login
from tools.handler_path import conffiguration_file
from configparser import ConfigParser
from tools.handler_log import logger


class HandlerRequest_crm():

    def __init__(self):
        self.rs = requests.Session()        # 请求一个会话
        self.rs.headers = {"admin-token": Login(), "authorization": Login(), "content-type": "application/json"}    # 给会话设置默认请求头格式
        server_file = conffiguration_file("baseurl.ini")        # 通过封装的conffiguration_file()配置文件路径函数获取指定文件绝对路径
        conf = ConfigParser()   # 实例化配置对象
        conf.read(server_file)      # 读取指定配置文件
        self.baseurl = conf.get("base", "baseurl")  # 获取文件中某模块的某一个变量值

    def send_request(self, method, api_uri, data=None, **kwargs):
        """

        :param method: 请求方式
        :param api_uri: 接口uri（不包含域名）
        :param data: 接口传参数据，默认为None，防止无数据时报错（也叫 body体）
        :param kwargs: 用来接收其他参数数据，比如上传文件时用到的 file参数
        :return: 返回接口响应结果
        """

        url = self.baseurl + api_uri    # 域名与接口uri拼接成完整的url
        logger.info(f"请求接口：\n{url}")
        logger.info(f"请求方式：{method}")
        logger.info(f"请求body体数据：\n{data}")
        logger.info(f"请求headers：\n{self.rs.headers}")
        if method == 'GET' or method == 'get':
            res = self.rs.get(url, params=data)     # get请求方式
        else:
            # 根据自己输出的method来做接口请求方式，data= 的数据，因为在self.rs.headers中已经默认为"content-type": "application/json"了，系统会自动帮忙处理成json数据
            res = self.rs.request(method, url, data=data.encode("utf-8"), **kwargs)
        logger.info(f"http响应状态码：{res.status_code}")
        logger.info(f"响应body体：\n{res.text}")

        return res

if __name__ == '__main__':
    h1 = HandlerRequest_crm()