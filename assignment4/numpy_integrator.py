#!/usr/bin/python

import numpy as np
import time
from math import pi, sin

def numpy_integrate(f, a, b, N):


	a = float(a)
	b = float(b)
	x = np.linspace(a, b, N+1)
	delta_x = float(b/N)
	#Start timing how long the calculation takes
	start_time = time.time()
	"""
	I = delta_x*f(x)
	sum_I = sum(I)
	"""
	I = 0
	for i in range(N):

		I += delta_x*f(x[i])

	#End timing
	end_time = time.time()
	computing_time = end_time - start_time
	print ("CPU time = ", computing_time)
	print ("Numpy method = ", I)
	return I

def midpoint_numpy_integrate(f, a, b, N):


	a = float(a)
	b = float(b)
	delta_x = float((b-a)/N)
	x = np.linspace(a, b, N+1)
	#Start timing how long the calculation takes
	start_time = time.time()

	#Taking care of first element in x
	"""
	I = delta_x*f(x[0])
	I += delta_x*f(x[1:] - delta_x/2.)
	sum_I = sum(I)
	"""
	I = delta_x*f(x[0])
	for i in range(N):
		I += delta_x*f(x[i+1] - delta_x/2.)

	#End timing
	end_time = time.time()
	computing_time = end_time - start_time
	#print ("CPU time = ", computing_time)
	print ("Numpy midpoint method = ", I)
	return I

#f = lambda x: sin(x)
#N = 1000
#numpy_integrate(f, 0, pi, N)
#midpoint_numpy_integrate(f, 0, pi, N)
