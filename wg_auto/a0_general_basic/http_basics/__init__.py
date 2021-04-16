# coding:utf-8
from wg_auto.base import request_wrap


def http_post1(person_input='TscBdp'):
    __url = '/HttpBasics/attack1'
    return request_wrap(url=__url, method='POST',  data={"person": person_input})


def http_post2(magic_num="22"):
    __url = '/HttpBasics/attack2'
    data = {"magic_num": magic_num, "answer": "POST", "magic_answer": magic_num}
    return request_wrap(url=__url, method='POST', data=data)


