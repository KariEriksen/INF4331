#!/usr/bin/python

"""Import integrate function from integrator.py"""

from math import pi, sin
from integrator import integrate, midpoint_integrate
from numpy_integrator import numpy_integrate, midpoint_numpy_integrate
from numba_integrator import numba_integrate, midpoint_numba_integrate
import cython_integrator


#def comparison(f, a, b, N):


a = 0
b = pi
f = lambda x: sin(x)
N = 100000

exact_answer = 2.0

integrate(f, a, b, N)
midpoint_integrate(f, a, b, N)

numpy_integrate(f, a, b, N)
midpoint_numpy_integrate(f, a, b, N)

numba_integrate(f, a, b, N)
midpoint_numba_integrate(f, a, b, N)

cython_integrator.cython_integrate(a, b, N)
cython_integrator.midpoint_cython_integrate(a, b, N)
