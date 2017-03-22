#Creating and manipulating NumPy record arrays
    #Record arrays are 2-d arrays without all elements being the same type
    #Hybrid of list and dictionary
#Working with NumPy datetime64 objects

import numpy as np

reca = np.array([(1,(2.0,3.0),'hey'),(2,(3.5,4.0),'n')],
                dtype=[('x',np.int32),('y',np.float64,2),('z',np.str,4)])
#dtype for row one is int 32, for row two named 'y' is float and we need two of them, then row 3 named z which is a string of max length 4

#access first row
reca[0]
reca['x']
reca['x'][0]
reca[0]['x']

#Data type that can hold date and time
# np.datetime('2015')
# np.datetime('2015-01')
# np.datetime('2015-01-03 12:00:00')
# np.datetime('2015-01-03 12:00:00+0700')
# np.datetime('2015-01-03') < np.datetime('2015-04-04')
# np.datetime('2015-01-03') - np.datetime('2015-04-04')
# np.datetime('2015-01-03') + np.datetime(5,'D')
# np.datetime('2015-01-03') + np.datetime(6, 'h')

