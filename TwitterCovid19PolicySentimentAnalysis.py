# The aim of this program is scrape data, or in this case, tweets from Twitter.
# In the aim of getting a better understanding of the impression or 'sentiment' users have of the implementation of restrictive Covid-19 policies. 


# Import the appropriate libraries - 

import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import sys
import re

import matplotlib.pyplot as plt   # Here we used the 'as' keyword to create an alias for the module we want to import. 
plt.style.use(seaborn-bright) # What style I;ve chosen doesn't really matter, I have chosen 'seaborn-bright', but you could have anything. E.g fivethirtyeight. 
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

# Creating the API object, that accounts for our authentication information - 
# The Twitter API has a rate limit of 900 requests per 15 minutes, it would return anything above this amount an error. 
# The 'wait_on_rate_limit' parameter asks whether or not automatically wait for rate limits to replenish, in this case we set it to 'True' to avoid errors.  

api = tweepy.API(authentication, wait_on_rate_limit= True)




# Now that we have authentication, we can now use the tweepy and TextBlob modules to retrieve Tweets and discern intention parameters, respectively.


# The below self defined function is to be used later to calculate the percentage of positive, negative and neutral Tweets we have in our sample.
# The 'part' paramater representing whatever category of sentiment was want to look at and the 'whole' parameter representing our total number of Tweets, NoOfTweets. 

def percentage(part,whole):
   return 100 * float(part)/float(whole)
 

# Recording the keyword(s) and number of Tweets being considered - the input() may not be called unless you are using an interactive interface like Juypter. 
  
keyword = input("Please enter keyword or hashtag to search: ")
NoOfTweets = int(input ("Please enter how many tweets to analyse: "))


# Using tweepy to search and collect Tweets based on the predefined keyword(s) and number of Tweets we want to analyse - 

tweets = tweepy.Cursor(api.search, q = keyword).items(NoOfTweets) # [Explain the usage of these function unique to tweepy]

# Below are neutral lists, where the analysed tweets will be appended to - 
positive = 0
positive = 0
neutral = 0

polarity = 0

tweet_list = []
neutral_list = []
negative_list = []
positive_list = []



for tweet in tweets: # Essentially, for every Tweet in the list of int(NoOfTweets) Tweets that our API has scraped.. 
   tweet_list.append(tweet.text)

 
   # We can now make our first 'TextBlob' using the TextBlob module, (Refer to this difficulty in the README file, linking the TextBlob Documentation.)
   # This is in the for loop, so each individual tweet will be treated as a TextBlob to be processed. 
   analysis = TextBlob(tweet.text)




# It is important to note that there are specific pieces of terminology unique to each library. 
# In the context of TextBlob, polarity indicates is a float in the range [-1-1], where 1 indicates a purely positive statement and -1 and purely negative statement.












