import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': 'khsh5592',
    'password': 'gktjdgktjd1025'
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