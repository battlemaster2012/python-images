from pymongo import MongoClient

mongolab_uri = "mongodb://<heroku_j3jxlf8g>:<18@!YoQu@FQluia>@ds037215.mongolab.com:37215/heroku_j3jxlf8g"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()
print db.collection_names()
