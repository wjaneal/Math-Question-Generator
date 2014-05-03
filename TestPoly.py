'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

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
