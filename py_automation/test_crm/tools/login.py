"""
====================
Author: 张崽崽
Time  : 2021/8/26 15:02
Project: test_python
Motto: 不敲代码，就看看你的余额！
====================
"""
import requests


def Login(user='zhangzaizai', password='zZ12345678'):
    requ_url = 'https://lesscodeapitest.bjx.cloud/usercenter/api/v1/user/login'
    method = 'post'
    header = {"content-type": "application/json"}
    data = {"loginName": user, "password": password, "loginType": 2}
    res = requests.request(method, url=requ_url, headers=header, json=data)
    response = res.json()
    return response["data"]["token"]


if __name__ == '__main__':
    print(Login())
