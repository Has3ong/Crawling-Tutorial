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

# DELETE
response = session.delete('http://httpbin.org/delete')
print(response.text)

session.close()