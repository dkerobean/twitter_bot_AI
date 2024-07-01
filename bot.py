import tweepy
from dotenv import load_dotenv
import os
import logging
from openai import OpenAI

import random
import time

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

client = OpenAI(api_key=open_ai)


def generate_tweet(topic):
    prompt = f"Generate a relevant and interesting tweet about {topic}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert software \
                    developer, and you are trying to \
                    create a social presence on twitter"},
            {"role": "user", "content": prompt}
        ],
        )

    tweet = response.choices[0].message.content.strip()

    return tweet


def create_tweet(tweet):
    try:
        response = client.create_tweet(text=tweet)
        tweet_url = f"https://twitter.com/user/status/{response.data.id}"
        return tweet_url
    except Exception as e:
        log.error(f"Error creating tweet: {e}")
        raise SystemExit(f"Error creating tweet: {e}")

    return tweet_url


topics = ["MongoDb", "artificial intelligence", "Jenkins", "health", "python", "Javasccript", "Kubernetes"]


def main():
    topic = random.choice(topics)
    tweet = generate_tweet(topic)
    log.info("Tweet posted successfully")


if __name__ == "__main__":
    main()
