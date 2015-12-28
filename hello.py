import sys
import feedparser
import json
import datetime
import db_testing


#"""
#    This is just for me to get the API part and the base part working
#    API will deal with the DB stuff so I just need to send the artist name and number of
#    images to the API to get the url's of the images to download
#"""


def main():
    print('This is my first project in py')

    data = {}
    json_holder = {}

    d = feedparser.parse('http://backend.deviantart.com/rss.xml?type=deviation&q=by%Poromaa+sort%3Atime+meta%3Aall')

    x = 0

    db_testing.db.drop_collection('images')
    images = db_testing.db['images']

    for content in d.entries:
#        print(content.media_content[0]['url'])
        data['Artists'] = 'Poromaa'
        data['Date'] = str(datetime.date.today())
        data['url'] = content.media_content[0]['url']
        data['used'] = False
        data['SFW'] = True if content.media_rating['content'] == 'nonadult' else False
        json_holder[x] = data
        data = {}
        x += 1

#    images.insert(json_holder)

    json_data = json.dumps(json_holder)

#    images.insert(json_data)

    parsed_json = json.loads(json_data)

#    images.insert(parsed_json)

    for x in range(0, len(parsed_json)):
#        output = output + str(parsed_json[str(x)])
#        if x != (len(parsed_json) - 1):
#            output = output + ','
#        print(str(parsed_json[str(x)]))
        images.insert(parsed_json[str(x)])
        x += 1

#    output = output + ']'

#    print(output)

#    images.insert(output)

    db_testing.client.close()

if __name__ == '__main__':
    main()
