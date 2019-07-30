# BeautifulSoup_Basic_1

#### Beautifulsoup

* Beautiful Soup is a library that makes it easy to scrape information from web pages.
* It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

```
pip3 install beautifulsoup4
```

* HTML 
<img width=500 src="https://user-images.githubusercontent.com/44635266/62002885-13d50500-b148-11e9-884f-ed632d8da514.png">
```
> test.html

<html>
    <head>
        <title>BeautifulSoup Example</title>
    </head>
    <body>
        <h1>H1 Tag</h1>
        <h2>H2 Tag</h2>
        <p class="A">First P Tag</p>
        <p class="B">Second P Tag</p>
        <p id="C"> Third P Tag
            <p class = "D">Multiple P Tag</p>
        </p>
        <p class="A">Fourth P Tag</p>
    </body>
</html>
```

```
> Section5-1.py

from bs4 import BeautifulSoup

print('\n# soup')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
print(soup.prettify())

print('\n# h1\n')
h1 = soup.html.body.h1
print(h1)

print('\n# p1')
p1 = soup.html.body.p
print(p1)
print(p1.string)

print('\n# p2')
p2 = p1.next_sibling.next_sibling
print(p2)
print(list(p2.next_elements))

soup = BeautifulSoup(html, 'html.parser')
p3 = soup.find_all("p")  # limit=2
print('\n# p3')
type((p3))
print(p3)

print('\n# link')
# class Selector
link1 = soup.select_one("p.A")
# id Selector
link2 = soup.select_one("p#C")

print(link1)
print(link1.string)
print(link2)
print(link2.string)


print('\n# link2')
link1 = soup.select("p.A")
print(link1)
print(link1[0], link1[1])
print(link1[0].contents)
```

#### Image Scraping

<img width=500 src="https://user-images.githubusercontent.com/44635266/62005358-08480500-b16d-11e9-81d4-c59780024179.png">

```
> Section5-2.py

import os
from urllib import parse
from urllib import request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

opener = request.build_opener()
opener.addheaders = [('User-agent', UserAgent().ie)]

request.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = parse.quote_plus("벤츠")

url = base + quote
res = request.urlopen(url)

savePath = BASE_DIR + ('/5-2/')

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    print("Folder creation failed!")
else:
    print('Folder creation success!')

soup = BeautifulSoup(res, "html.parser")
imageSource = soup.select("div.img_area > a.thumb._thumb > img")

for i, imageSource in enumerate(imageSource, 1):
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    print(i, imageSource)
    request.urlretrieve(imageSource['data-source'], fullFileName)

print("download succeeded!")

```