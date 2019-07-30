import json
import requests

session = requests.Session()
data = session.get('http://httpbin.org/stream/3', stream=True)

print(data.text)

if data.encoding is None:
    data.encoding = 'UTF-8'

for line in data.iter_lines(decode_unicode=True):
    content = json.loads(line)
    for key, value in content.items():
        print(key, value)

session.close()


request = session.get('http://httpbin.org/post')
print(request.headers)
session.close()