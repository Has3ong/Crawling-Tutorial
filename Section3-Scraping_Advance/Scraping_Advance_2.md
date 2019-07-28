# Scraping_Advance_2

#### Stock Scraping

* finance.daum.net 

<img width="600" src="https://user-images.githubusercontent.com/44635266/61994704-ea20cd00-b0b8-11e9-93b0-db8ce2639eeb.png">

* ranks?limit=10

<img width="600" src="https://user-images.githubusercontent.com/44635266/61994787-256fcb80-b0ba-11e9-9ba6-2290d65a1694.png">

* Preview

<img width="400" src="https://user-images.githubusercontent.com/44635266/61995125-f871e780-b0be-11e9-84ce-0f0b0b1f11d8.png">

* Scraping Data

<img width="400" src="https://user-images.githubusercontent.com/44635266/61995055-2a367e80-b0be-11e9-98ca-bac132c9f782.png">

```
pip3 install fake-useragent
```

```
> Section3-3.py

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

```
* ua.ie
* 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0'
#### User Agent

* A software agent that performs work on behalf of the user.
* It usually means a web browser.
* Example

```
> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
> Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0
```