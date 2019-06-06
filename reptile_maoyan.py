import requests
import user_agent
import re

# get html method using requests

def get_one_page(url,browser):
    headers = user_agent.user_agent(browser)
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'https://www.maoyan.com/board/4'
    html = get_one_page(url, 'chrome')
    return html

def parse_one_page(html,re_str):
    pattern = re.compile(re_str, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }



"""需要改正"""
# # 正则表达式：
# # 排名 group1
# rank_re = '<dd>.*?<i.*?>(.*?)</i>'
# # 提取图片 group2
# pic_re = '.*?data-src="(.*?)"'
# # 电影名称 group3
# name_re = '.*?class="name".*?title="(.*?)"'
# # 主演 group4
# actor_re = '.*?class="star".*?>(.*?)</p>'
# # 上映时间 group5
# release_time_re = '.*?class="releasetime">(.*?)</p>'
# # 评分整数 group6
# rating_int_re = '.*?class="integer">(.*?)</i>'
# # 评分小数 group7
# rating_fra_re = '.*?class="fraction">(*?)</i>.*?</dd>'
# # total
# # re_str = rank_re + pic_re + name_re + actor_re + release_time_re + rating_int_re + rating_fra_re

re_str = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'+ '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'+ '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'


html = main()
for index in parse_one_page(html,re_str):
    print(index)
