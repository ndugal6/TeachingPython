#Creating arrays: from a list, empty, zero, random, and linearly spaced
#Interrogating the dtype and shape of arrays
# Composing arrays
# Loading and saving arrays

import numpy as np
import matplotlib.pyplot as ppc =

a = np.array([1,2,3,4,5])

print(a.dtype) #Notice how numpy guess the data type based off our input

#We could've also specified the data type upon creation
a = np.array([1,2,3,4,5], dtype=np.float64)
print(a)

#Features that given us some info
# a.ndim, a.shape, a.size
print(a.ndim, a.shape, a.size)

b = np.array([[1,2,3,4,5], [6,7,8,9,10]], dtype=np.float64)
print(b)
print(b.ndim, b.shape, b.size)

#Other ways to make array
z = np.zeros((3,3),'d') # 'd' is shorthand for double which equates to np.float64
print(z)


e = np.empty([4,4],'d') #An empty array which can be dangerous since it just takes a block of memory as it is
print(e)

#Number of elements between 0 and 10
l = np.linspace(0,10,5)
print(l)
#Step to go between these elements
r = np.arange(0,10,2)
print(r)
#Give random numbers
ran = np.random.standard_normal((2,4))
print(ran)
#Combine arrays
a = np.random.standard_normal((2,3))
b = np.random.standard_normal((2,3))

v = np.vstack([a,b]) #Gives an array of 4 rows and 3 columns, vstack = Vertical Stack
print(v)

h = np.hstack[a,b] #Gives an array of 2 rows and 6 columns, hstack = Horizontal Stack

#Transpose an Array
h.transpose()

#To save an array
np.save('example.npy',a)

#To load the array back into use
al = np.load('example.npy')