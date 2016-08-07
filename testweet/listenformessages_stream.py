from __future__ import absolute_import, print_function
import json
import urllib
import time

from pprint import pprint

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

class MyStreamListener(StreamListener):

    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
            
def getTwitterAPIHandle():
  with open('api_secret_token.json') as data_file:    
    authdata = json.load(data_file)
  #pprint(authdata)
  auth = OAuthHandler(authdata['consumer_key'], authdata['consumer_secret'])
  auth.set_access_token(authdata['access_token'], authdata['access_token_secret'])

  api = API(auth)
  return api
  
if __name__ == '__main__':
  api = getTwitterAPIHandle()
  myStreamListener = MyStreamListener()
  myStream = Stream(auth = api.auth, listener=myStreamListener)
  myStream.filter(track=['myHDPi3_A'],async=True)
  