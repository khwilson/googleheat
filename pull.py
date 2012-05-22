#!/usr/bin/python

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

for query in range(maxquery):
    url = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins=%3.4f,%3.4f&destinations=' % (latmu, longmu)
    destinations = [ '%3.4f,%3.4f' % (gauss(latmu, latsigma), gauss(longmu, longsigma)) for dummy in range(numdests) ]
    url += '|'.join( destinations ) 
    url += '&units=metric&sensor=false'
    req = urllib2.Request(url)
    google_out = urllib2.urlopen(req).read()

    # See if we're over the temporary limit
    if google_out.find('OVER') != -1:
       time.sleep(10)
       google_out = urllib2.urlopen(req).read()
       if google_out.find('OVER') != -1:
          print "Apparently you're over the daily limit for requests"
          break
    
    # If it's a good request, write it out
    filename = 'output%d' % (int(time.time() * 1000))
    f = open(filename, 'wb')
    jOut = json.loads(google_out)
    jOut['latlongs'] = destinations
    f.write(json.dumps(jOut))




