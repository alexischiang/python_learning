# 请求 - 得到返回内容
from urllib.parse import urlencode
import requests

# 解析返回内容
from pyquery import PyQuery as pq

import json


base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host' : 'm.weibo.cn',
    'Referer' : 'https://m.weibo.cn/p/2304132611891653_-_WEIBO_SECOND_PROFILE_WEIBO',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest'
}

# 获取函数 -> json
def get_page(page):
    parmas = {
        'containerid' : '2304132611891653',
        'page_type' : '03',
        'page' : page
    }
    url = base_url + urlencode(parmas)
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            # 将response中的东西通过.json()方法解读成字典返回
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

# 解析函数
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comment_count')
            weibo['reports'] = item.get('reports_count')
            yield weibo

if __name__ == "__main__":
    count = 0
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            if '陈霸彪' in result.get('text'):
                count += 1
            print(result)
    print('你在前10页微博里提到了@都市丽人陈霸彪'+ str(count) +'次！\n')