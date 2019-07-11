# coding=utf-8
import requests
import json
import time
import random
import re

# 下载第一页数据
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

# 淘宝评论数据是jsonp
def load_jsonp(html):
    """
    解析jsonp数据格式为json
    :return:
    """
    try:
        return json.loads(re.match (".*?({.*}).*", html, re.S).group(1))
    except:
        raise ValueError ('Invalid Input')

# 解析 '猫眼电影-千与千寻'评论 第一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield {
            'comment':item['content'],
            'date':item['time'],
            'rate':item['score'],
            'city':item['cityName'],
            'nickname':item['nickName']
        }


# 保存数据到文本文档
def save_to_txt():
    for i in range(1, 100):
        # 猫眼电影+千与千寻
        url = 'http://m.maoyan.com/mmdb/comments/movie/1212.json?_v_=yes&offset='+str(i)
        html = get_one_page(url)
        print('正在保存第%d页。' % i)
        for item in parse_one_page(html):
            with open('Sprited Away.txt', 'a', encoding='utf-8') as f:
                print(item['date'], item['nickname'],item['city'], item['rate'], item['comment'])
                f.write(
                    item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' + str(item['rate']) + ',' + item['comment'] + '\n')
        time.sleep(5 + float(random.randint (1, 100)) / 20)


if __name__ == '__main__':
    save_to_txt()
