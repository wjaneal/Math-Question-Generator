'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

#Define Polynomial Differentiation Questions
def Polynomial_Questions(order):
	Range1 = NumberRange(-10,10)
	Equation_String = "(*x*)(*x*)"
	NumVariables = CountStars(Equation_String)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(Equation_String,VariableSet,RangeSet)
	E1 = Q1.Create_Equation_String(Q1.Format_String, 1)
	#Set Variables According to Randomly Generated Polynomials
	P1 = Polynomial(1)
	P1.GenerateIntRoots(Range1)
	P1.GenerateCoefficients()
	P2 = Polynomial(1)
	P2.GenerateIntRoots(Range1)
	P2.GenerateCoefficients()
	print P1.Roots, P1.Coefficients
	P3 = Polynomial(10)
	P3.GenerateIntRoots(Range1)
	P3.GenerateCoefficients()
	P4 = P3.Differentiate(P3.Coefficients)
	print P3.Coefficients
	print P4
	P3.Generate_Latex_String(P3.Coefficients)
	return [Question_String,Answer_String]
