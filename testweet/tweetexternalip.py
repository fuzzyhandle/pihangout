from __future__ import absolute_import, print_function
import json
import urllib
from pprint import pprint

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

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
  
  my_ip = json.load(urllib.urlopen('http://jsonip.com'))['ip']
  #print (my_ip)
  api.send_direct_message(user="hrishikesh_date", text="External IP is %s"%(my_ip))

  # print(api.me().name)
  # # If the application settings are set for "Read and Write" then
  # # this line should tweet out a direct message 
  # # The "Read and Write" setting is on https://dev.twitter.com/apps
  # #api.send_direct_message(user="hrishikesh_date", text="Hello From Pi :)")