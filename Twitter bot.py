#library to access twitter api
#pip3 install tweepy

import tweepy
import time #built in
#verify our account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

#print(user.name) --> all in the library
#print(user.screen_name)
#print(user.followers_count)

#generous bot

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300) #mili seconds



search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.retweet()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	#if follower.name == 'username':
		#follower.follow()
		#break #stop looping
	#print(follower.name) #problem heating the api


	#follow back copy that user name



