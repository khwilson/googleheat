# Extracts zip codes from the list of CA zips:
import csv

def extract_zips(fname = 'CA_Zip_Code_KML.csv'):
    f = open(fname)
    reader = csv.reader(f)
    zips = []
    for row in reader:
        zip = row[1]
        zips.append(zip)
    return zips

def filter_numbers(zips):
    outlist = []
    for string in zips:
        try:
            z = int(string) 
        except ValueError:
            continue
        outlist.append(z)
    return outlist

zip_numbers = filter_numbers(extract_zips())

