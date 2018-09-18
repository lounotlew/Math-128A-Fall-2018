###########################################
# Math 128A - Programming Assignment #1   #
#                                         #
# Written by Woo Sik (Lewis) Kim.         #
###########################################

# Notes: I probably should've just used Matlab to save myself some time and quite a few lines of code.

# The logic of problem 1 is straightforward; we calculate the first and second derivatives (or, the
# coefficients of the polynomials), and use the "derivative method" to find where the local min and max are
# for the cubic (or for the quadratic if c == 0)/ We then check the local min/max x values against the given range
# [a, b] to see if x1 and/or x2 lie in [a, b], and find the extrema of [a, b] from there.

# The code just happens to be long because there are a lot of cases to check. For example, if a local min
# and max exist at x1, x2 respectively, but if x1 and x2 are not in the range [a, b], then the local min/max
# of the cubic in [a, b] is just the min(f(a), f(b)), max(f(a), f(b)) respectively.
# Similarly, if x1 happens to be in [a, b] but not x2, then it means x1 is the local min of the cubic in the range [a, b],
# and local max is simply max(f(a), f(b)).
# We extend this logic to all other cases of either/both x1, x2 being inside/outside [a, b].

# Problem 2 is significantly shorter than 1, since there are no cases to check (other than the base case n == 1).

import math

### Question 1 ###

"""Evaluate a cubic function in the form Cx^3 + Dx^2 + Ex + F at X."""
def evaluate_cubic(c, d, e, f, x):
	return c*(x**3) + d*(x**2) + e*(x) + f


