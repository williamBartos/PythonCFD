import numpy
from pylab import *
import time, sys
#from IPython.core.display import clear_output #used for inline animation

nx = 41
dx = 2/float(nx-1)
nt = 25     #number of timesteps calculated
dt = 0.025   #amount of time each timestep covers (delta t)
c = 1       #assumed wavespeed of c = 1


u = numpy.ones(nx)      #numpy function ones()
u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

un = numpy.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt
    un = u.copy() ##copy the existing values of u into un
    for i in range(1,nx): ## you can try commenting this line and...
    #for i in range(nx): ## ... uncommenting this line and see what happens!
        u[i] = un[i]-c*(dt/dx)*(un[i]-un[i-1])

plot(numpy.linspace(0,2,nx), u)
show()
