import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'MT6KMuqBegbfAxU8ZeGBxmIG5'
CONSUMER_SECRET = 'VdRlAQxTqM1oWNDuW9etzWzmZIUwgJRA02REDyzzmRHYSYu72z'
OAUTH_TOKEN = '3700798289-PBuFNcTWQwNBVAmk2IghTYPnLosmPxbCshLOE3n'
OAUTH_TOKEN_SECRET = 'oQJrDYAHYOA4PqBia6a0uWHBikmwZfb2a975FpDYDrscf'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@madonna')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print status.text