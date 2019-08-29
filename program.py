import tweepy
from textblob import TextBlob
# keys and tokens from the Twitter Dev Console
consumer_key = ‘XXXXXXXXXXXXXXXXXXXXXXXX’
consumer_secret = ‘XXXXXXXXXXXXXXXXXXXXXXXXXXXX’
access_token = ‘XXXXXXXXXXXXXXXXXXXXXXXXXXXX’
access_token_secret = ‘XXXXXXXXXXXXXXXXXXXXXXXXX’
# attempt authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)
tweets=api.search(‘Annamalai’)
for t in tweets:
analysis = TextBlob(t.text)
if analysis.sentiment.polarity > 0:
print(‘Happy and Excited !!’)
elif analysis.sentiment.polarity == 0:
print(‘Unbiased’)
else:
print(‘Sad’)
