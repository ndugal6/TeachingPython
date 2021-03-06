#Load NOAA station and temp data from text files
#Integrate, smooth, and plot data
# compute daily records
#download file over ftp
#parse a space seperated file

import numpy as np
import matplotlib.pyplot as pp
import seaborn

import urllib.request

urllib.request.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt','stations.txt')

open('stations.txt', 'r').readlines()[:10]

stations = {}
for line in open('stations.txt','r'):
    if 'GSN' in line:
        fields = line.split()

        stations[fields[0]] = ' '.join(fields[4:])
print(len(stations))


def findstation(s):
    found = {code: name for code, name in stations.items() if s in name}
    print(found)

findstation('LIHUE')

findstation('SAN DIEGO')

findstation('MINNEAPOLIS')

findstation('IRKUTSK')

datastations =  ['USW00022536','USW00023188','USW00014922','RSM00030710']