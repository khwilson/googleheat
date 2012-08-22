from pull import make_query, geocode
import time
import pdb
import simplejson as json

def get_states(filename='State KML.csv'):
    lines = open(filename,'r').readlines()
    lines = lines[1:]
    names = [ l.split(',')[0] for l in lines ]
    return [ n for n in names 
             if n not in [ 'American Samoa', 
                           'Commonwealth of the Northern Mariana Islands', 
                           'Virgin Islands of the United States',
                           'Guam','Puerto Rico','Hawaii','Alaska'] ]

def get_state_latlongs():
    names = get_states()
    names = [ n.replace(' ','+') for n in names ]
    return dict( (n, geocode(n)) for n in names )

    

class stupidshit:
    def __init__(self):
        self.dists= {}

    def __call__(self):
        self.do_query()
        output = self.output
        f = open('output','r').readlines()
        latlongs = [ ','.join(ff.strip().split(',')[1:]) for ff in f[1:] ]
        names = [ ff.split(',')[0] for ff in f[1:] ]
        f = open('distancematrix','w')
        f.write('origin,destination,duration,distance')
        for n in names:
            for m in names:
                if n == m:
                    continue
                if n in output and m in output[n]:
                    f.write(n + ',' + m + ',' + ','.join(output[n][m]) + '\n')
        f.close()

    def do_query(self):
        f = open('output','r').readlines()
        latlongs = [ ','.join(ff.strip().split(',')[1:]) for ff in f[1:] ]
        names = [ ff.split(',')[0] for ff in f[1:] ]
        self.output = dict( (n,{}) for n in names)
        for i in xrange(1,len(names)):
            print i, names[i]
            time.sleep(1)
            google_out = make_query([latlongs[i]], latlongs[0:i])
            j = json.loads(google_out)
            self.dists = j['rows'][0]['elements']
            for k,d in enumerate(self.dists):
                self.output[names[i]].setdefault(names[k],{})
                self.output[names[i]][names[k]] = [str(d['duration']['value']), str(d['distance']['value'])]
        
