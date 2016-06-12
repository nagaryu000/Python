#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json
import MeCab

### Constants                                                                                                                                                     
oath_key_dict = {
    "consumer_key": "qK0BBiDzeZqekFq5VzOpKoX0R",
    "consumer_secret": "WpjvlWM4A2ed9ajZol5P2IT2yZsOnmItcRi4bxPTbbrWgvvQiz",
    "access_token": "129074254-k6wpcnlxjIiWxVgcI9NhbgDG5K6rrp1iwKiv6AlW",
    "access_token_secret": "pxh24zt3ob6W1gxHlKYKvmUMCicOuaeilAmdXRhpjE0O7"
}

### Functions                                                                                                                                                     
def main():
    tweet_list = tweet_search("@7x3x7x3", oath_key_dict)
    text = ""
    for dic in tweet_list:
        
        text += dic['text'] + "\n"
    
    print(text)
    mecab = MeCab.Tagger("-Ochasen")
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