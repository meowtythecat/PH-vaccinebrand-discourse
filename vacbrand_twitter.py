from pandas import date_range
import tweepy
import twitter_credentials as t
import datetime

#Authorization to mine Tweets
client = tweepy.Client(bearer_token=t.bearer_token)

#Assigning values for the parameters
query = '[vacbrand] lang:tl -is:retweet'
    #[vacbrand] is subject to change based on the vaccine brand to be searched for
start_time= '2021-01-01T12:00:01Z'
end_time= '2021-12-31T11:59:59Z'
    #Values of start_time and end_time are subject to changes based on desired timeframe

#Searching 100 Tweets with the established values of the parameters
response = client.search_all_tweets(query=query, start_time=start_time, end_time=end_time, max_results=100)
    #number assigned to max_results is subject to change based on desired number of Tweets to mine

#Writing mined Tweets on a text file
with open("vacbrand_[vacbrand]_2021.txt",'w', encoding='utf-8') as vaccine_file:
    for tweet in response:
        vaccine_file.write(str(tweet))
        vaccine_file.write('\n')