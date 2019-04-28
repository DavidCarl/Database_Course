# Task-12

### Made by David Carl & Tjalfe Møller
### www.dcarl.me

## Setup

First you need to get a container running with Neo4j, we used the teachers instructions on how to do it, we did it this way 
```
docker run \
    -d --name neo4j \
    --rm \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --env NEO4J_AUTH=neo4j/fancy!99Doorknob \
    neo4j
```

Then we need to download and import our data. First we download our data with this command `wget https://github.com/datsoftlyngby/soft2019spring-databases/raw/master/data/some2016UKgeotweets.csv.zip` 

After that we unzip it with the following command `unzip some2016UKgeotweets.csv.zip` 

and at last we make a docker cp like this. `docker cp some2016UKgeotweets.csv neo4j:/var/lib/neo4j/import/ some2016UKgeotweets.csv`

## Assignment 1

We used the following query to make assignment 1, we butchered some from the teachers example code and made it fit our purpose. We also included this string `USING PERIODIC COMMIT 500`, because without it our query crashed due to memory limit.

Our query is the following:
```
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "file:///some2016UKgeotweets.csv" AS row 
    FIELDTERMINATOR ";"
CREATE (tweet:Tweet {
    username: row.`User Name`,
    nickname: row.Nickname,
    location: row.`Place (as appears on Bio)`,
    lat: row.Latitude,
    long: row.Longitude,
    content: row.`Tweet content`,
    mentions: extract( m in 
                filter(m in split(row.`Tweet content`," ") where m starts with "@" and size(m) > 1) 
                | right(m,size(m)-1))
})
```

## Assignment 2

Question 1:

We only creates tweeters from our mention list since there are no reason to create users that have no use. At the same time we also creates our relationship since we tried a different method, where we did it in 2 steps, and found this way of doing it the fastest.

```
MATCH(tweet:Tweet)
UNWIND tweet.mentions AS username
WITH username, tweet
WHERE username <> ""
CREATE (tweeter:Tweeter {name:username})
CREATE (tweet)-[:MENTIONS]->(tweeter)
```

Question 2:

Here we created releationship between people who have tweeted togheter.

```
MATCH(tweeter:Tweeter)
WITH tweeter
MATCH(tweet:Tweet {username: tweeter.name})
CREATE (tweeter)-[:TWEETED]->(tweet)
```

## Assignment 3

We failed to come up with a solution to this assignment. We had a general idea, but we kept running into infinite loops (or us that was way to impatient to wait).
