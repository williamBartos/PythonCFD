import numpy
from pylab import *
import time, sys
#from IPython.core.display import clear_output #used for inline animation

nx = 41
dx = 2/float(nx-1)
nt = 20     #number of timesteps calculated
nu = 0.3    #the value of the viscosity
sigma = 0.2 #sigma is a parameter
dt = (sigma*(dx**2))/nu



u = numpy.ones(nx)      #numpy function ones()
u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

un = numpy.ones(nx) #initialize a temporary array which advances the solution in time

for n in range(nt):  #loop for values of n from 0 to nt
    un = u.copy() ##copy the existing values of u into un
    for i in range(1,nx-1):
        u[i] = un[i] + nu*dt/dx**2*(un[i+1]-2*un[i] + un[i-1])

plot(numpy.linspace(0,2,nx), u)
show()
