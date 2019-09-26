import tweet_puller
import google_sentiments
import mention_puller

n_tweets = int(input('How many tweets would you like to analyze? '))

m = [];
m = mention_puller.mentions_pull(n_tweets)
m_len = len(m);
m_len = int(m_len/2);
temp_tweets = [];
neg_users = [];

for n in range(m_len):
    temp_tweets = tweet_puller.tweet_pull(m[n*2], 1);
    temp_ave = 0;
    for b in temp_tweets:
        temp_ave = temp_ave + int(google_sentiments.get_sentiment(b)[0]);
    if temp_ave < 0:
        neg_users.append(n);
        
w_sentiments = [];
for n in range(m_len):
    w_sentiments.append(google_sentiments.get_sentiment(m[n*2-1]));
    
return w_sentiments