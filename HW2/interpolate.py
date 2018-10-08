###########################################################################
# Polynomial interpolation script files for Math 128A's Programming HW2.  #
#                                                                         #
# Written by Lewis Kim.                                                   #
###########################################################################

import numpy as np
import scipy.interpolate
import math as m


# The function we're using.
def f(x):
	return 1.0/(1 + (9*(x**2)))


# Generating xin linspaces (Uniform and Chebyshev) for n = 10, 19, 50, 99

xinU1 = np.linspace(-1, 1, 10+1)
xinU2 = np.linspace(-1, 1, 19+1)
xinU3 = np.linspace(-1, 1, 50+1)
xinU4 = np.linspace(-1, 1, 99+1)

xinC1 = np.array([m.cos(x) for x in np.linspace(-m.pi, 0, 10+1).tolist()])
xinC2 = np.array([m.cos(x) for x in np.linspace(-m.pi, 0, 19+1).tolist()])
xinC3 = np.array([m.cos(x) for x in np.linspace(-m.pi, 0, 50+1).tolist()])
xinC4 = np.array([m.cos(x) for x in np.linspace(-m.pi, 0, 99+1).tolist()])


# Generating y-outs:

youtU1 = np.array([f(x) for x in xinU1.tolist()])
youtU2 = np.array([f(x) for x in xinU2.tolist()])
youtU3 = np.array([f(x) for x in xinU3.tolist()])
youtU4 = np.array([f(x) for x in xinU4.tolist()])

youtC1 = np.array([f(x) for x in xinC1.tolist()])
youtC2 = np.array([f(x) for x in xinC2.tolist()])
youtC3 = np.array([f(x) for x in xinC3.tolist()])
youtC4 = np.array([f(x) for x in xinC4.tolist()])


"""Return a numpy poly1d object after performing scipy's Lagrange interpolation on a set of
   x-coordinates and y-coordinates."""
def interpolate1(x, y, as_coeff=False):
	return scipy.interpolate.lagrange(x, y)


"""Return a scipy BarycentricInterpolator object after performing scipy's Barycentric interpolation
   on a set of x-coordinates and y-coordinates."""
def interpolate2(x, y):
	return scipy.interpolate.BarycentricInterpolator(x, y)



print(interpolate1(xinC1, youtC1)(7))
print(interpolate2(xinC1, youtC1).__call__(7))

