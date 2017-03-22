#Indexing array elements
#Slicing arrays
#Advanced indexing
#NumPy vs Python-list indexing and slicing


import numpy as np

v = np.linspace(0,10,5)
v[0]
v[-1]

vv = np.random.random((5,4))
#First argument is row, second is column
vv[0,0]
vv[4,3]

ll = [[1,2,3],[4,5,6],[7,8,9]]
# ll[1 , 2]
ll[1][2]

#slicing
v[2:4]

#2-d slice on one or both
vv[2:5,1] #Gives 1-d array of the data
vv[2:5,1:2] #Gives 2-d array of the data
#Can use all the tricks form pythons list such as
vv[2:-1,:]
vv[:,::2] # :: indicates step size of 2

#Important note, the below code points v2 to the slice of v, therefore any changes to v2 will also changes those elements in v
v2 = v[2:4]
v[0] = 0

v3 = v[2:4].copy()

#advanced indexing extensions
print(v)
print(v[[1,2,3]]) #use list to select

#Create list of boolenvalues, then select only the items from array where true
bool_index = v > 0
v[bool_index]
vv[vv > 0.5] = vv[vv > 0.5] * 2 #Operates on elements of VV where elements are  than 0.5
