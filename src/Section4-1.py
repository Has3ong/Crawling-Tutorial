import requests

with requests.Session() as s:
    pass
    r = s.get('https://www.daum.net')
    #print(r.text)

r = s.get('http://httpbin.org/cookies',
          cookies={
              'name': 'has3ong',
              'url' : 'https://github.com/Has3ong/'
          })

print(r.text)

r = s.get('http://httpbin.org/cookies/set',
          cookies={
              'name': 'has3ong',
              'url': 'https://github.com/Has3ong/'
          })

print(r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent': 'has3ong'}

r = s.get(url, headers=headers)
print(r.text)



