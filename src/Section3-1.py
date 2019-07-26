import urllib.request
from urllib.parse import urlparse

url = "https://github.com/Has3ong/"

git = urllib.request.urlopen(url)

print('type : {}'.format(type(git)))
print("URL : {}".format(git.geturl()))
print("HTTP Status code : {}".format(git.status))
print("Headers : {}".format(git.getheaders()))
print("HTTP Get code : {}".format(git.getcode()))
print('parse : {}'.format(urlparse('https://github.com/Has3ong/?test=test').query))

API = "https://api.ipify.org"
values = {
    'format': 'json'
}

params = urllib.parse.urlencode(values)
url = API + "?" + params
print("Response URL= {}".format(url))

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print('response : {}'.format(text))
