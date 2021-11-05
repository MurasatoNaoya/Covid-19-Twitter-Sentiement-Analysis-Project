# The aim of this program is scrape data, or in this case, tweets from Twitter.
# In the aim of getting a better understanding of the impression or 'sentiment' users have of certain cryptocurrencies. 


# Import the appropriate libraries - 

import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import sys
import re

import matplotlib.pyplot as plt   # Here we used the 'as' keyword to create an alias for the module we want to import. 
plt.style.use(seaborn-bright) # What style use choose does not matter, I have chosen 'seaborn-bright'; but you could have anything; e.g fivethirtyeight. 
import pandas as pd
import numpy as np



# Twitter API credentials - consumer API key, the consumer API secret, access token and access token secret. 

Oauth1_consumer_key = "AVudPPS0nePRUgOAWNOOyQZB4"
oauth1_consumer_secret = "KeATWWKKjZYcJr9OExhMq1t2fKH35j5Z8hmPNwKOIg3EhwBHKv"
oauth1_access_token = "1454520951136194564-dXDgv1tI9EeRvMysAI1xpJxjpDW9hg"
oauth1_access_token_secret = "ByCcAp1zRDt2AuGCsu4astZtp78dBYDqjxQfh7G0dia7N"



# Creating an instance of tweepy's .AuthHandler class - 

authentication = tweepy.OAuthHandler(Oauth1_consumer_key, oauth1_consumer_secret)

# Setting the access token and access token secret - 

authentication.set_access_token(oauth1_access_token, oauth1_access_token_secret)

# Creating the API object, specific to our authentication information - 

api = tweepy.API(authentication, wait_on_rate_limit= True)



# Now that we have authentication, we can now use the tweepy and TextBlob modules to retrieve Tweets and discern intention parameters, respectively.

# Sentiment analysis - 








