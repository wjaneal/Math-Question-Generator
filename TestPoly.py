
from Polynomials import *

class NumberRange:
  def __init__(self, Min, Max):
		self.Minimum = Min
		self.Maximum = Max
		print "The range has been initialized"

A = Polynomial(6)

Range = NumberRange(-10,10)
A.GenerateIntRoots(Range)
A.GenerateCoefficients()
#A.Coefficients = [0,0,1]
A.Derivative = A.Differentiate(A.Coefficients)
Roots = A.Newtons_Method(A)
