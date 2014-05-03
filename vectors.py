'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

from base_classes import *
from visual import *

#Define Vector Magnitude Questions
def Vector_Magnitude():
	Range1 = NumberRange(-10,10)
	EquationString = "\\vec{a} = [*,*,*]"
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet,RangeSet)
	QuestionString = Q1.Create_Equation_String(Q1.Format_String,0)
	Answer = mag(vector(float(Q1.Variables[0]),float(Q1.Variables[1]),float(Q1.Variables[2])))
	AnswerString = "\\lvert\\vec{a}\\rvert \\approx "+"%.2f" % (Answer) + ""
	AnswerString = MakeLatexEquation(AnswerString)
	QuestionString = MakeLatexEquation(QuestionString)
	return [QuestionString, AnswerString]

#Define Dot Product Questions
def Dot_Product():
	Range1=NumberRange(-10,10)
	EquationString = "\\vec{a} = [*,*,*]\\\\\\vec{b} = [*,*,*]\\\\\\vec{a} \cdot \\vec{b} = "
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet, RangeSet)
	QuestionString = Q1.Create_Equation_String(Q1.Format_String,0)
	A = vector(0.0,0.0,0.0)
	B = vector(0.0,0.0,0.0)
	for i in range(0,3):
		A[i] = float(Q1.Variables[i])
		B[i] = float(Q1.Variables[i+3])
	Answer = dot(A,B)
	AnswerString = "\\vec{a} \cdot \\vec{b} = "+str(Answer)
	AnswerString = MakeLatexEquation(AnswerString)
	QuestionString = MakeLatexEquation(QuestionString)
	return [QuestionString, AnswerString]

#Define Cross Product Questions
def Cross_Product():
	Range1=NumberRange(-10,10)
	EquationString = "\\vec{a} = [*,*,*]\\\\\\vec{b} = [*,*,*]\\\\\\vec{a} \\times \\vec{b} = "
	NumVariables = CountStars(EquationString)
	RangeSet = NumVariables*[Range1]
	VariableSet = NumVariables*["Integer"]
	Q1 = QuestionForm(EquationString, VariableSet, RangeSet)
	QuestionString = Q1.Create_Equation_String(Q1.Format_String,0)
	A = vector(0.0,0.0,0.0)
	B = vector(0.0,0.0,0.0)
	for i in range(0,3):
		A[i] = float(Q1.Variables[i])
		B[i] = float(Q1.Variables[i+3])
	Answer = cross(A,B)
	AnswerString = "\\vec{a} \\times \\vec{b} = ["+str(Answer[0])+","+str(Answer[1])+","+str(Answer[2])+"]"
	AnswerString = MakeLatexEquation(AnswerString)
	QuestionString = MakeLatexEquation(QuestionString)
	return [QuestionString, AnswerString]
