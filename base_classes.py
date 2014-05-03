'''
Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

##################################################################################
#Base Classes and Functions for Python Automatic Question Generation Program
##########################################################################

import special_problem_code
import inspect
from math import *
from random import *
from fractions import *

def lcm(a, b):
        return (a * b) // gcd(a, b)
        return reduce(lcm, numbers, 1)



################################################################################################################################
# Additional Classes
################################################################################################################################
class Topic:
        def __init__(self,name):
                self.TopicName = name
                self.Problems = []
                self.questions_per_line = 0
                self.SPC = special_problem_code.SpecialProblemCode()
        def AddProblems(self, name, difficulty_level,special_code):
                self.Problems.append(Problem(name,difficulty_level,special_code))


class Problem:
        def __init__(self, name,difficulty_level,special_code):
                self.ProblemName = name
                self.QuestionForms = []
                #Add different types of question forms later using some over-riding
                self.QuestionForms.append(QuestionForm(difficulty_level,special_code))
                SPC_Problem = special_problem_code.SpecialProblemCode()
                
class QuestionForm:
        def __init__(self, difficulty_level,special_code):
                self.Variables = []
                self.Difficulty_Level = difficulty_level
                #Execute special code here for each question type? Variables need to be selected according to requirements for each section.
                #This is to be removed??? - causes difficulties when defined low in the 
                #object hierarchy.
                SPC = special_problem_code.SpecialProblemCode()
                ProblemNames = inspect.getmembers(SPC, predicate=inspect.ismethod)
                #print ProblemNames
                GetVariablesFunction = {}
                for i in range(0,len(ProblemNames)):
                        if ProblemNames[i][0] != "__init__":
                                GetVariablesFunction[ProblemNames[i][0]] = ProblemNames[i][1](difficulty_level) 
                
                self.ProblemObject = GetVariablesFunction[special_code]
                #The following code appears relevant only for arithmetic questions...
                if self.ProblemObject.Operator in ("+", "-", "\\times", "/"):
                        self.Format_String = "*"+self.ProblemObject.Operator+"*= "
                        self.Equation_String = self.Create_Equation_String(self.Format_String, self.ProblemObject.N,0)
                if self.ProblemObject.Operator == "":
                        self.Format_String = self.ProblemObject.Latex
                        self.Equation_String = self.Create_Equation_String(self.Format_String, self.ProblemObject.N,1)
                self.SpecialCode = special_code
                print self.ProblemObject.__dict__
                self.Answers = self.ProblemObject.Answer
                #self.Title = self.ProblemObject.Title
                #self.Instructions = self.ProblemObject.Instructions
                        
                #print "New QF:", self.Variable_Set, self.Variables
                
        
        def GetArithmeticAnswer(self, variables):
                #variables[0] should be the arithmetic operator; [1] and [2] are the numbers
                if variables[0] == "+":
                        Answer = variables[1] + variables[2]
                
                if variables[0] == "-":
                        Answer = variables[1] - variables[2]

                if variables[0] == "\\times":
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
                        print i, ".."
                        print Variables, "..."
                        print Variables[i-1] 
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
                #print "The range has been initialized"


##########################################################################
#Base Functions:
##########################################################################
def AllowedCheck(number,notallowed):
#Takes a list, not allowed, and checks the number against integers and ranges within the list
        return False

def GetVariable(VariableType, RangeSet, notallowed=False):
        #Return A Random Variable of the Given Type in the Given RangeSet.
        #print VariableType
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
#       T1.Problems[0].QuestionForms[0].Answers.append(T1.Problems[0].QuestionForms[0].GetArithmeticAnswer(T1.Problems[0].QuestionForms[0].Variables,T1.Problems[0].QuestionForms[0].Operator))
for i1 in range(0,len(T1.Problems)):
        for i2 in range(0,len(T1.Problems[i1].QuestionForms)):
                print T1.Problems[i1].QuestionForms[i2].Parsed_String
                print T1.Problems[i1].QuestionForms[i2].Answers

#print T1.Problems[0].QuestionForms[0].Parsed_String
#print T1.Problems[0].QuestionForms[0].Answers
'''
