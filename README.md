# EC602-Mini-Project-1-Twitter-Sentiment-Software
This is software that will relay tweets from Twitter to the Google Natural Language API and provide the user with the sentiment of the tweet.

## User Stories:
Business Owners who want to see the relative sentiment of tweets about their business.

Business Owners who want to get the comments from real people rather than robots.

Individuals who want to have a better estimate on the sentiment of responses on their profile. 

Individuals who want an idea of how positive or negative a user is on average. 



## File Descriptions:

tweet_puller.py: Takes the twitter username and number of tweets to analyze as inputs. Returns a list of strings for every tweet. Currently this file will read from a text file TKeys.txt for the API keys. 

mention_puller.py: Uses a users twitter account API keys to pull mentions of that user. The file takes in one input (number of tweets) and returns a list of mentions and the user who mentioned them. 

module_test.py: Temporary test module for the tweet_puller file. 

google_sentiments.py: Can analyse sentiments from a comment,this need a json file as a key.
google_apis: analyse text and get both entities and the senmtients of the entities.
        such as: "The humburger is bad."=> [[Hamburger,-0.6]]

