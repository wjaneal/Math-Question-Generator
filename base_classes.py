##########################################################################
#Base Classes for Python Automatic Question Generation Program
##########################################################################
from random import *
class ApplicationData:
  def __init__(self):
		self.Topics = ["Arithmetic", "Fractions", "Algebra I"]
		self.SubTopics = [["Addition Pairs","Addition Pairs + 1","Simple Addition"], ["Greatest Common Divisor","Least Common Multiple","Fraction Addition"], ["Isolate Variable","Evaluate Expressions I","Squares and Square Roots"]]
		self.topicChoice = -1
		self.subtopicChoice = -1

#Eventually: Export the Special Problem Code to a separate module
class SpecialProblemCode:
#This class collects special functions associated with each type of problem
	#Instead of a range set, receive a difficulty level here, mapping it to a range set with a dictionary
	def addition_pairs_SC(self, difficulty_level):	
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		print RangeSet
		#Ensure that only one variable is chosen instead of two
		number = GetVariable("Integer", RangeSet)
		AnswerArray = [number, number]
		return AnswerArray		
		


class Topic:
	def __init__(self,name):
		self.TopicName = name
		self.Problems = []
		self.questions_per_line = 0

	def AddProblems(self, name, difficulty_level,special_code):
		self.Problems.append(Problem(name,difficulty_level,special_code))


class Problem:
	def __init__(self, name,difficulty_level,special_code):
		self.ProblemName = name
		self.QuestionForms = []
		#Add different types of question forms later using some over-riding
		self.QuestionForms.append(QuestionForm(difficulty_level,special_code))
		
class QuestionForm:
	def __init__(self, difficulty_level,special_code):
		self.Variables = []
		self.Difficulty_Level = difficulty_level
		#Execute special code here for each question type? Variables need to be selected according to requirements for each section.
		#for i in range(0,len(variable_set)):
		#	self.Variables.append(GetVariable(variable_set[i],variable_range_set[i]))
		SPC = SpecialProblemCode()
		GetVariablesFunction = {"addition_pairs_SC": SPC.addition_pairs_SC(self.Difficulty_Level)}
		self.Variables = GetVariablesFunction[special_code]
		self.Format_String = "*"+self.Operator+"*= "
		self.Parsed_String = ""
		self.SpecialCode = special_code
		self.Answers = self.GetArithmeticAnswer(self.Variables,self.Operator)
		
		print "New QF:", self.Variable_Set, self.Variables
		
	
	def GetArithmeticAnswer(self, variables, operator):
		print operator, variables, ",,,,,,"
		if operator == "+":
			Answer = variables[0] + variables[1]
		
		if operator == "-":
			Answer = variables[0] - variables[1]

		if operator == "x":
			Answer = variables[0] * variables[1]

		if operator == "/":
			Answer = variables[0] / variables[1]
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
