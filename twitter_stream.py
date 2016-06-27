from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
import sentiment_mod as s
import MySQLdb
import time
import json
import sys
import os
import io

# consumer key, consumer secret, access token, access secret.
ckey = "....................................."
csecret = "....................................."
atoken = "....................................."
asecret = "....................................."

from twitterapistuff import *

start_time = time.time() #grabs the system time
keyword_list = ['stupid'] #track list

#Listener Class Override
class listener(StreamListener):

	def __init__(self, start_time, time_limit=90):

		self.time = start_time
		self.limit = time_limit
		#self.tweet_data = []
		#self.saveFile = io.open('scripts/raw_tweets.json', 'w', encoding='utf-8')
		self.saveFile = open('scripts/twitter_out.txt', 'w')
		#self.saveFile.write(u'[\n')

	def on_data(self, data):

		#saveFile = io.open('scripts/raw_tweets.json', 'w', encoding='utf-8')

		while (True):

			try:
				all_data = json.loads(data)
				tweet = all_data["text"]
				print tweet
				#self.saveFile.write(data)

				self.saveFile = open('scripts/twitter_out.txt', 'a')
				self.saveFile.write(str(s.sentiment(tweet)) + "\n")
				self.saveFile.close()

				return True

			except BaseException, e:
				print 'failed,', str(e), '\n'
				time.sleep(5)
				pass

		'''saveFile = io.open('scripts/raw_tweets.json', 'w', encoding='utf-8')
								saveFile.write(u'[\n')
								saveFile.write(','.join(self.tweet_data))'''
		#self.saveFile.write(u'\n]')
		#self.saveFile.close()
		exit()

	def on_error(self, status):

		print statuses

auth = OAuthHandler(ckey, csecret) #OAuth object
auth.set_access_token(atoken, asecret)


twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object
