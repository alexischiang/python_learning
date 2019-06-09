# requests库获取源代码
import requests

# pyquery库解析
from pyquery import PyQuery as pq
import user_agent


url = 'http://www.zhihu.com/explore'
headers = user_agent.user_agent('chrome')
html = requests.get(url, headers = headers).text

doc = pq(html)
items = doc('#zh-recommend-list .recommend-feed').items()

for item in items:
    print(item)
    question = item.find('h2').text()
    file = open('./zhihu/recommend.txt','a',encoding = 'utf-8')
    file.write('\n'.join([question]))
    file.write('\n' + '='*50 + '\n')
    file.close

