#!/usr/bin/python
# pull.py
# Kevin Wilson and Tarik Tosun, August 2012
# Description:
#   Makes pull request to google maps API in order to get distance and duration
#   data.

from random import gauss
from sys import argv
import urllib2
import time
import simplejson as json

import pdb
#
maxquery = 25
numdests = 50

if len(argv) > 1:
   maxquery = int(argv[1])

# witchita:
latmu = 38.08269
longmu = -84.484863
# roughly 400 miles:
latsigma = 3.5
longsigma = 3.5

def make_query(origins, destinations):
   origins_str = map(str, origins)
   destinations_str = map(str, destinations)
   url = ('http://maps.googleapis.com/maps/api/distancematrix/json?' +
          'origins=' + '|'.join(origins_str) +
          '&destinations=' + '|'.join(destinations_str))
   url += '&units=metric&sensor=false'
   print url
   req = urllib2.Request(url)
   google_out = urllib2.urlopen(req).read()
   
    # See if we're over the temporary limit
   if google_out.find('OVER') != -1:
      time.sleep(10)
      google_out = urllib2.urlopen(req).read()
      if google_out.find('OVER') != -1:
         raise ValueError("Over the daily limit for requests")
   
   return google_out

def geocode(address):
   url=('http://maps.googleapis.com/maps/api/geocode/json?' + 
        'address=%s&sensor=false' % address)
   req = urllib2.Request(url)
   google_out = urllib2.urlopen(req).read()
   j = json.loads(google_out)
   return j['results'][0]['geometry']['location']

def format(geocode_dict_list):
    out_list = [str(entry['lat']) + ',' + str(entry['lng']) for entry in geocode_dict_list]
    return out_list


'''
if __name__=='__main__':
   r"""
   Add back in a test guy
   """

   maxquery = 25
   numdests = 50

   # witchita:
   latmu = 38.08269
   longmu = -84.484863
   # roughly 400 miles:
   latsigma = 3.5
   longsigma = 3.5
   pdb.set_trace()

   for query in range(maxquery):
      destinations = [ '%3.4f,%3.4f' % 
                       (gauss(latmu, latsigma), gauss(longmu, longsigma)) 
                       for dummy in range(numdests) ]
      try:
         google_out = make_query([ ','.join([str(latmu), str(longmu)])], 
                                 destinations)
      except ValueError, e:
         print e
         exit()

      # If it's a good request, write it out
      filename = 'output%d' % (int(time.time() * 1000))
      f = open(filename, 'wb')
      jOut = json.loads(google_out)
      jOut['latlongs'] = destinations
      f.write(json.dumps(jOut))

'''
