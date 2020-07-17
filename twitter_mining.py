import tweepy
import json
import string
from pymongo import MongoClient
import pandas as pd
import twitter_mining_functions
from datetime import datetime
from sqlalchemy import create_engine
import pymysql
from flask_sqlalchemy import SQLAlchemy
import creds

engine = create_engine(creds.sql_con, pool_pre_ping = True) #engine = create_engine("mysql+pymysql://ariel:password@192.168.56.10/fitness?charset=latin1", pool_pre_ping = True, encoding = 'latin1')
con = engine.connect()
#######################################################################
######Tweepy connection keys###########################################
consumer_key = creds.consumer_key
consumer_secret = creds.consumer_secret
access_token = creds.access_token
access_token_secret = creds.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
#######################################################################

mongo_entry_list = []
sql_entry_list = []

class SimpleListener(tweepy.StreamListener):

   def on_error(self, error_code):
       print('@on_error')
       print(error_code)
       if error_code == 420:
           return False

   def on_data(self, status):
        global entry_list
        # code to run each time you receive some data (direct message, delete, profile update, status,...)
        #fields_dict = {}
        tweet = json.loads(status)                                     #load all the different parameters that the tweet has in json format
        sec_tweet = twitter_mining_functions.lang_retweet_check(tweet) # doing the first filter of the tweet to make sure its language field is english, it isnt truncated(cut off) and is not a retweet. if all these pass return object else return false

        if sec_tweet != False:  #if the tweet is useable ie passed the first filter and didnt return false
            filtered_security_tweet_object = ({**twitter_mining_functions.set_general_field(sec_tweet)}) # make a dictionary of all the fields we want from the bigger json object
            keywords_list = twitter_mining_functions.filter_sec_data(filtered_security_tweet_object)         #make a list of the main words in the tweet, minus punctuation, links, @ mentions
            if keywords_list != None:
                security_tweet_data = (twitter_mining_functions.double_meaning_words_checking(keywords_list,tweet)) # checking for double meaning words
                security_tweet_data = twitter_mining_functions.cluster_removal(security_tweet_data)
            else:
                security_tweet_data = None

            if security_tweet_data != None:
                tweet_text = filtered_security_tweet_object["tweet_text"]
                tweet_created_at = filtered_security_tweet_object["tweet_created_at"]
                sent_score = twitter_mining_functions.sentiment_scores(tweet_text)
                datetime_object = datetime.strptime(tweet_created_at, "%a %b %d %H:%M:%S %z %Y")

                sql = "INSERT INTO security_tweet_data (sql_tweet_text, sql_platform, sql_sentiment, sql_datetime_object ) VALUES (%s,%s,%s,%s)"
                val = tweet_text, "twitter", sent_score, datetime_object
                con.execute(sql,val)

# initialize the stream
tweepy_stream = tweepy.Stream(auth=api.auth, listener=SimpleListener())
tweepy_stream.filter(track=['wolfrat','exodus','cybercrime','phishing','dos','botnet','xss','wannacry','heartbleed','ransomware','trojan','spyware','exploit','malware','mitm','petya','mirai','stuxnet','eternalblue','infosec','keylogger','spammer','rootkit','phreaking','conficker','worm','scammers','hacker','cybersecurity','notpetya',"locky","uiwix","samsam","RAT","APT","spamware","dns", "wolfrat","revil"])