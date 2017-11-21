import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 
CONSUMER_SECRET = '
OAUTH_TOKEN = '
OAUTH_TOKEN_SECRET = '

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
