import datetime
from authentication import api
import tweepy

listOfTweets = []
user_name = "@KimKardashian"

def get_tweets(user_name):
    counter = 0
    # Iterate through all tweets containing the given word, api search mode
    for tweet in tweepy.Cursor(api.user_timeline, id=user_name, tweet_mode = 'extended').items(1):
        #Add tweets in this format
        dict_ = {'Index': counter,
                'Tweet': tweet.full_text,
                'Tweet ID': tweet.id,
                }
        listOfTweets.append(dict_)  
        counter += 1 
    return listOfTweets

(get_tweets(user_name))

the_tweet_that_I_want = listOfTweets[0]['Tweet']
the_tweet_that_I_want_ID = listOfTweets[0]['Tweet ID']

def manipulate_tweet(tweet_text):
    result = ""
    for i in range(len(tweet_text)):
        if not tweet_text[i].isalpha():
            result += tweet_text[i]
            continue
        if i % 2 == 0:
            result += tweet_text[i].lower()
        else:
            result += tweet_text[i].upper()
    return result

URL = "https://twitter.com/" + str(user_name) +  "/status/" + str(the_tweet_that_I_want_ID)

message = str(user_name) + " " + str(manipulate_tweet(the_tweet_that_I_want)) + "\n" + URL

if len(message) > 280:
    message = str(user_name) + " " + str(manipulate_tweet(the_tweet_that_I_want))

print('posting this clever message to twitter:')
print(message)

api.update_status(message)

print('success!')
