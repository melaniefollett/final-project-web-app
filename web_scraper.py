import requests
import json
import csv
import time
import datetime

# Scrape Reddit posts
def commentScraper(username):
    
    reddit_comments = []

    data = getPushshiftData(username)

    for comment in data:
        reddit_comments.append(comment['body'])
        #data = getPushshiftData(username)

    # obj = {}
    # obj['username'] = username
    # obj['comments'] = reddit_comments

    #print(reddit_comments)
    return(reddit_comments)

    # with open("comments.json", "w") as jsonFile:
    #     json.dump(obj, jsonFile)

def getPushshiftData(username):
    url = f"https://api.pushshift.io/reddit/search/comment/?author={username}&sort=desc&size=50"
    r = requests.get(url)
    data = json.loads(r.text)
    return(data['data'])

    #comments = getPushshiftData(username)
    #print(comments)

#username = input("Input username:")
#comment_scrape(username)