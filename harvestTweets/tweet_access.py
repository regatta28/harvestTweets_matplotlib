import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'MT6KMuqBegbfAxU8ZeGBxmIG5'
CONSUMER_SECRET = 'VdRlAQxTqM1oWNDuW9etzWzmZIUwgJRA02REDyzzmRHYSYu72z'
OAUTH_TOKEN = '3700798289-PBuFNcTWQwNBVAmk2IghTYPnLosmPxbCshLOE3n'
OAUTH_TOKEN_SECRET = 'oQJrDYAHYOA4PqBia6a0uWHBikmwZfb2a975FpDYDrscf'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [word
         for text in status_texts
         for word in text.split()]

for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table


def get_lexical_diversity(items):
    return 1.0 * len(set(items)) / len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0 * total_words / len(tweets)


print "Average words: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)