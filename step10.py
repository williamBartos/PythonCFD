#Laplace Equation

from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot
from matplotlib import cm

def plot2D(x, y, p):
    fig = pyplot.figure(figsize = (11,7), dpi = 100)
    ax = fig.gca(projection = '3d')
    X,Y = numpy.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = 0, antialiased = False)
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.view_init(30,225)


#variable declarations
    
nx = 50
ny = 50
nt = 1000
xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax-xmin)/(nx-1)
dy = (ymax-ymin)/(ny-1)

#initialization
p = numpy.zeros((ny,nx))
pd = numpy.zeros((ny,nx)) 
b = numpy.zeros((ny,nx))
x = numpy.linspace(xmin,xmax,nx)
y = numpy.linspace(xmin,xmax,ny)

#source
b[ny/4,nx/4] = 100
b[3*ny/4, 3*nx/4] = -100

for it in range(nt):
    pd = p.copy()
    
    p[1:-1, 1:-1] = ((pd[1:-1, 2:] + pd[1:-1,:-2])*dy**2 + \
    (pd[2:,1:-1] + pd[:-2, 1:-1])*dx**2 -\
    b[1:-1, 1:-1]*dx**2*dy**2)/(2*(dx**2+dy**2))
    
    p[0,:] = 0
    p[ny-1,:] = 0
    p[:,0] = 0
    p[:,nx-1] = 0
    
plot2D(x,y,p)