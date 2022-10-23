import tweepy

from settings import app_settings


class TwitterPoster:

    def __init__(self):
        self.consumer_key = app_settings.consumer_key
        self.consumer_secret = app_settings.consumer_secret
        self.access_token = app_settings.access_token
        self.access_token_secret = app_settings.access_token_secret

    def post_content(self, content_to_post: str):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        # Create API object
        api = tweepy.API(auth)
        # Create a tweet
        api.update_status(content_to_post)


twitter_poster = TwitterPoster()