"""Return the coefficients of the 1st deriv. quadratic of the cubic fn. defined by
   C, D, E, F.

   e.g. f(x) = 3x^3 + x^2 + x + 1
        f'(x) = 9x^2 + 2x + 1

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


"""Evaluate the parabola of the form Ax^2 + Bx + C at X."""
def evaluate_parabola(a, b, c, x):
	return a*(x**2) + b*x + c


"""Find the local extrema of the parabola of the form Ax^2 + Bx + C in the range [r1, r2].""" 
def find_parabola_extrema(r1, r2, a, b, c):
	h = -b/(2*a)
	k = a*(h**2) + b*h + c

	# If the second derivative is > 0 or < 0:
	if 2*a > 0:
		concave_up = True

	else:
		concave_up = False

	if concave_up:
		if h >= r1 and h <= r2:
			if evaluate_parabola(a, b, c, r1) < evaluate_parabola(a, b, c, r2):
				return h, r1

			elif evaluate_parabola(a, b, c, r1) > evaluate_parabola(a, b, c, r2):
				return h, r2

			else:
				return h, r1

		else:
			if evaluate_parabola(a, b, c, r1) < evaluate_parabola(a, b, c, r2):
				return r1, r2

			elif evaluate_parabola(a, b, c, r1) > evaluate_parabola(a, b, c, r2):
				return r2, r1

			else:
				return r1, r2

	elif not concave_up:
		if h >= r1 and h <= r2:
			if evaluate_parabola(a, b, c, r1) < evaluate_parabola(a, b, c, r2):
				return r1, h

			elif evaluate_parabola(a, b, c, r1) > evaluate_parabola(a, b, c, r2):
				return r2, h

			else:
				return r1, h

		else:
			if evaluate_parabola(a, b, c, r1) < evaluate_parabola(a, b, c, r2):
				return r1, r2

			elif evaluate_parabola(a, b, c, r1) > evaluate_parabola(a, b, c, r2):
				return r2, r1

			else:
				return r1, r2

	else:
		if evaluate_parabola(a, b, c, r1) < evaluate_parabola(a, b, c, r2):
			return r1, r2

		elif evaluate_parabola(a, b, c, r1) > evaluate_parabola(a, b, c, r2):
			return r2, r1

		else:
			return r1, r2


"""Find the local extrema of the cubic of the form Cx^3 + Dx^2 + Ex + F in the range [a, b]."""
def find_extrema(a, b, c, d, e, f):
	# First, we check the cases where c = 0, in which case we have a quadratic (makes problem simpler),
	# or we have c = 0 and d = 0, in which case we simply have a linear line.
	if c == 0 and not d == 0:
		return find_parabola_extrema(a, b, d, e, f)

	elif c == 0 and d == 0 and not e == 0:
		# If the slope is negative:
		if e < 0:
			return b, a

		else:
			return a, b

	elif c == 0 and d == 0 and e == 0:
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

	# If x1 is local max, x2 is local min:
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

	# If x1 is local min, x2 is local max:
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


"""Run find_extrema(a, b, c, d, e, f) for the test cases provided in the handout for Problem 1."""
def test_problem1():
	# print("1) local min/max of -1x^3 + 2x^2 + -1x + 1 in [-1, 2]: " + str(find_extrema(-1, 2, -1, 2, -1, 1)))
	# print("2) local min/max of 1x^3 + -2x^2 + -1x + 1 in [1, 2]: " + str(find_extrema(1, 2, 1, -2, -1, 1)))
	# print("3) local min/max of 4x^3 + 8x^2 + -4x + -2 in [-2, 1]: " + str(find_extrema(-2, 1, 4, 8, -4, -2)))
	# print("4) local min/max of 1x^3 + 0x^2 + 1x + -3 in [-1, 2]: " + str(find_extrema(-1, 2, 1, 0, 1, -3)))
	# print("5) local min/max of 10^-14 x^3 + 9x^2 + -3x + 0 in [-0.3, 0.6]: " + str(find_extrema(-0.3, 0.6, 10**(-14), 9, -3, 0)))
	# print("6) local min/max of 0x^3 + 0x^2 + 0x + 1.7 in [-1, 2]: " + str(find_extrema(-1, 2, 0, 0, 0, 1.7)))
	# print("7) local min/max of -3x^3 + 9x^2 + -10^-14 x + 0 in [0, 3]: " + str(find_extrema(0, 3, -3, 9, -10**(-14), 0)))
	# print("8) local min/max of 0x^3 + -2x^2 + 3x + -1 in [0, 1]: " + str(find_extrema(0, 1, 0, -2, 3, -1)))

	# p2 = find_extrema(1, 2, 1, -2, -1, 1)
	# p3 = find_extrema(-2, 1, 4, 8, -4, -2)
	# p4 = find_extrema(-1, 2, 1, 0, 1, -3)
	# p5 = find_extrema(-0.3, 0.6, 10**(-14), 9, -3, 0)
	# p6 = find_extrema(-1, 2, 0, 0, 0, 1.7)
	p7 = find_extrema(0, 3, -3, 9, -10**(-14), 0)
	# p8 = find_extrema(0, 1, 0, -2, 3, -1)

	# print(evaluate_cubic(1, -2, -1, 1, p2[0]), evaluate_cubic(1, -2, -1, 1, p2[1]))
	# print(evaluate_cubic(4, 8, -4, -2, p3[0]), evaluate_cubic(4, 8, -4, -2, p3[1]))
	# print(evaluate_cubic(1, 0, 1, -3, p4[0]), evaluate_cubic(1, 0, 1, -3, p4[1]))
	# print(evaluate_cubic(10**(-14), 9, -3, 0, p5[0]), evaluate_cubic(10**(-14), 9, -3, 0, p5[1]))
	# print(evaluate_cubic(0, 0, 0, 1.7, p6[0]), evaluate_cubic(0, 0, 0, 1.7, p6[1]))
	# print(evaluate_cubic(-3, 9, -10**(-14), 0, p7[0]), evaluate_cubic(-3, 9, -10**(-14), 0, p7[1]))
	# print(evaluate_cubic(0, -2, 3, -1, p8[0]), evaluate_cubic(0, -2, 3, -1, p8[1]))

	print(p7)


	
### Question 2 ###

"""Evaluate the Ramanujan Nested Radicals at N."""
def nested_radicals(n):
	if n <= 0:
		raise ValueError("Invalid n. Must be >= 1.")
		return

	if n == 1:
		return 1

	nested_sum = 1
	for k in range(n, 1, -1):
		nested_sum = math.sqrt(1 + k*nested_sum)

	return nested_sum


"""Evaluate the Ramanujan nested radicals from N = 1 to N = 40, inclusive."""
def test_problem2():
	# for i in range(1, 41):
	# 	print("Ramanujan Nested Radical at n = " + str(i) + ": " + str(nested_radicals(i)))
	print(nested_radicals(1))
	print(nested_radicals(2))
	print(nested_radicals(3))
	print(nested_radicals(4))
	print(nested_radicals(5))
	print(nested_radicals(6))
	print(nested_radicals(38))
	print(nested_radicals(39))
	print(nested_radicals(40))


	# print("Limit appears to be 3.")

