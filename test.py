
import user_agent
import requests
import re

headers = user_agent.user_agent('chrome')
r = requests.get("https://www.zhihu.com/explore",headers = headers )
pattern = re.compile('explore-feed.*?question_link.*?(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
print(headers)
