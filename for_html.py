import urllib.request
import user_agent
import re

def get_html(url, browser):
    headers = user_agent.user_agent(browser)
    req = urllib.request.Request(url = url, headers = headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    return html
