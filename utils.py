import scipy.integrate


def fact(n):
	a = 1
	for num in range(2,n +1):
		a *= num
	return a
	pass

def roots(a, b, c):
	delta = b**2-(4*a*c)
	if delta == 0:
		root1 = -b/2*a
		return root1
	if delta < 0:
		delta = delta*-1
		root1 = (-b+(1j*(delta**(1/2))))/(2*a)
		root2 = (-b-(1j*(delta**(1/2))))/(2*a)
		return root1, root2
	if delta < 0:
		root1 = (-b+((delta**(1/2))))/(2*a)
		root2 = (-b-((delta**(1/2))))/(2*a)	
		return root1, root2
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(function, lower, upper):
	from scipy.integrate import quad
	f = lambda x: eval(function)
	I = quad(f,lower,upper)
	return I
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
	
