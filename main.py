import tweepy
from api_keys import keys


class tweeter:
    def __init__(self):
        api_key = keys['api_key']
        api_secret = keys['api_secret']
        access_token = keys['access_token']
        access_secret = keys['access_secret']

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth)

    def convert_response(self, response):
        converted = [{
            "id": tweet.id,
            "title": tweet.title,
            "text": tweet.full_text
        } for tweet in response]

        return converted

    def user_tweets(self, user, limit):
        response = self.api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
        converted_response = self.convert_response(response)

        return converted_response

    def find_hashtags(self, tweet):
        werbs = tweet.split()
        hashtags = [werb for werb in werbs if werb[0] == '#']

        return hashtags

    def find_tags(self, tweet):
        werbs = tweet.split()
        hashtags = [werb for werb in werbs if werb[0] == '@']

        return hashtags
