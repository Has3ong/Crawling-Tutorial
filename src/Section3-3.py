import json
from urllib import request
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"
ret = request.urlopen(request.Request(url, headers=headers)).read().decode('utf-8')
rank_json = json.loads(ret)['data']


for element in rank_json:
    print(element['rank'], element['tradePrice'], element['name'])
