import tweepy

def tweet_pull(scr_name, n_tweets):


	keys = open("TKey.txt").read().split();
	consumer_key = keys[0];
	consumer_secret = keys[1];

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	api = tweepy.API(auth)
	
	tweets = [];
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=scr_name, result_type = 'recent', tweet_mode='extended').items(n_tweets):
		tweets.append(tweet.full_text);
		
	return tweets;