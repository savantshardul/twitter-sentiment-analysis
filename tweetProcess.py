import re


def tweetCleaning(tweet):

    #Convert the whole tweet to lower case
    tweet = tweet.lower()
    #Remove the URLS from the tweet
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    #Remove the Usernames
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Rmove # from hashtag
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
