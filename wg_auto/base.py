# coding:utf-8
from requests.api import request
from urllib.parse import urlencode

SERVER = 'http://10.27.106.247:8090/WebGoat'
USERNAME = 'test111'
PASSWORD = '112233..'


from wg_auto.wg_token import WebgoatLogin, valid_cookie


def request_wrap(url, method='GET', data=None):
    wl = WebgoatLogin(server=SERVER, username=USERNAME, password=PASSWORD)
    cookie = valid_cookie(server=SERVER, username=USERNAME, password=PASSWORD)[1]

    if method.lower() == 'get':
        return request(method=method, headers=dict(wl.default_headers(), **{"Cookie": cookie}), url=wl.server + url)

    if method.lower() == 'post':
        return request(method=method, headers=dict(wl.default_post_headers(), **{"Cookie": cookie}), url=wl.server + url, data=urlencode(data))


