import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'MT6KMuqBegbfAxU8ZeGBxmIG5'
CONSUMER_SECRET = 'VdRlAQxTqM1oWNDuW9etzWzmZIUwgJRA02REDyzzmRHYSYu72z'
OAUTH_TOKEN = '3700798289-PBuFNcTWQwNBVAmk2IghTYPnLosmPxbCshLOE3n'
OAUTH_TOKEN_SECRET = 'oQJrDYAHYOA4PqBia6a0uWHBikmwZfb2a975FpDYDrscf'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10  # the min amount of times a status is retweeted to gain entry to our list.
# reset this value to suit your own tests

pop_tweets = [status
              for status in results
              if status._json['retweet_count'] > min_retweets]

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print table