import tweepy
from datetime import datetime, timedelta
import csv
import json
import os
# import sqlite3
# from sqlite3 import Error
from dotenv import load_dotenv
load_dotenv()
# from textblob import Blobber
# from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer
import re
# from db.index import upsert, getTweets


RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

class Tweet:

    def __init__(self,
        id,
        username,
        user_screenname,
        text,
        created_at,
        retweeted,
        retweet_count,
        favourite_count,
        place_fullname,
        user_followers_count,
        user_statuses_count,
        user_location,
        hashtag):

        self.id = id
        self.username = username
        self.user_screenname = user_screenname
        self.text = text
        self.created_at = created_at
        self.retweeted = retweeted
        self.retweet_count = retweet_count
        self.favourite_count = favourite_count
        self.place_fullname = place_fullname
        self.user_followers_count = user_followers_count
        self.user_statuses_count = user_statuses_count
        self.hashtag = hashtag

        if (len(user_location) > 0):
            self.user_location = user_location[0]
        else:
            self.user_location = ""

        self.score = None
        self.sentimental = None
        self.subjectivity = None

class twitterSearch():

    def __init__(self):
        self.authenticate()

    def authenticate(self):        
        consumerKey = os.getenv("API_KEY")
        consumerSecret = os.getenv("API_SECRET")
        accessToken = os.getenv("ACCESS_TOKEN")
        accessSecret = os.getenv("ACCESS_SECRET")

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessSecret)
        self.api  = tweepy.API(auth,
                            wait_on_rate_limit = True,
                            wait_on_rate_limit_notify = True)

    def setKey(self):
        #self.key = '(sampleTermOne AND sampleTermTwo) OR sampleTermThree -filter:retweets'
        self.runName = 'mySearch'
        self.dateSince = '2019-03-13'
        self.dateUntil = '2019-03-19'
        self.yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        self.today = datetime.strftime(datetime.now(), '%Y-%m-%d')
       
    def searchTwitter(self, word):
        items = tweepy.Cursor(self.api.search,
                           q = word + ' -filter:retweets',
                           rpp=100,
                           result_type='recent',
                           include_entities=True,
                           lang='en').items(20)

        #items number specified for testing
        tweets = []
        for status in items:
            tweet = status._json
            try:
                place = tweet["place"]["full_name"]
            except:
                place = None

           
            formattedTweet = Tweet(tweet["id_str"],
                                tweet["user"]["name"],
                                tweet["user"]["screen_name"],
                                tweet["text"],
                                tweet["created_at"], 
                                tweet["retweeted"],
                                tweet["retweet_count"],
                                tweet["favorite_count"],
                                place, 
                                tweet["user"]["followers_count"],
                                tweet["user"]["statuses_count"],
                                tweet["user"]["location"],
                                word
                            )
            
            tweets.append(formattedTweet.__dict__)
        
        print('Number of Tweets retrived: ', len(tweets))
        return tweets

    def exportToJson(self, tweets, filename):
        with open(filename + '.json', 'w') as f:
            json.dump(tweets, f)  
    
    def getAllTweets(self):
        return getTweets()

    def to_utf8(self, lst):
        newList = []
        for elem in lst:
            if(elem is not None):
               newList.append(elem.encode('utf-8')) 

        return newList

    def csvCreate(self, data):
       
        with open('tweetNew.csv', 'w') as writeFile:
            # fields = [ "id",
            #     "username",
            #     "user_screenname",
            #     "text",
            #     "created_at",
            #     "retweeted",
            #     "retweet_count",
            #     "favourite_count",
            #     "place_fullname", 
            #     "user_followers_count",
            #     "user_statuses_count",
            #     "user_location",
            #     "score",
            #     "sentimental",
            #     "subjectivity"]

            fields = [ "user_screenname",
            "created_at",
            "sentiment",
            "sent_score",
            "text",
            "retweet_count",
            "favourite_count"]
            writer = csv.writer(writeFile)
            writer.writerow(fields)
            
            for row in data:
                writer.writerow(self.to_utf8(row))


        print("writing completed")
        writeFile.close()

    def sentiment(self, tweet):
        q = "select id, text from tweet where sentiment is null"

        tb = Blobber(analyzer=NaiveBayesAnalyzer())
        blob = tb(tweet.text)
        # tweet.score = blob.sentiment.polarity
        # tweet.subjectivity = blob.sentiment.subjectivity

        if blob.sentiment.classification == 'pos':
            tweet.sentimental = 'positive'
            tweet.score = blob.sentiment.p_pos
            self.factoredTweets['positive'].append(json.dumps(tweet.__dict__))
        elif  blob.sentiment.classification == 'neg':
            tweet.sentimental = 'negative'
            tweet.score = blob.sentiment.p_neg*(-1)
            self.factoredTweets['negative'].append(json.dumps(tweet.__dict__))
        else:
            tweet.sentimental = 'neutral'
            tweet.score = 0
            self.factoredTweets['neutral'].append(json.dumps(tweet.__dict__))

        return tweet
            