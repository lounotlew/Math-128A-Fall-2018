from matplotlib import pyplot
import math as m
import numpy as np
from scipy.interpolate import spline
from interpolate1 import interpolate1
from interpolate2 import interpolate2


# The function we're using.
def f(x):
	return 1.0/(1 + (9*(x**2)))


# Generating xin linspaces (Uniform and Chebyshev) for n = 10, 19, 50, 99

xinU1 = np.array(np.linspace(-1, 1, 10+1).tolist())
xinU2 = np.array(np.linspace(-1, 1, 19+1).tolist())
xinU3 = np.array(np.linspace(-1, 1, 50+1).tolist())
xinU4 = np.array(np.linspace(-1, 1, 99+1).tolist())

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


"""Plot for Chebychev n=10."""
def plot1():
	yout = interpolate1(xinC1, xoutC1)

	x_values = np.linspace(-1, 1, 11)
	y_values = [f(x) for x in x_values.tolist()]

	pyplot.plot(x_values, y_values)
	pyplot.plot(xoutC1, yout)
	pyplot.show()


"""Plot for Uniform n=10."""
def plot2():
	values = interpolate1(xinU1, xoutU1)

	x_values = np.linspace(-1, 1, 11)
	y_values = [f(x) for x in x_values.tolist()]

	pyplot.plot(x_values, y_values)
	pyplot.plot(xoutU1, values)
	pyplot.show()


"""Plot for Chebychev n=19."""
def plot3():
	values = interpolate1(xinC2, xoutC2)

	x_values = np.linspace(-1, 1, 11)
	y_values = [f(x) for x in x_values.tolist()]

	pyplot.plot(x_values, y_values)
	pyplot.plot(xoutC2, values)
	pyplot.show()


"""Plot for Uniform n=19."""
def plot4():
	values = interpolate1(xinU2, xoutU2)

	x_values = np.linspace(-1, 1, 11)
	y_values = [f(x) for x in x_values.tolist()]

	pyplot.plot(x_values, y_values)
	pyplot.plot(xoutU2, values)
	pyplot.show()


### Semilogy plots. ###


"""Semilogy plot for Uniform n=50."""
def plot5():
	youtU1 = interpolate1(xinU3, xoutU3)
	youtU2 = interpolate2(xinU3, xoutU3)

	values1 = []
	values2 = []

	for i in range(len(xoutU3)):
		val = 1.0e-18 + abs(youtU1[i] - f(xoutU3[i]))
		values1.append(val)

	for i in range(len(xoutU3)):
		val = 1.0e-18 + abs(youtU2[i] - f(xoutU3[i]))
		values2.append(val)

	pyplot.semilogy(xoutU3, values1)
	pyplot.semilogy(xoutU3, values2)
	pyplot.show()


"""Semilogy plot for Chebyshev n=50."""
def plot6():
	youtC1 = interpolate1(xinC3, xoutC3)
	youtC2 = interpolate2(xinC3, xoutC3)

	values1 = []
	values2 = []

	for i in range(len(xoutC3)):
		val = 1.0e-18 + abs(youtC1[i] - f(xoutC3[i]))
		values1.append(val)

	for i in range(len(xoutC3)):
		val = 1.0e-18 + abs(youtC2[i] - f(xoutC3[i]))
		values2.append(val)

	pyplot.semilogy(xoutC3, values1)
	pyplot.semilogy(xoutC3, values2)
	pyplot.show()


"""Semilogy plot for Uniform n=99."""
def plot7():
	youtU1 = interpolate1(xinU4, xoutU4)
	youtU2 = interpolate2(xinU4, xoutU4)

	values1 = []
	values2 = []

	for i in range(len(xoutU4)):
		val = 1.0e-18 + abs(youtU1[i] - f(xoutU4[i]))
		values1.append(val)

	for i in range(len(xoutU4)):
		val = 1.0e-18 + abs(youtU2[i] - f(xoutU4[i]))
		values2.append(val)

	pyplot.semilogy(xoutU4, values1)
	pyplot.semilogy(xoutU4, values2)
	pyplot.show()


"""Semilogy plot for Chebyshev n=99."""
def plot8():
	youtC1 = interpolate1(xinC4, xoutC4)
	youtC2 = interpolate2(xinC4, xoutC4)

	values1 = []
	values2 = []

	for i in range(len(xoutC4)):
		val = 1.0e-18 + abs(youtC1[i] - f(xoutC4[i]))
		values1.append(val)

	for i in range(len(xoutC4)):
		val = 1.0e-18 + abs(youtC1[i] - f(xoutC4[i]))
		values2.append(val)

	pyplot.semilogy(xoutC4, values1)
	pyplot.semilogy(xoutC4, values2)
	pyplot.show()


plot8()
