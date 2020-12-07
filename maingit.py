import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text.encode('utf-8'))


csvFile = open('file-name_2', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "bts"      # enter your words
new_search = search_words + " -filter:retweets"
COUNT = 0
HASHTAGS = ""


for tweet in tweepy.Cursor(api.search,q=new_search,count=100,lang="en",since_id=0, exclude='retweets').items():
    COUNT = COUNT + 1
    if(COUNT !=10):
     
        if(tweet.user.location.encode('utf-8')!="b''" or tweet.user.location.encode('utf-8')!="b'' "):
            print(tweet.user.location.encode('utf-8'))
        # for i in tweet.entities.hashtags:
        #     HASHTAGS += str(i) + ","
        if(tweet.user.location!="''"):
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8'), tweet.user.name.encode('utf-8')])
    else:
        exit()