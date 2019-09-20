import tweepy

def mentions_pull(n_tweets):

    keys = open("TKey.txt").read().split();
    consumer_key = keys[0];
    consumer_secret = keys[1];

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth)

    mentions = []
    for t in tweepy.Cursor(api.mentions_timeline, tweet_mode='extended').items(n_tweets):
        mentions.append(t.full_text)
        mentions.append(t.user.screen_name)
    
    return mentions