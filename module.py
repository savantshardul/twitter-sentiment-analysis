import tweepy
from tweepy import OAuthHandler
from flask import Flask
from flask import jsonify
from flask import request
from app import app
import re
import html.parser



def getTweets(user,user_count):
    ckey="bViZAyDCRe"
    csecret="CwCFaIrItB87wjOJ1UBrKZ"
    atoken="OjC2eTxYbnBWefererRINYe"
    asecret="ja5cGksvefucefuvfi3454re-00eudd0-e9g4iga3"
    
    auth =tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api=tweepy.API(auth)
    usertimelines = api.user_timeline(screen_name = user, count = user_count)
    tweets=[]
    for single_tweet in usertimelines:
        temp_tweet1=addWebLinks(single_tweet)
        temp_tweet2=addUserMentions(temp_tweet1)
        final_tweet=addHashTags(temp_tweet2) 
        tweets.append({"status":final_tweet,"user":user}) 
    return tweets
  
def addUserMentions(tweet):
    searchObj = re.findall( r'@[^\s]+', tweet, re.M|re.I)
    if(tweet.startswith("RT") ):
        new_string= "<a href=https://twitter.com/" + searchObj[0][1:-1] + ">" + searchObj[0][:-1] + "</a>"
        tweet=tweet.replace(searchObj[0],new_string)
    for anyMatch in searchObj:
        new_string= "<a href=https://twitter.com/" + anyMatch[1:] + ">" + anyMatch + "</a>"
        tweet=tweet.replace(anyMatch,new_string)
    return tweet


def addHashTags(tweet):
    searchObj = re.findall( r'#([^\s]+)', tweet, re.M|re.I)
    for anyMatch in searchObj:
        new_string= "<a href=https://twitter.com/hashtag/" + anyMatch + ">#" + anyMatch + "</a>"
        tweet=tweet.replace(anyMatch,new_string)
    return tweet


def addWebLinks(single_tweet):
    tweet=single_tweet.text
    urls=single_tweet.entities.get("urls")
    media=single_tweet.entities.get("media")
    searchObj = re.findall( r'((www\.[^\s]+)|(https?://[^\s]+))', tweet, re.M|re.I)
    all_urls=None
    if(urls!=None):
        all_urls=urls
    if(media!=None):
        all_urls=all_urls+media
    for anyMatch in searchObj:
        for match in all_urls:
            if(anyMatch[0]==match.get("url")):
                expanded_url=match.get("expanded_url")
                display_url=match.get("display_url")
                new_string= "<a href=" + expanded_url + ">" + display_url + "</a>"
                tweet=tweet.replace(anyMatch[0],new_string)
    return tweet



  
@app.route('/')
def test():
    output=getTweets("savant_shardul",1010)
    """For Testing the method - getTweets() : Returns JSON Object as per the requirement for screen_name=savant_shardul"""
    return jsonify({"Statuses":output})


@app.route('/statuses', methods=['GET'])
def statuses():
    request_Usernames=request.args.get('screen_names')
    usernames_list=request_Usernames.split(",")
    count=request.args.get('count')
    if(count==None):
        error={"code":2 ,"message":"You have to specify the number of result this request should return"}
        return jsonify(errors=error)
    cursor=request.args.get('cursor')
    final=[]
    for single_username in usernames_list:
        tweets=getTweets(single_username,count)
        final.extend(tweets)
    return jsonify(next_cursor=cursor,Statuses=final)

