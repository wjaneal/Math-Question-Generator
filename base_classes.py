########################################################################
#Base Classes for Python Automatic Question Generation Program
##########################################################################
from random import *
from fractions import *
from math import *

def lcm(a, b):
	return (a * b) // gcd(a, b)
	return reduce(lcm, numbers, 1)

class ApplicationData:
  def __init__(self):
		self.Topics = ["Arithmetic", "Fractions", "Algebra I","Quadratic Equations"]
		self.SubTopics = [["Addition Pairs","Addition Pairs + 1","Simple Addition"], ["Greatest Common Divisor","Least Common Multiple","Fraction Addition"], ["Isolate Variable","Evaluate Expressions I","Squares and Square Roots"],["Number of Roots", "Factor Quadratic Expressions", "Find Vertex", "Quadratic Formula"]]
		self.SpecialCode = [["Addition_Pairs","Addition_Pairs_Plus_One","Simple_Addition"],["Greatest_Common_Divisor","Lowest_Common_Multiple","Fraction_Addition"],["Isolate","Evaluate","Squares_and_Square_roots"],["Number_of_Roots", "Factor_Quadratic_Expressions", "Find_Vertex", "Quadratic_Formula"]]
		self.topicChoice = -1
		self.subtopicChoice = -1
class AnswerObject:
	def __init__(self): 
		pass

#Eventually: Export the Special Problem Code to a separate module
#Let SpecialProblemCode Pass OBJECTS....
class SpecialProblemCode:
#This class collects special functions associated with each type of problem
	#Instead of a range set, receive a difficulty level here, mapping it to a range set with a dictionary

#####################################################################################################################
# Arithmetic
#####################################################################################################################


	def addition_pairs_SC(self, difficulty_level):	
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		print RangeSet
		AO = AnswerObject()
		#Ensure that only one variable is chosen instead of two
		self.NumQuestions = 20
		AO.N = []
		AO.N.append(GetVariable("Integer", RangeSet))
		AO.N.append(AO.N[0])
		AO.Latex = "* + *"
		AO.Answer = 2*AO.N[0]
		AO.Operator = "+"
		return AO		
	def Addition_Pairs_Plus_One(self, difficulty_level):
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                print RangeSet
                AO = AnswerObject()
                #Ensure that only one variable is chosen instead of two
                self.NumQuestions = 20
                AO.N = []
                AO.N.append(GetVariable("Integer", RangeSet))
                AO.N.append(AO.N[0]+1)
                AO.Latex = "* + *"
                AO.Answer = 2*AO.N[0]+1
                AO.Operator = "+"
                return AO

	def Simple_Addition(self, difficulty_level):
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
		AO = AnswerObject()
		AO.N = []
		for i in range(0,2):
			AO.N.append(GetVariable("Integer", RangeSet))
		AO.Operator = "+"
		#Perhaps define an object to return - with the number of questions included
		AO.Latex = "*+*="
		#AO.AdjustSign: Adjust Addition Operator for negative numbers
		AO.AdjustSign = False
		AO.Answer = sum(AO.N)
                return AO

	def Vertical_Addition(self,difficulty_level):
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
		AO = AnswerObject()
		for i in range(0,2):
			AO.N.append(GetVariable("Integer", RangeSet))
		AO.Operator = "+"

		AO.Latex =  "\frac{\begin{array}[b]{r}\left( * \right)\\\plus \left( * \right)\end{array}{\left( y_1y_2y_3y_4 \right)}"
		AO.AdjustSign = False
		AO.Answer = sum(AO.N)
		return AO

