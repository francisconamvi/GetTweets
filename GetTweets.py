import tweepy
import json
import csv
from keys_and_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_list = list()

name = "fulano"
number = 50

user = api.get_user(name)
for status in tweepy.Cursor(api.user_timeline, id = name).items(number):
    if(status.in_reply_to_screen_name == None): #tira status respondendo
        if(status.is_quote_status == False): #tira retuites comentados
            if("retweeted_status" not in status._json.keys()): #tira puros retuites
                #limitar a tweets de 20 palavras
                if(len(status.text.split()) < 20):
                    if("https" not in status.text):
                        print('"'+status.text+'"')
                        tweet_list.append(status.text)
                        #print()

# outfile = name + "_tweets.csv"
# print("writing to " + outfile)
# with open(outfile, 'w+') as file:
#     writer = csv.writer(file)
#     for data in tweet_list:
#         writer.writerow([data])