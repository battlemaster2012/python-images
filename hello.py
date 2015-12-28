import sys
import feedparser
import json
import datetime

def main():
    print('This is my first project in py')

    data = {}
    json_holder = {}

    d = feedparser.parse('http://backend.deviantart.com/rss.xml?type=deviation&q=by%Poromaa+sort%3Atime+meta%3Aall')

    x = 0

    for content in d.entries:
#        print(content.media_content[0]['url'])
        data['Artists'] = 'Poromaa'
        data['Date'] = str(datetime.date.today())
        data['url'] = content.media_content[0]['url']
        data['used'] = False
        json_holder[x] = data
        data = {}
        x += 1

    json_data = json.dumps(json_holder)

    parsed_json = json.loads(json_data)

    for x in range(0, len(parsed_json)):
        print(parsed_json[str(x)]['url'])
        print('X is ' + str(x))
        x += 1

if __name__ == '__main__':
    main()
