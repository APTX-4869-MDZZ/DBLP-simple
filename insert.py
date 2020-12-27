import pymongo
import json
import time

client = pymongo.MongoClient(host='10.176.64.55', port=37017)
db = client['dblp']
col = db['info']

with open('info.json') as f:
    data = json.load(f)
    # print(data)
    # for x in data:
    # col.insert_one(x)
    start = time.time()
    col.insert_many(data)
    end = time.time()
    print('time: ', end-start)
