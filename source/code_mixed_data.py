import tweepy
import pandas as pd
import re
consumer_key = "4oaR96mGutG5exI6zQw18kB3t"
consumer_secret = "GeqSmRLMj7ovrxeYPQFTM2H3aTrs14Ip7U0pSooaUr3OWHSzcH"
access_token = "945723835-hkXfk0hfrVtJ5yGCaA02IOHpyE2nyKWLjeF0SfLf"
access_token_secret = "tqyHO7nupdcpFwssDOFWtlhKlMiEyMBCKLpfI4vLBf69E"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def tweet_list(hashtag):
   sanju = api.search(hashtag,count=100)
   g = set()
   for i in range(len(sanju)):
       g.add(str(sanju[i]._json['text']))
   g = list(g)
   my_df = pd.DataFrame(g)
   my_df.to_csv("code_mixed_tweets.csv")	

tweet_list("#Sanju")

def user_tweet_list(username):
	taapsee = list()                                                                       
	for status in tweepy.Cursor(api.user_timeline, screen_name=username).items():
		taapsee.append(status._json['text'])
	my_df = pd.DataFrame(taapsee)
	my_df.to_csv("user_tweets.csv")

def filter_lid_text(lid_path):
	data = pd.read_csv(lid_path)
	data.columns=['id','tweet']
	code_mix_ids=list()
	for i in range(len(data['tweet'])): 
    	if bool(re.search("Hin",data['tweet'][i]))==bool(re.search("Eng",data['tweet'][i])):
        	code_mix_ids.append(i)
    return code_mix_ids