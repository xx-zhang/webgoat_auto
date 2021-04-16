# coding:utf-8
import os
import json
import random
from requests.api import request
from urllib.parse import urlencode
try:
    from lib.web_sdk.logger import Log
    logging = Log(log_flag='webgoat_login')
except:
    import logging


def rand_uname(size=8):
    s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join([random.choice(s) for i in range(size)])


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
cookie_save_path = os.path.join(DATA_DIR, 'cookie.txt')


class FileManager:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as f:
            _txt = f.read().decode()
            f.close()
        return _txt

    def write(self, s: str):
        with open(self.path, 'wb') as f:
            f.write(s.encode())
            f.close()


class WebgoatLogin:

    def __init__(self, server='http://10.27.106.247:8090/WebGoat', username=None, password=None):
        self.username = username if username else rand_uname(8)
        self.password = password if password else '112233..'
        self.server = server
        self.fack_ua = "TopsecBDP-SecurityLab-Tool"

    def get_csrf_cookie(self):
        response = request(url=self.server + '/', method='get', allow_redirects=False)
        return response.headers["Set-Cookie"].split(";")[0]

    def default_headers(self):
        return {"User-Agent": self.fack_ua}

    def default_post_headers(self):
        return dict(**self.default_headers(), **{"Content-Type": "application/x-www-form-urlencoded"})

    @staticmethod
    def set_cookie(headers, cookie):
        return dict(**headers, **{"Cookie": cookie})

    def check(self, headers):
        url = "/service/lessonmenu.mvc"
        response = request(method='get', url=self.server + url, headers=headers, allow_redirects=False)
        if int(response.status_code) > 200:
            return False
        return True

    def register(self):
        payload = dict(username=self.username, password=self.password,
                       matchingPassword=self.password, agree="agree"
                       )
        response = request(
            method='post',
            data=urlencode(payload),
            url=self.server + '/register.mvc',
            headers=dict(self.default_post_headers(), **{"Cookie": self.get_csrf_cookie()}),
            allow_redirects=False
           )
        print(response.status_code)
        return response.headers["Set-Cookie"].split(";")[0]

    def get_cookie(self):
        # dict(self.default_post_headers(), **{"Cookie": self.get_csrf_cookie()})
        response = request(
            method='post',
            url=self.server + '/login',
            headers=self.default_post_headers(),
            data=urlencode({"username": self.username, "password": self.password}),
            allow_redirects=False
        )
        return response.headers["Set-Cookie"].split(";")[0]


def get_login_info(server='http://10.27.106.247:8090/WebGoat', username='test111', password='112233..'):
    wa = WebgoatLogin(server=server, username=username, password=password)
    cookie = wa.get_cookie()
    headers = wa.set_cookie(wa.default_headers(), cookie)
    flag = wa.check(headers=headers)
    if flag:
        _finput = json.dumps([username, cookie])
        FileManager(cookie_save_path).write(_finput)
        return username, cookie
    return None


def valid_cookie(server='http://10.27.106.247:8090/WebGoat', username='test111', password='112233..', force_register=False):
    if force_register:
        return WebgoatLogin(server=server, username=username, password=password).register()

    if os.path.exists(cookie_save_path):
        current_txt = FileManager(cookie_save_path).read()
        uname = json.loads(current_txt)[0]
        cookie = json.loads(current_txt)[1]
        # TODO 上面是从文件中获取的 username, cookie
        wa = WebgoatLogin(username=uname)
        flag = wa.check(headers=dict(wa.default_headers(), **{"Cookie": cookie}))
        if flag:
            logging.warn('Token 有效')
            return uname, cookie
        else:
            logging.warn('Token 无效')
            return get_login_info(server=server, username=username, password=password)
    logging.warn('Token 激活')
    return get_login_info(server=server, username=username)


if __name__ == '__main__':
    # _ = valid_cookie()
    # print(_)

    data = WebgoatLogin().register()
    print(data)