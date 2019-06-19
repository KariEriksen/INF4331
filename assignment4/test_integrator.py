#!/usr/bin/python

"""Import integrate function from integrator.py"""

from integrator import integrate

def test_integral_of_constant_function():

	#abs(computed_answer - expected_answer) < 1E-20
	expected_answer = 2
	f = lambda x: 2; a = 0; b = 1; N = 1000000
	computed_answer = integrate(f, a, b, N) #numpy_integrate(f, a, b, N)
	print (computed_answer)
	#assert abs(computed_answer - expected_answer) < 1E-20, "Computational error to large!"
	if abs(computed_answer - expected_answer) < 1E-5:
		print ("Computation ok")
	else:
		print ("Computational error to large!")


def test_integral_of_linear_function():

	expected_answer = 1
	f = lambda x: 2*x; a = 0; b = 1; N = 1000000
	computed_answer = integrate(f, a, b, N) #numpy_integrate(f, a, b, N)
	#assert abs(computed_answer - expected_answer) < 1E-20, "Computational error to large!"
	if abs(computed_answer - expected_answer) < (1./N):
		print ("Computation ok")
	else:
		print ("Computational error to large, error = %f" % (1./N))


test_integral_of_constant_function()
#test_integral_of_linear_function()
