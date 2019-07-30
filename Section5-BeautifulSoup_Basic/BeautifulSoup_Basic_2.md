# BeautifulSoup_Basic_1

#### Login Site

* Using *ReDirectUrl, Referer, loginMemberType, id, password*
<img width=500 src="https://user-images.githubusercontent.com/44635266/62006120-637ef500-b177-11e9-8e60-8cb571857432.png">

<img width =500 src="https://user-images.githubusercontent.com/44635266/62006115-54984280-b177-11e9-89d1-a862f58c751c.png">

```
> Section5-3.py
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': '',
    'password': ''
}

headers = {
    'User-Agent': UserAgent().chrome,
    'Referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fcws.danawa.com%2Fpoint%2Findex.php'
}

with requests.session() as session:
    res = session.post('https://auth.danawa.com/login', login_info, headers=headers)

    if res.status_code != 200:
        raise Exception('Login failed.')

    res = session.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    check_name = soup.find('p', class_="user")
    if check_name is None:
        raise Exception('Login failed. Wrong Password.')

    info_list = soup.select("p.pd_txt")

    print('\nMy Danawa Pay Order List')
    print('==========================================\n')

    for i in info_list:
        print(i)
```

* Result
```
My Danawa Pay Order List
==========================================

<p class="pd_txt">SSD 970 EVO Plus M.2 2280 병행수입(500GB) 외 1건</p>
<p class="pd_txt">Arctis 5 7.1 Surround RGB (정품)</p>

```