import numpy
import time
cimport numpy 
cimport cython
from math import sin


cdef double f(double x):
	#return x**2
	return sin(x)
	
cpdef cython_integrate(double a, double b, int N):

	
	a = float(a)
	b = float(b)		
	cdef numpy.ndarray[numpy.double_t, ndim=1] x = numpy.linspace(a, b, N+1)
	cdef double delta_x = float((b-a)/N)

	#Start timing how long the calculation takes
	start_time = time.time()

	#cdef numpy.ndarray[numpy.double_t, ndim=1] I #= delta_x*f(x)
	cdef double I = 0
	for i in range(len(x)):
		I += delta_x*f(x[i])

	#cdef double sum_I = sum_integral(I)

	#End timing
	end_time = time.time()
	computing_time = end_time - start_time
	#print ("CPU time cython = ", computing_time)
	print "Cython method = ", I
	return I


def midpoint_cython_integrate(double a, double b, int N):

	a = float(a)
	b = float(b)
	cdef numpy.ndarray[numpy.double_t, ndim=1] x = numpy.linspace(a, b, N+1)
	cdef double delta_x = float((b-a)/N)
	#Start timing how long the calculation takes
	start_time = time.time()

	#Taking care of first element in x
	cdef double I = delta_x*f(x[0])
	for i in range(len(x)):
		I += delta_x*f(x[i] - delta_x/2.)

	#End timing
	end_time = time.time()
	computing_time = end_time - start_time
	#print ("CPU time cython midpoint = ", computing_time)
	print "Cython midpoint method = ", I
	return I


#%timeit cython_integrate()
