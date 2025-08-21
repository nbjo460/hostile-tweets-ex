import os
import json
from bson import json_util
from pymongo import MongoClient

def connection(func):
    def wrapper(dal, *args, **kwargs):
        client = None
        try:
            client = MongoClient(dal.URI)
            print("opened")
            db = client[dal.DBNAME]
            collection = db[dal.COLLECTION]
            result = func(dal, collection, *args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            try:
                client.close()
                print("closed")
            except Exception as e:
                print("Can't close ", e)

    return wrapper

class Dal:
    """
    Object that make connection with mongodb server, and get data.
    """
    def __init__(self):
        self.URI = os.getenv("HOST", "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
        self.USER = os.getenv("USER", "IRGC")
        self.DBNAME = os.getenv("DBNAME", "IranMalDB")
        self.COLLECTION = os.getenv("COLLECTION", "tweets")
        self.PASSWORD = os.getenv("PASSWORD", "iraniraniran")

    @connection
    def get_tweets(self, collection):
        """
        Ruturns list of all tweets.
        :return: list
        """
        print("Fetching tweets.")
        tweets = list(collection.find())
        result = json.loads(json_util.dumps(tweets))
        print(f"{tweets.count()} tweets loaded.")
        return result
d = Dal()
print(d.get_tweets())