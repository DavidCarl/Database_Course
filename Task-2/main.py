import pymongo
from pymongo import MongoClient
from bson.son import SON
from pprint import pprint


client = MongoClient()
db = client.tweet
training = db.training

def fprint(data):
    for each in data:
        pprint(each)

def question1():
    print('Question 1')
    data = training.distinct('user')
    print('Amount of unique users:', len(data))

def question2():
    print('\nQuestion 2')
    pipeline = [
        {"$match": {"text": {"$regex": "@"}}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    pprint(list(training.aggregate(pipeline)))

def question3():
    print('\nQuestion 3')
    print('Got no answer for this question!')

def question4():
    print('\nQuestion 4')
    pipeline = [
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    pprint(list(training.aggregate(pipeline, session=None)))


def question5():
    print('\nQuestion 5')
    print('Top 5 negative:')
    pipeline = [
        {"$match": {"polarity": 0}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 5}
    ]
    rs = training.aggregate(pipeline)
    fprint(rs)
    print('\n')

    print('Top 5 positive:')
    pipeline = [
        {"$match": {"polarity": 4}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 5}
    ]
    rs = training.aggregate(pipeline)
    fprint(rs)

    
question1()
question2()
question3()
question4()
question5()