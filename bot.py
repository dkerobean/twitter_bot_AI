import tweepy
from dotenv import load_dotenv
import os
import logging

# Set up logging
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='twitter_bot.log', format=LOG_FORMAT, level=logging.DEBUG)
log = logging.getLogger()

# Load environment variables from .env file
load_dotenv()

# Your Twitter API credentials from environment variables
bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
log.info("Authenticated with Twitter as user")

response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)
print(f"https://twitter.com/user/status/{response.data['id']}")
