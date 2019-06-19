#!/usr/bin/python

import numpy as np
from matplotlib.pyplot import *
import time

def integrate(f, a, b, N):

	a = float(a)
	b = float(b)
	delta_x = float((b-a)/N)
	I = 0
	x = a
	#Start timing how long the calculation takes
	start_time = time.time()

	for i in range(N+1):

		I += delta_x*f(x)
		x += a + delta_x

	#End timing
	end_time = time.time()
	simulation_time = end_time - start_time
	print ("CPU time = ", simulation_time)
	print ("Ordinary method = ", I)
	return I

def midpoint_integrate(f, a, b, N):

	a = float(a)
	b = float(b)
	delta_x = float((b-a)/N)
	I = 0
	x = a
	x2 = a/2.
	#Start timing how long the calculation takes
	start_time = time.time()

	for i in range(N+1):

		I += delta_x*f(x2)
		x += a + delta_x
		#Calculating the midpoint x2
		x2 = x - delta_x/2.

	#End timing
	end_time = time.time()
	simulation_time = end_time - start_time
	#print ("CPU time = ", simulation_time)
	print ("Ordinary midpoint method = ", I)
	return I


#f = lambda x: x**2
#integrate(f, 0, 1, 1000000)
#midpoint_integrate(f, 0, 1, 1000000)


#Plotting error in assignment 4.2
"""
K = 10
sim = np.linspace(100, 1000, K)
C_list = []
Error = []

for j in range(K):

	num = sim[j]
	C = integrate(f, 0, 1, num)
	C_list.append(C)
	Error.append(abs(C-(1./3)))

plot(sim, Error)
title("Error produced from calculating integral of x$^2$ from 0 to 1")
#legend((""), loc='upper right')
xlabel("N = number of timesteps")
ylabel("Correct value - computed value")
#axis([100, 10000, 0, 0.005])
show()
"""
