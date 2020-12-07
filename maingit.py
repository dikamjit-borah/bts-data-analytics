import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import time
import random

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text.encode('utf-8'))


csvFile = open('1825 01-12 KEY=KPOPorBTS.csv', 'a', newline='')
csvFile2 = open('bts_world2.csv', 'a', newline='')
csvWriter = csv.writer(csvFile)
csvWriter2 = csv.writer(csvFile2)

search_words = "kpop OR bts"   #grumpy OR cat OR #meme  
new_search = search_words + " -filter:retweets"
count_country = 0
print("Fetching...")
substring = "India"

#tweets = api.search(keyword, count=10, lang='en', exclude='retweets',tweet_mode='extended')

count_total =0
for tweet in tweepy.Cursor(api.search,q=new_search,geocode="20.5937,78.9629,2933km",count=100,lang="en",since_id=0, exclude='retweets', geo_enabled=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():
    if(count_total<20000):
        count_total = count_total + 1
        print("####################################")
        print("{} -> {}".format(count_total, tweet.id_str))
        #time.sleep(random.randint(2, 8))
        T_ID=tweet.id_str
        T_TEXT = tweet.text.encode('utf-8')
        T_DATETIME = tweet.created_at
        T_USERNAME = tweet.user.name.encode('utf-8')
        T_SCREENNAME = tweet.user.screen_name.encode('utf-8')
        T_LOCATION = tweet.user.location.encode('utf-8')
        T_FOLLOWERS = tweet.user.followers_count
        T_FRIENDS = tweet.user.friends_count
        T_STATUSES = tweet.user.statuses_count
        T_HASHTAGS = []
        T_MENTIONS = []
        try:
            for i in range(3):
                T_HASHTAGS.append(tweet.entities["hashtags"][i]["text"])
        except:
            pass
           
        try:
            for i in range(3):
                T_MENTIONS.append(tweet.entities["user_mentions"][i]["screen_name"].encode('utf-8'))
        except:
            pass

        if(count_country<10000):
            #print(tweet)
            #if(tweet.user.location.startswith("b''", 0, 3)==False):
            #print(count_country)
            try:
                print("Writing in bts_india")    
                csvWriter.writerow([T_ID, T_DATETIME, T_TEXT, T_HASHTAGS, T_MENTIONS, T_LOCATION, T_USERNAME, T_SCREENNAME, T_FOLLOWERS, T_FRIENDS, T_STATUSES ])
                count_country = count_country + 1
                print("bts_india comments = ",count_country)
               
            except:
                pass
            
        else:
            exit()
        print("####################################")
        print("")
    else:
        exit()

