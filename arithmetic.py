'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

#Arithmetic Module for Python Math Question Generator
from base_classes import *

class Question(QuestionForm):
  def __init__(self, form_string, var_set, range_set, equation_string ):
		self.Range = NumberRange(0,10)
		self.EquationString = equation_string
		self.NumVariables = CountStars(self.EquationString)
		self.RangeSet = self.NumVariables*[self.Range]
		self.VariableSet = self.NumVariables*["Integer"]
		self.Q1 = QuestionForm(self.EquationString, self.VariableSet)
		self.QuestionString = self.Q1.Create_Equation_String(self.EquationString,0)
		self.Q1.Variables[1] = self.Q1.Variables[0]
		self.QuestionString = str(self.Q1.Variables[0]) + "+" + str(self.Q1.Variables[1]) + "= "
		self.Answer = int(self.Q1.Variables[0]) + int(self.Q1.Variables[1])
		return [QuestionString, AnswerString]
def Addition_Pairs():
	print "Addition"
	Range1 = NumberRange(0,10)
	EquationString = "*+*="
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Q1.Variables[1] = Q1.Variables[0]
	QuestionString = str(Q1.Variables[0]) + "+" + str(Q1.Variables[1]) +"= "
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = QuestionString+str(Answer)
	return [QuestionString, AnswerString]

def Addition_Pairs_Plus_1():
	Range1 = NumberRange(0,10)
	EquationString = "*+*="
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Q1.Variables[1] = Q1.Variables[0]+1
	QuestionString = str(Q1.Variables[0]) + "+" + str(Q1.Variables[1]) +"= "
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = QuestionString+"= "+str(Answer)
	return [QuestionString, AnswerString]

def Simple_Addition():
	Range1 = NumberRange(0,12)
	EquationString = "*+*="
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = QuestionString+str(Answer)
	return [QuestionString, AnswerString]

def Addition_to_15():
	Range1 = NumberRange(0,15)
	EquationString = "*+*="
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = "QuestionString"+str(Answer)
	return [QuestionString, AnswerString]

def Addition_to_20():
	Range1 = NumberRange(0,20)
	EquationString = "*+*="
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = "\\QuestionString"+str(Answer)
	return [QuestionString, AnswerString]

def Vert_Addition_to_20():
	Range1 = NumberRange(0,9)
	EquationString = "\[\\begin{array} & \hspace ** \\ & +** \\ \cline{2-2} \end{array}\]"
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(EquationString,0)
	Answer = int(Q1.Variables[0])+int(Q1.Variables[1])
	AnswerString = "\\QuestionString"+str(Answer)
	return [QuestionString, AnswerString]



#Organize the data connected with each of the functions
Num_Questions_Array = [0,69,69,69,69,69, 18]
Num_Columns_Array = [0,3,3,3,3,3,3]
Line_Length_Array = [75,75,75,75,75,0,0]
Arith_QA_Function = {1:Addition_Pairs, 2:Addition_Pairs_Plus_1, 3:Simple_Addition, 4:Addition_to_15, 5:Addition_to_20, 6:Vert_Addition_to_20}
Arith_Function_Name = {1:"Addition Pairs", 2:"Addition Pairs Plus One", 3:"Addition to 12", 4:"Addition to 15", 5:"Addition to 20", 6:"Vertical Addition to 20"}

