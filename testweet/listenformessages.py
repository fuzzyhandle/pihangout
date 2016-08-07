from __future__ import absolute_import, print_function
from datetime import datetime
import json
import urllib
import time

from pprint import pprint

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from itertools import ifilter
            
def getTwitterAPIHandle():
  with open('api_secret_token.json') as data_file:    
    authdata = json.load(data_file)
  #pprint(authdata)
  auth = OAuthHandler(authdata['consumer_key'], authdata['consumer_secret'])
  auth.set_access_token(authdata['access_token'], authdata['access_token_secret'])

  api = API(auth)
  return api

def filter_has_my_mention(twt):
  for um in twt.entities['user_mentions']:
    if um['id'] == myid:
      return True
  
  return False

def filter_for_author(twt):
  return twt.user.screen_name == 'hrishikesh_date'

def nFilter(filters, tuples):
    for f in filters:
        tuples = ifilter(f, tuples)
    return tuples
    
if __name__ == '__main__':
  starttime = datetime.now()
  
  api = getTwitterAPIHandle()
  myid = api.me().id
  
  #Get Default number of recent tweets
  tl = api.home_timeline()
  filters= (filter_for_author,filter_has_my_mention)
  
  #for twt in nFilter(filters, tl):
    #print (twt.text.encode('utf-8'))
  #   print (twt.created_at)