#2D linear convection

from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot

nx = 81
ny = 81
nt = 100
c = 1
dx =  2/(nx-1)
dy = 2/(ny-1)
sigma = 0.2
dt = sigma*dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx)) #create a 1xn vector of 1's
un = numpy.ones((ny,nx))

#assign initial conditions

u[ .5/dy : 1/dy+1, .5/dx : 1/dx+1] = 2 ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2

for n in range(nt + 1): #looping across time steps
    un = u.copy()
    u[1:,1:] = un[1:,1:] - (c*dt/dx*(un[1:,1:] - un[1:, :-1])) - (c*dt/dy*(un[1:,1:] - un[:-1,1:]))
            
    u[0,:]      = 1
    u[-1,:]     = 1
    u[:,0]      = 1
    u[:,-1]     = 1

#plot the initial condition

fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.gca(projection = '3d')
X, Y = numpy.meshgrid(x,y)
surf2 = ax.plot_surface(X,Y, u[:])