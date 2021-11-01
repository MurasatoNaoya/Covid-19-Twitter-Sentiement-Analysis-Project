# The aim of this program is scrape data, or in this case, tweets from Twitter.
# In the aim of getting a better understanding of the impression or 'sentiment' users have of certain cryptocurrencies. 


# Import the appropriate libraries 
# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt   # Here we used the 'as' keyword to create an alias for the module we want to import. 
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


# Next we will need the consumer API key, the consumer API secret, access token and access token secret. 
# I rec

consumerAPIKey = AVudPPS0nePRUgOAWNOOyQZB4
consumerAPISecret = KeATWWKKjZYcJr9OExhMq1t2fKH35j5Z8hmPNwKOIg3EhwBHKv
accessToken = 1454520951136194564-dXDgv1tI9EeRvMysAI1xpJxjpDW9hg
accessTokenSecret =  ByCcAp1zRDt2AuGCsu4astZtp78dBYDqjxQfh7G0dia7N

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)



