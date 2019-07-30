# Request_Basic_2.md

* http://httpbin.org/#/Dynamic_data/get_stream__n_

<img width="400" src="https://user-images.githubusercontent.com/44635266/62002228-98208b80-b13a-11e9-93e2-6c8cc4b720e9.png">

<img width="400" src="https://user-images.githubusercontent.com/44635266/62002229-99ea4f00-b13a-11e9-9267-cb72e3bb7653.png">

#### Source Code

```
> Section4-2.py
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
```
