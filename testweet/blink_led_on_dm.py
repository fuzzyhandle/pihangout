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
import functools
            
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
  return twt.sender_screen_name == 'hrishikesh_date'

def filter_for_time(twt,tm):
  print (twt.created_at,tm)
  return twt.created_at > tm

def nFilter(filters, tuples):
    for f in filters:
      tuples = ifilter(f, tuples)
    return tuples

def blinkled():
  from gpiozero import LED
  led = LED(17)
  led.on()
  time.sleep(1)
  led.off()

def loopforever():
  loopstarttime = None 
  lastchecktime = None
  while True:
    loopstarttime = datetime.utcnow()
    #First time set last check time to the time of the loop execution
    #This will filter only the message that come only after stating the program
    if (lastchecktime is None):
      lastchecktime = loopstarttime
    dm = api.direct_messages()
    
    fl = (filter_for_author, functools.partial(filter_for_time, tm=lastchecktime))
    for twt in nFilter(fl, dm):
      text = twt.text.encode('utf-8')
      tweettime = twt.created_at
      print ("%s received Message %s"%(tweettime, text))
      if text == "BLINK LED":
        blinkled()
      
    
    print ("Sleeping...")
    time.sleep (60)
    lastchecktime = loopstarttime

#starttime = datetime.utcnow()
#lastchecktime = starttime

api = getTwitterAPIHandle()
myid = api.me().id
#filters= (filter_for_author,)

if __name__ == '__main__':
  api = getTwitterAPIHandle()
  myid = api.me().id
  loopforever()  
