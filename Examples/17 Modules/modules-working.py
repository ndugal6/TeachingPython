#!/usr/bin/python3
#MODULE PACKAGES LOCATION
#   HTTP://PYPI.PYTHON.ORG/PYPI

import sys

def main():
    #Prints python version
    print('Python version {}.{}.{}'.format(*sys.version_info))
    #Get system platform that the os is running on
    print(sys.platform)

    #Notice how you can import within stuff
    import os
    print(os.name)
    #Get environment variables
    print(os.getenv('PATH'))
    #Get current working directory
    print(os.getcwd())
    #Gives random bytes
    print(os.urandom(25))

    import urllib.request
    #Get website as object, cast bytes as string
#    page = urllib.request.urlopen('http://lsu.edu')
#    for line in page: print(str(line, encoding = 'utf_8'), end=' ')
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.metrics import pairwise_distances_argmin
    from sklearn.datasets import load_sample_image
    from sklearn.utils import shuffle
    from time import time

    import  random
    #Print random number in a range
    print(random.randint(1,1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    x = shuffle(x, random_state=0)[:1000]
    print(x)
    x = shuffle(x, random_state=0)[:10]
    print(x)
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)




if __name__ == "__main__": main()
