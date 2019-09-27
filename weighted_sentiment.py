import tweet_puller
import google_sentiments
import mention_puller

def mention_filter(n_tweets):
    m = [];
    m = mention_puller.mentions_pull(n_tweets)
    m_len = len(m);
    m_len = int(m_len/2);
    temp_tweets = [];
    pos_users = [];

    for n in range(m_len):
        temp_tweets = tweet_puller.tweet_pull(m[n*2+1], 5);
        temp_ave = 0;
        for b in temp_tweets:
            temp_ave = temp_ave + google_sentiments.get_sentiment(b)[0];
        if temp_ave > 0:
            pos_users.append(n);
        
    w_tweets = [];
    for n in pos_users:
        print(m)
        w_tweets.append(m[n*2]);
	
    return w_sentimentsprint(m[n*2])