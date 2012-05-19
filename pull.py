from random import gauss
from os import popen
from sys import argv

import pdb
#
maxquery = 25
numdests = 50

if len(argv) > 1:
   maxquery = int(argv[1])

# lexington
latmu = 38.08269
longmu = -84.484863
# roughly 400 miles:
latsigma = 3.5
longsigma = 3.5

for query in range(maxquery):
    destinations = [ (gauss(latmu, latsigma), gauss(longmu, longsigma)) for dummy in range(numdests) ]
    popenstr = 'wget \'http://maps.googleapis.com/maps/api/distancematrix/json?origins=' + str(latmu) + ',' + str(longmu) + '&destinations='
    imlazy = ''
    for count in range(0,len(destinations)):
        imlazy += str(destinations[count][0]) + ',' + str(destinations[count][1])
        if count < len(destinations) - 1:
            imlazy += '|'
    popenstr += imlazy
    popenstr += '&units=metric&sensor=false\''
    popen(popenstr + ' -O output' + str(query)) 
