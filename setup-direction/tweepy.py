# Importing Tweepy
import tweepy

# Credentials
api_key = "wGyRdDSfNb9IYbJI6OeEe0Sth"
api_secret = "Zuw0hb97WEwhvrLXc4IVbmaFP9bNn1m1TNMoGb4F7kCrIEftxN"
bearer_token = r"Zuw0hb97WEwhvrLXc4IVbmaFP9bNn1m1TNMoGb4F7kCrIEftxN"
access_token = "d1R2QU90TFVkMmVZblM1TWd0SE06MTpjaQ"
access_token_secret = "-xkRJlgaWZN3B86N7_rFKKs3i5dll2xl5QbE4Q5LLty7Rm9rlL"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Creating a tweet to test the bot
client.create_tweet(text="Hello World")