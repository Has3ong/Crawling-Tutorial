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

