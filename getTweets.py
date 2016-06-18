import tweepy
from tweepy import OAuthHandler


def ProcessTweets(text,location):
	ckey="dkI7mZ2zvuLyDCRe"
	csecret="UkxsCPwCqKo1UBrK12Z"
	atoken="4071621492-ltDIoNjwQXOjC2eTxYbnBWMRINYe"
	asecret="ja5cGkSo4O4iga3"
	auth =tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api=tweepy.API(auth)
	c = tweepy.Cursor(api.search, q='')
	output = open("twitter-out.txt","a")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	from random import randint
	for num in range(0,500):
		i=randint(0,4)
		if(i<=2):
			output.write("neg")
			output.write('\n')
		else:
			output.write("pos")
			output.write('\n')

	output.close()
