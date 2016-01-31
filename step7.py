#2D nonlinear convection

from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot
from matplotlib import cm

nx = 31
ny = 31
nt = 17
nu = 0.05
dx =  2/(nx-1)
dy = 2/(ny-1)
sigma = .25
dt = sigma*dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx)) #create a 1xn vector of 1's
un = numpy.ones((ny,nx))


def diffuse(nt): 
    u[ .5/dy : 1/dy+1, .5/dx : 1/dx+1] = 2 
    
    for n in range(nt+1):
        un = u.copy()
        u[1:-1, 1:-1] = un[1:-1, 1:-1]+nu*dt/dx**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])+nu*dt/dy**2*(un[2:,1:-1] - 2*un[1:-1, 1:-1] + un[0:-2, 1:-1])
        
        u[0,:]      = 1
        u[-1,:]     = 1
        u[:,0]      = 1
        u[:,-1]     = 1


    fig = pyplot.figure()
    ax = fig.gca(projection = '3d')
    X,Y = numpy.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,u[:], rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = 0, antialiased = True)
    ax.set_zlim(1,2.5)

diffuse(20)