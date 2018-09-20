####################################################################
# Code for generating the plot in Math 128A Programming HW#1, Q2.  #
#                                                                  #
# Written by Lewis Kim.                                            #
####################################################################

from matplotlib import pyplot
from hw1 import nested_radicals
import math

"""Generate a plot displaying ln(|a_n - a|) vs. n, and y = 3 - ln(2)n."""
def plot_q2():
	# Plotting ln(|a_n - a|) vs. n
	x_val1 = [x for x in range(1, 41)]
	y_val1 = [math.log(abs(nested_radicals(i) - 3)) for i in range(1, 41)]

	# Plotting y = 3 - ln(2)n.
	x_val2 = [x for x in range(1, 41)]
	y_val2 = [3 - math.log(2)*i for i in range(1, 41)]

	pyplot.scatter(x_val1, y_val1, c='g')
	pyplot.plot(x_val2, y_val2, c='b')
	pyplot.show()

