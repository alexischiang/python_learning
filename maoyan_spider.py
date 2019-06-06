import requests
import user_agent
import re
import json
import time

# get html method using requests

def get_one_page(url,browser):
    headers = user_agent.user_agent(browser)
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    return None


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

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # json.dumps()函数是将字典转化为字符串
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii= False )+'\n')

def main(offset):
    re_str = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'+ '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'+ '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
    url = 'https://www.maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url, 'chrome')
    for item in parse_one_page(html, re_str):
        write_to_file(item)

if __name__ == "__main__":
    for i in range(10):
        main(offset= i * 10)
        time.sleep(1)
