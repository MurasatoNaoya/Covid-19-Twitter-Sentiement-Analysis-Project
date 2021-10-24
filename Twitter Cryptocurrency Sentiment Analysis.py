# The aim of this program is scrape data, or in this case, tweets from Twitter.
# In the aim of getting a better understanding of the impression or 'sentiment' users have of certain cryptocurrencies. 



# Import the appropriate libraries 

import tweepy 
from textblob import TextBlob 
import pandas as pd 
import numpy as np 
import re 
import matplotlib.pyplot as plt 
plt.style.use('seaborn')  # Plotting style is preference here, anything from default to fivethirtyeight is fine. 


