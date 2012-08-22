#!/bin/python
# create_csv.py
# Tarik Tosun, 2012-08-21
# Description:
#   Creates a simple CSV with latitudes/longitudes and distance values in order
#   to play with google fusion tables.
import simplejson as json
import csv
import pdb

def create_csv(infile_name='file.json',outfile_name='csv.txt'):
    """ format: place name, distance(m), duration(s)"""
    infile = open(infile_name, 'rb')
    outfile = open(outfile_name, 'wb')
    jIn = json.loads(infile.read())
    csv_out = csv.writer(outfile)

    dist_dur = jIn['rows'][0]['elements']
    out_list = [[]]*len(dist_dur)
    csv_out.writerow(['lat-long','distances','durations'])
    for i,str in enumerate(jIn['latlongs']):
    #for i,str in enumerate(jIn['destination_addresses']): 
        if dist_dur[i]['status'] == 'OK':
            distance = dist_dur[i]['distance']['value'] 
            duration = dist_dur[i]['duration']['value'] 
            out_list[i] = [str,distance,duration]
        else:
            out_list[i] = [str,-1,-1]
        csv_out.writerow(out_list[i])
    infile.close()
    outfile.close()

    

