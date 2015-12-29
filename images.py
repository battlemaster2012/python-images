import urllib.request

response = urllib.request.urlopen('http://python.org/')

for content in response:
    urllib.request.urlretrieve(content[0]['url'], content[0]['Title'] + '.JPG')