###################################################################################################################
# Fractions
###################################################################################################################

	def Greatest_Common_Divisor(self, difficulty_level):
		Difficulty_Lookup = {0:(2,10), 1:(2,12), 2:(2,15)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
		AO = AnswerObject()
		AO.N = []
		q = GetVariable("Integer", RangeSet)
		for i in range(0,2):
			AO.N.append(GetVariable("Integer", RangeSet)*q)
		AO.Operator = "" 
		AO. Latex = "GCD( * , * )"
		AO.AdjustSign = False
		AO.Answer = gcd(AO.N[0], AO.N[1])
		return AO

	def Least_Common_Multiple(self, difficulty_level):
		Difficulty_Lookup = {0:(2,10), 1:(2,12), 2:(2,15)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
		AO = AnswerObject()
		AO.N = []
		for i in range(0,2):
			AO.N.append(GetVariable("Integer", RangeSet))
		AO.Operator = "" 
		AO. Latex = "LCM( * , * )"
		AO.AdjustSign = False
		AO.Answer = lcm(AO.N[0], AO.N[1])
		return AO

	def Fraction_Addition(self, difficulty_level):
		Difficulty_Lookup = {0:(2,5),1:(2,8),2:(2,10),3:(2,12),4:(2,15),5:(2,20)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		AO = AnswerObject()
		AO.N = []
		for i in range(0,2):
			AO.N.append(GetVariable("Fraction", RangeSet))
		if AO.N[1].numerator*AO.N[1].denominator >= 0:
			sign = "+"
		else:
			sign = "-"
		AO.Latex = "\\frac{"+str(AO.N[0].numerator) +"}{"+str(AO.N[0].denominator)+"}"+sign+"\\frac{"+str(AO.N[1].numerator) +"}{"+str(AO.N[1].denominator)+"}"
                AO.Operator = "+"
		AO.Answer = AO.N[0] + AO.N[1]
                return AO
###################################################################################################################
# Quadratics
###################################################################################################################


	def Number_of_Roots(self, difficulty_level):
		Difficulty_Lookup = {0:(-10,10),1:(-100,100)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		AO = AnswerObject()
		AO.Latex = "* x^2 * x * "
		AO.N = []
		AO.Operator = ""
		if difficulty_level == 0:
			VariableType = "Integer"
		else:
			VariableType = "Float"
		for i in range(0,3):
			AO.N.append(GetVariable(VariableType, RangeSet))
		Delta = AO.N[1]*AO.N[1]-4*AO.N[0]*AO.N[2]
		if Delta > 0:
			AO.Answer = 2
		elif Delta == 0:
			AO.Answer = 1
		else:
			AO.Answer = 0
		return AO
		
	def Factor_Quadratic_Expressions(self,difficulty_level):
		#A = 1
		Difficulty_Lookup = {0:(-10,10),1:(-12,12)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		AO = AnswerObject()
		AO.Latex = "* x^2 * x * "
		AO.N = []
		AO.Operator = ""
		Roots = []
		for i in range(0,2):
			Roots.append(GetVariable("Integer", RangeSet))
		A = 1
		B = Roots[0]+Roots[1]
		C = Roots[0]*Roots[1]	
		AO.N.append(A)
		AO.N.append(B)
		AO.N.append(C)
		AO.Answer = Roots
		return AO


	def Quadratic_Formula(self, difficulty_level):
		Difficulty_Lookup = {0:(-10,10),1:(-12,12)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                AO = AnswerObject()
                AO.Latex = "* x^2 * x * "
                AO.N = []
                AO.Operator = ""
                Roots = []
                for i in range(0,3):
                        AO.N.append(GetVariable("Integer", RangeSet))
		A = AO.N[0]
		B = AO.N[1]
		C = AO.N[2]
		if A==0:
			A=1
			AO.N[0] =1

		Delta = B**2-4*A*C
		if Delta < 0:
			AO.Answer = "No Roots"
		if Delta == 0: 
			Root = (-B)/(2*A)
			AO.Answer = Root
		if Delta >0:		
			Root1 = (-B + sqrt(B**2-4*A*C))/(2*A)
			Root2 = (-B - sqrt(B**2-4*A*C))/(2*A)
                	AO.Answer = [Root1, Root2]
                return AO

################################################################################################################################
# Additional Classes
################################################################################################################################
class Topic:
	def __init__(self,name):
		self.TopicName = name
		self.Problems = []
		self.questions_per_line = 0
		self.SPC = SpecialProblemCode()
	def AddProblems(self, name, difficulty_level,special_code):
		self.Problems.append(Problem(name,difficulty_level,special_code))


class Problem:
	def __init__(self, name,difficulty_level,special_code):
		self.ProblemName = name
		self.QuestionForms = []
		#Add different types of question forms later using some over-riding
		self.QuestionForms.append(QuestionForm(difficulty_level,special_code))
		SPC_Problem = SpecialProblemCode()
		
class QuestionForm:
	def __init__(self, difficulty_level,special_code):
		self.Variables = []
		self.Difficulty_Level = difficulty_level
		#Execute special code here for each question type? Variables need to be selected according to requirements for each section.
		#for i in range(0,len(variable_set)):
		#	self.Variables.append(GetVariable(variable_set[i],variable_range_set[i]))
		#This is to be removed??? - causes difficulties when defined low in the 
		#object hierarchy.
		SPC = SpecialProblemCode()
		GetVariablesFunction = {"Addition_Pairs": SPC.addition_pairs_SC(self.Difficulty_Level), "Addition_Pairs_Plus_One":SPC.Addition_Pairs_Plus_One(self.Difficulty_Level), "Simple_Addition":SPC.Simple_Addition(self.Difficulty_Level),"Number_of_Roots":SPC.Number_of_Roots(self.Difficulty_Level), "Factor_Quadratic_Expressions":SPC.Factor_Quadratic_Expressions(self.Difficulty_Level), "Greatest_Common_Divisor": SPC.Greatest_Common_Divisor(self.Difficulty_Level), "Lowest_Common_Multiple":SPC.Least_Common_Multiple(self.Difficulty_Level), "Fraction_Addition": SPC.Fraction_Addition(self.Difficulty_Level), "Quadratic_Formula":SPC.Quadratic_Formula(self.Difficulty_Level)}
		
		#self.Variables is of the form [operator, Number1, Number2] The operator is arithmetic and in quotes. N1 and N2 are integers
		self.ProblemObject = GetVariablesFunction[special_code]
		#The following code appears relevant only for arithmetic questions...
		if self.ProblemObject.Operator in ("+", "-", "*", "/"):
			self.Format_String = "*"+self.ProblemObject.Operator+"*= "
			self.Equation_String = self.Create_Equation_String(self.Format_String, self.ProblemObject.N,0)
		if self.ProblemObject.Operator == "":
			self.Format_String = self.ProblemObject.Latex
			self.Equation_String = self.Create_Equation_String(self.Format_String, self.ProblemObject.N,1)
		self.SpecialCode = special_code
		self.Answers = self.ProblemObject.Answer
			
		#print "New QF:", self.Variable_Set, self.Variables
		
	
	def GetArithmeticAnswer(self, variables):
		#variables[0] should be the arithmetic operator; [1] and [2] are the numbers
		if variables[0] == "+":
			Answer = variables[1] + variables[2]
		
		if variables[0] == "-":
			Answer = variables[1] - variables[2]

		if variables[0] == "x":
			Answer = variables[1] * variables[2]

		if variables[0] == "/":
			Answer = variables[1] / variables[2]
		return Answer

	def Parse_Format_String(self,String1):
		String2 = String1.split("*")
		return String2

	def Create_Equation_String(self, String1, Variables, SignFlag):
		print String1
		print Variables
		ParsedStringArray = self.Parse_Format_String(String1)
		print ParsedStringArray
		ParsedString = ParsedStringArray[0]
		for i in range(1,len(ParsedStringArray)):
			'''print i, ".."
			print Variables, "..."
			print Variables[i-1] '''
			Variable = Variables[i-1]
			#Add in a + sign for positive outcomes
			if SignFlag == 1:
				if Variable >0:
					VariableString = "+"+str(Variable)
				elif Variable == 0 :
					VariableString = ""
				else:
					VariableString = str(Variable)
			else:
				VariableString = str(Variable)
			ParsedString += VariableString
			ParsedString += ParsedStringArray[i]
		return ParsedString

class NumberRange:
	def __init__(self, Min, Max=False,notallowed=False):
		#This function can take a tuple in which case Max is set to false.
		#Otherwise, it takes two values to set the range
		#Optionally, the function can take a list indicating all values not allowed; for later implementation
		if Max == False:
			self.Minimum = Min[0]
			self.Maximum = Min[1]
		else:
			self.Minimum = Min
			self.Maximum = Max
		self.NotAllowed = notallowed
		print "The range has been initialized"


##########################################################################
#Base Functions:
##########################################################################
def AllowedCheck(number,notallowed):
#Takes a list, not allowed, and checks the number against integers and ranges within the list
	return False

def GetVariable(VariableType, RangeSet, notallowed=False):
	#Return A Random Variable of the Given Type in the Given RangeSet.
	print VariableType
	if VariableType == "Integer":
		#Incorporate a notallowed routine here checking individual numbers and ranges of numbers
		return randint(RangeSet.Minimum, RangeSet.Maximum)
	elif VariableType == "Fraction":
		a1 = randint(RangeSet.Minimum, RangeSet.Maximum)
		a2 = 0
		while a2 == 0 and a2 <> a1:
			a2 = randint(RangeSet.Minimum, RangeSet.Maximum)
		return Fraction(a1,a2)
	else:
		return uniform(RangeSet.Minimum, RangeSet.Maximum)

def MakeLatexEquation(string1):
	return "\\begin{equation}"+string1+"\\nonumber\\end{equation}"

#Function to count stars within a string
def CountStars(String1):
	Count=0
	for i in range(0,len(String1)):
		if String1[i] == "*":
			Count+=1
	return Count


##############################################################################
#Testing Area:
##############################################################################
'''
#May 3: Need to add special code; need to generate multiple question_forms for each problem; need to interface with Latex
T1 = Topic("Arithmetic")
T1.Difficulty_Levels = []
T1.VariableTypes = []
for i in range(0,6):
	T1.Difficulty_Levels.append(i)
	T1.VariableTypes.append(["Integer", "Integer"])

T1. AddProblems("Addition Pairs", ["+"]*6, T1.VariableTypes, T1.Difficulty_Levels,["addition_pairs_SC"]*6)
print T1.Problems
print T1.Problems[0].QuestionForms[0].Format_String
for i1 in range(0,len(T1.Problems)):
	for i2 in range(0,len(T1.Problems[i1].QuestionForms)):	
		T1.Problems[i1].QuestionForms[i2].Parsed_String = T1.Problems[i1].QuestionForms[i2].Create_Equation_String(T1.Problems[i1].\
QuestionForms[i2].Format_String,T1.Problems[i1].QuestionForms[i2].Variables, 0)
#for i in range(0,len(T1.VariableTypes)):
#	T1.Problems[0].QuestionForms[0].Answers.append(T1.Problems[0].QuestionForms[0].GetArithmeticAnswer(T1.Problems[0].QuestionForms[0].Variables,T1.Problems[0].QuestionForms[0].Operator))
for i1 in range(0,len(T1.Problems)):
	for i2 in range(0,len(T1.Problems[i1].QuestionForms)):
		print T1.Problems[i1].QuestionForms[i2].Parsed_String
		print T1.Problems[i1].QuestionForms[i2].Answers

#print T1.Problems[0].QuestionForms[0].Parsed_String
#print T1.Problems[0].QuestionForms[0].Answers
'''
