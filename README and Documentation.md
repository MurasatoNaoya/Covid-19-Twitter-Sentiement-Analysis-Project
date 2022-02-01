# Sentiment-Anlysis-Project-


This project aims to scrape data, specifically Tweets, to gauge the opinions and sentiments of users regarding a particular subject. 
It is important to note that although keyword(s) in this project will be focused on blockchain and crytocurreny terminology, it can be easily changed to other keywords. 

Firstly, we would need to get authentication to use Twitter's API. tweepy handles two different types of authentication, OAuth 1.0a and OAuth 2.0, both of which are handled by tweepy's .AuthHandler class. 

The raw data will be collected by using the Twitter API to scrape Tweets from the Twitter platform. 
Then, by using python libraires associated with textual processing and sentiment analysis, we will be able to discerne the proportion of positive, negative and neutral sentiments in our sample. 







PROBLEMS AND SETBACKS - 


29/10/2021- 



30/10/2021 - In order to actually have access to Twitter's API and eventually use it to scrape for Tweets, I needed to apply for a Twitter Developer account. Without such an account, I would not have access to the the consumer API key, the consumer API secret, access token and access token secret; all necessary to authenticate my app. Also, although not much of a problem, I had to ensure I had 'Read and Write' permission so I could read and post Tweets and profile information. 


1/2/2022 - One of the most important parts of any project focused on sentiment analysis, is of course the means of sentiment analysis. The two primary Python libraries that I will be using for such analysis will be TextBlob and Vader, the later seems to handle more formal language, while the latter seems to be more strongly suited to slang, emojies and casual language. Although social media platforms like Twitter might be more casual in general, meaning VADER might be a more suitable choice. However, consdiering the seriousness of the topic I am investigiating, TextBlob will likely be very useful also. In the end, I've decided to use both in quantifying polarity and processing Tweets. 
