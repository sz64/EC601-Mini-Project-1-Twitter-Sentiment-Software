# EC602-Mini-Project-1-Twitter-Sentiment-Software
This is software that will relay tweets from Twitter to the Google Natural Language API and provide the user with the sentiment of the tweets. This software comes with two usable functions, by running the file run.py. The first function gives the keywords of every tweet from a specified user and gives the sentiment on those keywords. The second function pulls all of the most recent mentions about the user and filters out those that are from users who are more negative no average. We believe that there are more users who post negative messages for their own amusement, that is not constructive, versus users who only post positive messages. So we decided to filter out these users from the list of tweets that mention the user. 

## User Stories:
Individuals who want to have a better estimate on the sentiment of responses on their profile. (MVP)

Business Owners who want to see the relative sentiment of tweets about their business.

Individuals who want a better understanding of another user's tweets. 

## Installation
To install and run this program, download the entire repository, and execute run.py with python to use the software. There may be some dependencies that need to be installed in order to run this code. In order to run this code, however, two API key files need to be editted in order to work. Gkey.json is the google service account json which can be downloaded from their site, while TKey.txt is a file that contains both the twitter developer keys and the user's own personal twitter keys. (Tkey Exmaple.txt shows the layout for each key)
- GKey.json
- TKey.txt

## Software Examples:
![ex1](https://github.com/sz64/EC601-Mini-Project-1-Twitter-Sentiment-Software/blob/master/F1.PNG)
![ex2](https://github.com/sz64/EC601-Mini-Project-1-Twitter-Sentiment-Software/blob/master/F2.PNG)

### Module Requirements
- google-cloud

- tweepy

## System Architecture:
![system architecture](https://github.com/sz64/EC601-Mini-Project-1-Twitter-Sentiment-Software/blob/master/architecture.png)

## File Descriptions:

run.py: The main file that should be run to run the software. 

tweet_puller.py: Takes the twitter username and number of tweets to analyze as inputs. Returns a list of strings for every tweet. Currently this file will read from a text file TKeys.txt for the API keys. 

mention_filter.py: This file takes the tweets that mention the user and analyzes the sentiment of each of the user's who posted the mentions to filter out users who have tweets that are negative on average. Returns a list of tweets that are from user's who are more positive on average. 

mention_puller.py: Uses a users twitter account API keys to pull mentions of that user. The file takes in one input (number of tweets) and returns a list of mentions and the user who mentioned them. 

module_test.py: Temporary test module for the tweet_puller file. 

google_sentiments.py: Can analyse sentiments from a comment, this needs a json file as a key.

google_apis: analyse text and get both entities and the senmtients of the entities.
        such as: "The humburger is bad."=> [[Hamburger,-0.6]]
        
analyse_functions: At first we use this functions to combine the entities with the same name. But last week we found the Natural Language API was updated and we don't need to use this function to combine anymore.

## Future Changes
- Spam Detection
- More accurate system for filtering out users in out mentions_filter
- GUI
