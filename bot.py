import tweepy
from dotenv import load_dotenv
import os
import logging
import openai

# Set up logging
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='twitter_bot.log', format=LOG_FORMAT, level=logging.DEBUG)
log = logging.getLogger()

# Load environment variables from .env file
load_dotenv()

# credentials from environment variables
bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
open_ai = os.getenv('OPEN_AI')

# Authentication
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


def create_tweet(tweet):
    try:
        response = client.create_tweet(text=tweet)
        tweet_url = f"https://twitter.com/user/status/{response.data['id']}"
        log.info(f"Tweet posted successfully: {tweet_url}")
        return tweet_url
    except tweepy.TweepError as e:
        log.error(f"Error creating tweet: {e}")
        raise SystemExit(f"Error creating tweet: {e}")
