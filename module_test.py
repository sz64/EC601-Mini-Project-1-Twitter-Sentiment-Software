import tweepy
import tweet_puller

scr_name = input('Twitter username: ');
n_tweets = int(input('How many tweets would you like to analyze? '))
tweets = [];

tweets = tweet_puller.tweet_pull(scr_name, n_tweets);
