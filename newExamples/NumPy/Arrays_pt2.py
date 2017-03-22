#Applying mathematical operations to and between arrays
#Plotting one-dimensional arrays with matplotlib
#Performing linear-algebra computations with arrays

import numpy as np
import matplotlib.pyplot as pp

#numpy array of nums 1-10
x = np.linspace(0,10,40)

#Apply trig function to array
#Can't use standard Math.sin function of python. need to use numpy version which can take a full array as argumennt
sinx = np.sin(x)

# pp.plot(x,sinx)
# pp.show()

cosx = np.cos(x)
# pp.plot(x,sinx)
# pp.plot(x,cosx)

#Can modify style
# pp.plot(x,sinx, 'x')
# pp.plot(x,cosx, 'o')
# pp.show()

#Just as we can use uniary funciton sin, we can use regular operators
y = sinx * cosx
z = cosx**2 - sinx**2

pp.plot(x,y)
pp.plot(x,z)

#add legend
pp.legend(['sin(x) cos(x)', 'cos(x)^2 - sin(x)^s'])
# pp.show()

# Normally mathematical operations are applied to arrays element by element
# However, if you want to do linear algebra, that's not the case
# For instance, the inner product of 2 vectors, that's the sum of element by element products
#You can do this in numpy with the function dot. This will treat the two one-dimensional arrays as vectors.
np.dot(sinx,cosx)

# We could also take the outer product, which builds every possible combination of the elements from the two vectors
mat_outer = np.outer(sinx, cosx)

# The result is a matrix, Numpy always tries to be helpful in any way to guess what you want to do.
# So it has some broadcasting rules, with which it will try to make sensex.shape, x.size of operations between arrays of different shapes
# For instance, if you have a one-dimensional vector, and you add a number to it, just a single number, the numeber will be added to every element
v = np.linspace(0,10,5)
print(v)
print(v+1)


#Broadcasting also applies if we try to add a one-dimensional array to a 2-d array
# Let's see what happens
vv = np.outer(v,v)
print(vv + v)

#If instead we wanted to add the 1-d to every column, we'd first have to turn it into a proper n-by-one column vector, by adding a dimnsion with numpy newaxis

print(vv + v[:,np.newaxis])