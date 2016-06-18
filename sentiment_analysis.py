from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentiment_mod as s
import json
import sys


#consumer key, consumer secret, access token, access secret.


ckey="bViZAyDCRe"
csecret="CwCFaIrItB87wjOJ1UBrKZ"
atoken="OjC2eTxYbnBWefererRINYe"
asecret="ja5cGksvefucefuvfi3454re-00eudd0-e9g4iga3"
    


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

print (sys.argv[1])
arg1 = sys.argv[1]


def start_stream():
    while True:
        try:
            twitterStream = Stream(auth, listener())
            twitterStream.filter(track= [arg1],async=True)
        except: 
            continue

start_stream()

