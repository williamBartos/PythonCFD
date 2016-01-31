import numpy
from pylab import *
import time, sys

phi = exp(-(x-4*t)**2/(4*nu*(t+1))) + exp(-(x-4*t-2*numpy.pi)**2/(4*nu*(t+1)))

phiprime = phi.diff(x)
print(phiprime)
