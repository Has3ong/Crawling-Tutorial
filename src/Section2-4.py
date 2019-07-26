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