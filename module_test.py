import tweepy
import tweet_puller
import google_sentiments

scr_name = input('Twitter username: ');
n_tweets = int(input('How many tweets would you like to analyze? '))
tweets = [];

tweets = tweet_puller.tweet_pull(scr_name, n_tweets);

sentiments_list = [];

for n in tweets:
	sentiments_list.append(google_sentiments.get_sentiment(n));
	print(google_sentiments.get_sentiment(n));
