#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json
import MeCab

### Constants                                                                                                                                                     
oath_key_dict = {
    "consumer_key": "your consumer_key",
    "consumer_secret": "your consumer_secret",
    "access_token": "your access_token",
    "access_token_secret": "your access_token_secret"
}

### Functions                                                                                                                                                     
def main():
    tweet_list = tweet_search("-Ochasen", oath_key_dict)
    text = ""
    for dic in tweet_list:
        
        text += dic['text'] + "\n"
    
    print(text)
    mecab = MeCab.Tagger("Twitter account you want search")
    mecab_parsed = mecab.parse(text)
    
    lines = mecab_parsed.split("\n")
    for line in lines:
        items = line.split("\t")
        if len(items)>4:
            if items[3].find("地域") > -1:
                print(items[0]+" "+items[3] )
        
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(user, oath_key_dict):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?"
    params = {
        "screen_name": user,
        "count": "100"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()
