class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""
        
        self.coeff = coefficients
	

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        index = 0
        for i in range(len(self.coeff)):
		a = self.coeff[i]
		if a == 0:
			index = -1
		else:
			index = i	
	return index	


    def coefficients(self):
        """Return the list of coefficients. 

        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""
        
	coeff_list = list
        for i in range(len(self.coeff)):
		coeff_list.append(self.coeff[i])
	return coeff_list


    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        k = 0
	for i in range(len(self.coeff)):
		k += self.coeff[i]*x**i
	return k

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""

	new_poly = list
	if len(self.coeff) <= len(p.coeff):
		new_poly = p.coeff[:]
		for i in range(len(self.coeff)):
			new_poly[i] = p.coeff[i] + self.coeff[i]
	else:
		new_poly = self.coeff[:]
		for i in range(len(p.coeff)):
			new_poly[i] = self.coeff[i] + p.coeff[i]

			
        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""

        new_poly = list
	if len(self.coeff) <= len(p.coeff):
		new_poly = p.coeff[:]
		for i in range(len(self.coeff)):
			new_poly[i] = p.coeff[i] - self.coeff[i]
	else:
		new_poly = self.coeff[:]
		for i in range(len(p.coeff)):
			new_poly[i] = self.coeff[i] - p.coeff[i]

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

	poly = list
        if type(c) != int:
		poly = self.coeff[:]
		for i in range(len(self.coeff)):
			poly[i] = self.coeff[i]*c
	else:
		ArithmeticError
		#self.__rmul__(c) 

	return poly


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        c = int(round(c))
	poly = list
	poly = self.coeff[:]
	for i in range(len(self.coeff)):
		poly[i] = self.coeff[i]*c

	return poly
	
    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
	s = ''
        for i in range(len(self.coeff)-1, -1, -1):
		if self.coeff[i] != 0:
			s += ' + %g*x^%d' % (self.coeff[i], i)
		else:
            		s += ''
        return s


    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

	#NOTE: can't seem to get this one working... Not used in the test file



    	
	if len(self.coeff) != len(p.coeff):
		for i in range(len(self.coeff)):
			if self.coeff[i] != p.coeff[i]:
				return True
			else:
				return False
	"""
	if isinstance(self.coeff, p.coeff):
		return True
	else:
		return False
	"""
def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))

    
    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
