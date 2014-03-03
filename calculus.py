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
