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
