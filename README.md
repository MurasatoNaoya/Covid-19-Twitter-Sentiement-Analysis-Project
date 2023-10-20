# Covid-19 Twitter Sentiement Analysis Project README


This Python script is a versatile tool for performing sentiment analysis on a collection of tweets obtained from Twitter.
It combines the power of several essential libraries and modules to gather, clean, and analyze Twitter data that contain
specific keywords, within specified locations. The scraped tweets are then analysed using the TextBlob sentiment analysis
library, where their polarity scorces and subjectivity scores are then returned. 

# Sentiment Analysis of Tweets from Twitter

## Usage

1. **Running the Script**: Execute the script in your Python environment of choice.

2. **Input Keyword and Number of Tweets**: The script will prompt you to provide a keyword or phrase for focusing your search. You'll also specify the number of tweets you want to analyze.

3. **Twitter Data Retrieval**: The script uses the Twitter Scrape Module to collect tweets containing the specified keyword. It further filters tweets geolocated in the "United Kingdom" and posted within a specific date range.

4. **Data Organization**: Retrieved tweets are organized in a Pandas DataFrame, allowing for easy management and analysis. The initial rows of the DataFrame are displayed.

5. **Tweet Cleaning**: The script proceeds to clean the tweets, removing mentions, hashtags, retweets, and hyperlinks, which can introduce noise into the sentiment analysis.

6. **Sentiment Analysis Methods**:
    - **VADER Sentiment Analysis**: The script employs the VADER sentiment analysis method to determine the sentiment of each tweet. This method provides scores for negative, neutral, and positive sentiment, as well as a compound score.
    - **TextBlob Sentiment Analysis**: A second method, TextBlob, is used for sentiment analysis. It calculates subjectivity and polarity scores for each tweet.

7. **Displaying Sentiment Results**: The sentiment analysis results are presented in the terminal, including the compound sentiment score for each tweet. You'll also get an overview of the proportions of positive, negative, and neutral tweets.

8. **Aggregate Sentiment Scores**: The script calculates aggregate sentiment scores, including overall subjectivity and polarity. It also computes a true compound score based on the average of the compound scores for all tweets.

9. **Validating Results**: The script verifies the validity of the sentiment proportions by summing the percentages of positive, negative, and neutral tweets. This ensures that they add up to 100%.
