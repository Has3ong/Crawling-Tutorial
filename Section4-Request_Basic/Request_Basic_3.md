# Request_Basic_3

#### REST API

* Representational State Transfer
* This means anything that separates a resource by name (expression of the resource) and sends and receives the status (information) of that resource.
* This refers to the application of CRUD Operation to an HTTP Method (POST, GET, PUT, DELETE)

#### Source Code
```
> Section4-3.py
import requests

session = requests.Session()

response = session.get('https://api.github.com/events')
print(response.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('Python', 'Requests', domain='httpbin.org', path='/cookies')

# GET
response = session.get('http://httpbin.org/cookies', cookies=jar)
print(response.text)

# POST 1
response = session.post('http://httpbin.org/post', data={'Python': 'Requests'}, cookies=jar)
print(response.text)
print(response.headers)


# POST 2
postData = {
    'language': 'python',
    'version' : '3.7',
    'url' : 'http://httpbin.org/post'
}

response = session.post("http://httpbin.org/post", data=postData)
print(response.text)

# PUT
putData = {
    'data' : '{"language" : "python", "package": "request"}'
}

response = session.put('http://httpbin.org/put', data=putData)
print(response.text)

# DELETE 1
response = session.delete('http://httpbin.org/delete')
print(response.text)

# DELETE 2
r = session.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.text)

session.close()
```


* Result
```
{
  "cookies": {
    "Python": "Requests"
  }
}

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "Python": "Requests"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "15", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "211.214.14.153, 211.214.14.153", 
  "url": "https://httpbin.org/post"
}

{'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Origin': '*', 'Content-Encoding': 'gzip', 'Content-Type': 'application/json', 'Date': 'Sun, 28 Jul 2019 05:17:48 GMT', 'Referrer-Policy': 'no-referrer-when-downgrade', 'Server': 'nginx', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'DENY', 'X-XSS-Protection': '1; mode=block', 'Content-Length': '266', 'Connection': 'keep-alive'}
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "language": "python", 
    "url": "http://httpbin.org/post", 
    "version": "3.7"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "63", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "211.214.14.153, 211.214.14.153", 
  "url": "https://httpbin.org/post"
}

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "data": "{\"language\" : \"python\", \"package\": \"request\"}"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "76", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "211.214.14.153, 211.214.14.153", 
  "url": "https://httpbin.org/put"
}

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "211.214.14.153, 211.214.14.153", 
  "url": "https://httpbin.org/delete"
}

```