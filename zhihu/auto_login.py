# 获取验证码的URL地址是 
# https://www.zhihu.com/captcha.gif?r=1490690391695&type=login

# 登录需要提供的表单数据有4个：
# 用户名（email）密码（password）验证码（captcha） _xsrf

# http.cookiejar 模块可用于自动处理HTTP Cookie
# LWPCookieJar 对象就是对 cookies 的封装
# 它支持把 cookies 保存到文件以及从文件中加载
from http import cookiejar

import time 
import requests
from bs4 import BeautifulSoup
import user_agent


# session 对象 提供了 Cookie 的持久化
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename= 'cookies.txt')


try:
    #首先从cookies.txt 文件中加载 cookie信息
    print(session.cookies)
    session.cookies.load(ignore_discard = True)
except:
    # 因为首次运行还没有cookie，所有会出现 LoadError 异常。
    print('load cookies failed')


def get_xsrf():
    