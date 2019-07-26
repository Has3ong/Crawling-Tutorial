# Scraping_Basic_2

### News Scraping
```
> pip3 install lxml
> pip3 install requests
> pip3 install cssselect
```

#### 네이버 실시간 검색어

<img width="600" src="https://user-images.githubusercontent.com/44635266/61955377-d9f3e980-aff5-11e9-8b73-bdf3d2d2e6a6.png">

```
# Section2-3.py
import requests
import lxml.html
import lxml.cssselect

def main():
    response = requests.get('https://www.naver.com/')
    urls = []
    root = lxml.html.fromstring(response.content)

    for i in root.cssselect('.ah_l .ah_item .ah_k'):
        url = i.text_content()
        urls.append(url)

    for url in urls:
        print(url)

main()
```

#### Using XPath

```
> Section2-4.py
import requests
from lxml.html import fromstring, tostring
import cssselect.xpath

def main():
    session = requests.Session()
    response = session.get('http://www.naver.com/')

    root = fromstring(response.content)
    root.make_links_absolute(response.url)

    for i in root.xpath('//*[@id="PM_ID_ct"]/div[1]/div[2]/div[2]/div[1]/div/ul'):
        number, name = i.xpath("//span[@class='ah_r']/text()"), i.xpath("//span[@class='ah_k']/text()")
        for j in range(len(number)):
            print(number[j], name[j])

main()
```