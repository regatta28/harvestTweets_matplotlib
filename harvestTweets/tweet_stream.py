from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'MT6KMuqBegbfAxU8ZeGBxmIG5'
CONSUMER_SECRET = 'VdRlAQxTqM1oWNDuW9etzWzmZIUwgJRA02REDyzzmRHYSYu72z'
OAUTH_TOKEN = '3700798289-PBuFNcTWQwNBVAmk2IghTYPnLosmPxbCshLOE3n'
OAUTH_TOKEN_SECRET = 'oQJrDYAHYOA4PqBia6a0uWHBikmwZfb2a975FpDYDrscf'

keyword_list = ['python', 'java', 'c#', 'ruby']  # track list


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)