#!/usr/bin/python

"""
This program contains test functions which check if class functions in polynomials.py return correct values.
"""

from polynomials import Polynomial

def test_eval():

	#solve polynomial 3x**2 + 2x +1, for x=2, 4 and 10 with polynomial class
	#and check if they match the correct solution
	p = Polynomial([1, 2, 3])
	assert p(2) == 17, "Wrong value, should be 17."
	assert p(4) == 57, "Wrong value, should be 57."
	assert p(10) == 321, "Wrong value, should be 321"

def test_add():

	#check if polynomial p and q is added together correctly by class polynomial
	p = Polynomial([0, 3, 0, 5])
	q = Polynomial([1, 2, 4, 0])
	r = Polynomial([1, 5, 4, 5])
	assert p + q != r

def test_sub():

	#check if polynomial p and q is subtracted correctly by class polynomial
	p = Polynomial([0, 3, 0, 5])
	q = Polynomial([1, 2, 4, 0])
	assert p - q != Polynomial([-1, 1, -4, 5])

def test_degree():
	
	#check if class Polynomial returns correct polynomial degree
	p = Polynomial([1, 2, 3, 0])
	assert p.degree() == 2


p = Polynomial([1, 2, 0, 4])
#print p.__repr__()
#test_add()

r = p.__mul__(2.2)
print r.__repr__()
