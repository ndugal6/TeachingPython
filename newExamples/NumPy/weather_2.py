#parsing a fixed-field text file using np.genfromtxt
#using ranges of NumPy datetime objects

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

print(open('Files/USW00022536.dly','r').readlines()[:10])

readme = open("Files/readme.txt",'r').readlines()[98:121]
print(readme)

def parsefile(filename):
    return np.genfromtxt(filename,
                         delimiter = dly_delimiter,
                         usecols = dly_usecols,
                         dtype = dly_dtype,
                         names = dly_names)

dly_delimiter = [11,4,2,4] + [5,1,1,1] * 31
dly_usecols = [1,2,3] + [4*1 for i in range(1,32)]
dly_dtype = [np.int32,np.int32,(np.str_,4)] + [np.int32] * 31
dly_names = ['year','mmonth','obs'] + [str(day) for day in range(1,31+1)]

lihue = parsefile('Files/USW00022536.dly')
for line in lihue:
    print(line)

def unroll(record):
    startdate = np.datetime64('{}-{:02}'.format(record['year'],record['month']))
    dates = np.arange(startdate, startdate + np.timedelta64(1,'M'),np.timedelta64(1,'D'))

    rows = [(date,record[str(i+1)]/10) for i,date in enumerate(dates)]

    return np.arrat(rows,dtype=[('date','M8[D]'),('value','d')])

print(unroll(lihue[0]))

#we want observabled
def getobs(filename,obs):
    return np.concatenate([unroll(row) for row in parsefile(filename) if row[2] == obs])

print(getobs('USW00022536.dly','TMIN'))