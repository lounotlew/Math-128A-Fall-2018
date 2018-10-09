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

xoutU1 = np.array([f(x) for x in xinU1.tolist()])
xoutU2 = np.array([f(x) for x in xinU2.tolist()])
xoutU3 = np.array([f(x) for x in xinU3.tolist()])
xoutU4 = np.array([f(x) for x in xinU4.tolist()])

xoutC1 = np.array([f(x) for x in xinC1.tolist()])
xoutC2 = np.array([f(x) for x in xinC2.tolist()])
xoutC3 = np.array([f(x) for x in xinC3.tolist()])
xoutC4 = np.array([f(x) for x in xinC4.tolist()])


"""."""
def interpolate2(xin, xout):
	yout = []

	for x in xout:
		if x in xin:
			yout.append(f(x))

		else:
			yout.append(barycentric(x, xin))

	return yout


"""."""
def barycentric(x, xin):
	top_sum = 0
	bottom_sum = 0

	for j in range(len(xin)):
		top_sum += (lambda_coeff(j, xin)*f(xin[j]))/(x - xin[j])


	for j in range(len(xin)):
		bottom_sum += lambda_coeff(j, xin)/(x - xin[j])

	return top_sum/bottom_sum


"""."""
def lambda_coeff(j, xin):
	product = 1

	for k in range(len(xin)):
		if j != k:
			product *= (xin[j] - xin[k])

	return 1/product


print(interpolate2(xinU1, xoutU1))















