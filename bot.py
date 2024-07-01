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
twitter_client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

openai_client = OpenAI(api_key=open_ai)


def generate_tweet(topic):
    prompt = f"Generate a relevant and interesting tweet about {topic}"
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are an expert software developer, and you are trying to create a social presence on Twitter"},
            {"role": "user", "content": prompt}
        ],
    )

    tweet = response.choices[0].message.content.strip()

    return tweet


def create_tweet(tweet):
    try:
        response = twitter_client.create_tweet(text=tweet)
        tweet_url = f"https://twitter.com/user/status/{response.data['id']}"
        return tweet_url
    except Exception as e:
        log.error(f"Error creating tweet: {e}")
        raise SystemExit(f"Error creating tweet: {e}")


topics = ["MongoDB", "artificial intelligence", "Jenkins", "health", "python", "JavaScript", "Kubernetes"]


def main():
    topic = random.choice(topics)
    tweet = generate_tweet(topic)
    tweet_url = create_tweet(tweet)
    log.info(f"Tweet posted successfully: {tweet_url}")


if __name__ == "__main__":
    main()
