import tweepy
import tweet_puller
import google_sentiments
import google_apis
import weighted_sentiment

func = input('Type \"1\" to analyze your mentions or \"2\" for another user\'s tweets: ');

tweets = [];
if int(func) == 2:
	scr_name = input('Twitter username: ');
	n_tweets = int(input('How many tweets would you like to analyze? '))
	tweets = tweet_puller.tweet_pull(scr_name, n_tweets);
elif int(func) == 1:
	n_tweets = int(input('How many tweets would you like to analyze? '))
	tweets = weighted_sentiment.mention_filter(n_tweets);
else:
	print('You did not enter a valid input')
	exit()

sentiments_list = [];

for n in tweets:
	print(google_apis.google_sentiments_entities(n));