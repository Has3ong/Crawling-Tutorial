import requests

with requests.Session() as s:
    pass
    request = s.get('https://www.daum.net')
    #print(request.text)

request = s.get('http://httpbin.org/cookies',
          cookies={
              'name': 'has3ong',
              'url' : 'https://github.com/Has3ong/'
          })

print(request.text)

request = s.get('http://httpbin.org/cookies/set',
          cookies={
              'name': 'has3ong',
              'url': 'https://github.com/Has3ong/'
          })

print(request.text)

url = 'http://httpbin.org/get'
headers = {'user-agent': 'has3ong'}

request = s.get(url, headers=headers)
print(request.text)



