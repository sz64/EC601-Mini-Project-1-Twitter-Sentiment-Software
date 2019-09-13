import tweepy
import tweet_puller
import sentiment_puller

scr_name = input('Twitter username: ');
n_tweets = int(input('How many tweets would you like to analyze? '))
tweets = [];

tweets = tweet_puller.tweet_pull(scr_name, n_tweets);

sentiments_list = [];

for n in tweets:
	sentiments_list.append(sentiment_puller.get_sentiment(n));
	print(sentiment_puller.get_sentiment(n));