# Here is last weeks assignment

I havent touched the queries or the results from last week so its as new.

### Question 1
#### Query
```
    data = training.distinct('user')
    print('Amount of unique users:', len(data))
```
#### Answer
```
Amount of unique users: 659774
```

### Question 2
#### Query
```
    pipeline = [
        {"$match": {"text": {"$regex": "@"}}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    pprint(list(training.aggregate(pipeline)))
```
#### Answer
```
[{'_id': 'lost_dog', 'count': 549},
 {'_id': 'tweetpet', 'count': 310},
 {'_id': 'VioletsCRUK', 'count': 251},
 {'_id': 'what_bugs_u', 'count': 246},
 {'_id': 'tsarnick', 'count': 245},
 {'_id': 'SallytheShizzle', 'count': 229},
 {'_id': 'mcraddictal', 'count': 217},
 {'_id': 'Karen230683', 'count': 216},
 {'_id': 'keza34', 'count': 211},
 {'_id': 'TraceyHewins', 'count': 202}]
```

### Query 3
#### Query
```
    print('Got no answer for this question!')
```
#### Answer
```
Got no answer for this question!
```

### Query 4
#### Query
```
    pipeline = [
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    pprint(list(training.aggregate(pipeline, session=None)))
```
#### Answer
```
[{'_id': 'lost_dog', 'count': 549},
 {'_id': 'webwoke', 'count': 345},
 {'_id': 'tweetpet', 'count': 310},
 {'_id': 'SallytheShizzle', 'count': 281},
 {'_id': 'VioletsCRUK', 'count': 279},
 {'_id': 'mcraddictal', 'count': 276},
 {'_id': 'tsarnick', 'count': 248},
 {'_id': 'what_bugs_u', 'count': 246},
 {'_id': 'Karen230683', 'count': 238},
 {'_id': 'DarkPiano', 'count': 236}]

```

### Query 5
#### Query
```
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
```
#### Answer

```
Top 5 negative:
{'_id': 'lost_dog', 'count': 549}
{'_id': 'tweetpet', 'count': 310}
{'_id': 'webwoke', 'count': 264}
{'_id': 'mcraddictal', 'count': 210}
{'_id': 'wowlew', 'count': 210}

Top 5 positive:
{'_id': 'what_bugs_u', 'count': 246}
{'_id': 'DarkPiano', 'count': 231}
{'_id': 'VioletsCRUK', 'count': 218}
{'_id': 'tsarnick', 'count': 212}
{'_id': 'keza34', 'count': 211}
```