###########################################
# Math 128A - Programming Assignment #1   #
#                                         #
# Written by Woo Sik (Lewis) Kim.         #
###########################################

import math

### Question 1 ###

"""Evaluate a cubic function in the form Cx^3 + Dx^2 + Ex + F at X."""
def evaluate_cubic(c, d, e, f, x):
	return c*(x**3) + d*(x**2) + e*(x) + f


"""Return the coefficients of the 1st deriv. quadratic of the cubic fn. defined by
   C, D, E, F.

   e.g. f(x) = 3x^3 + x^2 + x + 1

        Returns 9, 2, 1."""
def first_derivative(c, d, e, f):
	return 3*c, 2*d, e


"""Evaluate the second derivative of the cubic fn. defined by C, D, E, F at X.
   
   e.g. f(x) = 3x^3 + x^2 + x + 1

        We evaluate f''(x) = 18x + 2 at some x."""
def evaluate_second_deriv(c, d, e, f, x):
	return 6*c*x + 2*d


"""Solve the quadratic formula with given A, B, and C coefficients of a quadratic fn."""
def quadratic_formula(a, b, c):
	try:
		x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
		x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

		return x1, x2

	# Imaginary number error
	except:
		return None


"""."""
def find_extrema(a, b, c, d, e, f):
	# First, we check the cases where c = 0, in which case we have a quadratic (makes problem simpler),
	# or we have c = 0 and d = 0, in which case we simply have a linear line.
	if c == 0:
		return


	elif c == 0 and d == 0:
		# If the slope is negative:
		if e < 0:
			return b, a

		else:
			return a, b


	# First derivative (quadratic) coefficients:
	quad_coeff = first_derivative(c, d, e, f)

	# If we get NONE, then it means the quadratic has no real solutions, and we simply
	# Evaluate at A and B to get the local min and max.
	if quadratic_formula(quad_coeff[0], quad_coeff[1], quad_coeff[2]) == None:
		if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
			return a, b

		else:
			return b, a

	# Solutions to the 1st derivative, i.e. the quadratic:
	x1, x2 = quadratic_formula(quad_coeff[0], quad_coeff[1], quad_coeff[2])

	# Evaluate the solutions to the first derivative at the second derivative.
	x1_at_second_deriv = evaluate_second_deriv(c, d, e, f, x1)
	x2_at_second_deriv = evaluate_second_deriv(c, d, e, f, x2)

	# The following are simply conditions to check the locations of x1, x2 vs. the interval [a, b].
	# e.g. if neither x1 or x2 lie in [a, b], then we know that the local min/max is simply at a, b (or b, a),
	# depending on how the cubic is evaluated at a and b.

	# If x1 is max, x2 is min:
	if x1_at_second_deriv < 0 and x2_at_second_deriv > 0:
		if x1 >= a and x1 <= b and x2 >= a and x2 <= b:
			return x2, x1

		elif x1 >= a and x1 <= b:
			if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
				return a, x1

			else:
				return b, x1

		elif x2 >= a and x2 <= b:
			if evaluate_cubic(c, d, e, f, a) > evaluate_cubic(c, d, e, f, b):
				return x2, a

			else:
				return x2, b

		else:
			if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
				return a, b

			else:
				return b, a

	# If x1 is min, x2 is max:
	elif x1_at_second_deriv > 0 and x2_at_second_deriv < 0:
		if x1 >= a and x1 <= b and x2 >= a and x2 <= b:
			return x1, x2

		elif x1 >= a and x1 <= b:
			if evaluate_cubic(c, d, e, f, a) > evaluate_cubic(c, d, e, f, b):
				return x1, a

			else:
				return x1, b

		elif x2 >= a and x2 <= b:
			if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
				return a, x2

			else:
				return b, x2

		else:
			if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
				return a, b

			else:
				return b, a

	else:
		if evaluate_cubic(c, d, e, f, a) < evaluate_cubic(c, d, e, f, b):
			return a, b

		else:
			return b, a
	



### Question 2 ###

"""Evaluate the Ramanujan Nested Radicals at N."""
def nested_radicals(n):
	if n <= 0:
		raise ValueError("Invalid n. Must be >= 1.")
	if n == 1:
		return 1

	t = 1
	for k in range(n, 1, -1):
		t = math.sqrt(1 + k*t)

	return t

