from __future__ import absolute_import, print_function
import json
import os
from pprint import pprint
from tweepy import OAuthHandler
from tweepy import API
from itertools import ifilter

import wiringpi

wiringpi.wiringPiSetupGpio() # For GPIO pin numbering

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

def filter_for_author(twt):
  return twt.sender_screen_name == 'hrishikesh_date'
  
def nFilter(filters, tuples):
    for f in filters:
      tuples = ifilter(f, tuples)
    return tuples  

def work():
  pin = 17
  wiringpi.pinMode(pin,wiringpi.GPIO.OUTPUT)
  try:
    for i in range (0,3):
      wiringpi.digitalWrite(pin,wiringpi.GPIO.HIGH)
      wiringpi.delay(500)
      wiringpi.digitalWrite(pin,wiringpi.GPIO.LOW)
      wiringpi.delay(500)
  finally:
    wiringpi.digitalWrite(pin,wiringpi.GPIO.LOW)
  
if __name__ == '__main__':
  datafile = "data.json"
  olddata = {}
  newdata = {}
  
  olddata = parsedata(datafile)
  
  last_id = olddata.get("message_id",0)
    
  api = getTwitterAPIHandle()
  
  dm = api.direct_messages(since_id=last_id)
  
  fl = (filter_for_author,)
  
  newdata = olddata
  
  for twt in nFilter(fl, dm):
    text = twt.text.encode('utf-8')
    #tweettime = twt.created_at
    last_id = twt.id
    newdata.update(message_id=last_id)
    if text == "BLINK LED":
      print ("Calling work")
      work()
    savedata(datafile,newdata)  
  newdata = {"last_checked_messageid":0}
  
  
    