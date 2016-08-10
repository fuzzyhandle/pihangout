from __future__ import absolute_import, print_function
import json
import urllib
import os
import uptime
from pprint import pprint
from tzlocal import get_localzone

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


def parsedata(jsonfile):
  data = {}
  if os.path.isfile(jsonfile):
    with open('data.json') as f:
      try:
        data = json.load(f)
      except ValueError:
        #Ignore
        pass
  return data

def savedata(jsonfile,d):
  with open(jsonfile, 'w') as f:
    json.dump(d, f)
    
if __name__ == '__main__':
  datafile = "data.json"
  dateformat = "%Y %m %d %H:%M:%S %Z"
  olddata = {}
  newdata = {}
  
  olddata = parsedata(datafile)
  
  api = getTwitterAPIHandle()
  bootup_time = get_localzone().localize(uptime.boottime())
  str_bootup_time = bootup_time.strftime(dateformat)
  newdata = {"boot_time":str_bootup_time}
  
  #Send a message if the data has changed
  if olddata <> newdata:
    savedata(datafile,newdata)
    print ("Sending a message")
    api.send_direct_message(user="hrishikesh_date", text="Booted up at %s"%(str_bootup_time))
  else:
    print ("No update. Ignoring")
    