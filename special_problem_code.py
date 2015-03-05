'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

########################################################################
#Special Problem Code for Python Automatic Question Generation Program
##########################################################################
#from random import *
#from fractions import *
#from math import *
#import inspect

from base_classes import *
from arithmetic_functions import *
#from Polynomials import *


#This class collects special functions associated with each type of problem
        #Instead of a range set, receive a difficulty level here, mapping it to a range set with a dictionary


class SpecialProblemCode:
        def __init__(self):
                pass

#####################################################################################################################
# Arithmetic
#####################################################################################################################


        def AR_Addition_Pairs(self, difficulty_level):  
                Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                print RangeSet
                AO = AnswerObject()
                #Ensure that only one variable is chosen instead of two
                self.NumQuestions = 20
                AO.Title = "Addition Pairs"
                AO.Instructions = "Addition Pairs - Add the pairs of integers."
                AO.N = []
                AO.N.append(GetVariable("Integer", RangeSet))
                AO.N.append(AO.N[0])
                AO.Latex = "* + *"
                AO.Answer = 2*AO.N[0]
                AO.Operator = "+"
                return AO               
        
	def AR_Addition_Pairs_Plus_One(self, difficulty_level):
                Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                print RangeSet
                AO = AnswerObject()
                #Ensure that only one variable is chosen instead of two
                self.NumQuestions = 20
		AO.Title = "Addition Pairs Plus One"
		AO.Instructions = "Addition - Add the Integers"
                AO.N = []
                AO.N.append(GetVariable("Integer", RangeSet))
                AO.N.append(AO.N[0]+1)
                AO.Latex = "* + *"
                AO.Answer = 2*AO.N[0]+1
                AO.Operator = "+"
                return AO

        def AR_Simple_Addition(self, difficulty_level):
                Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
		AO.Title = "Simple Addition"
		AO.Instructions = "Addition - Add the Integers"
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

	def AR_Simple_Subtraction(self, difficulty_level):
		Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
	        RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
	        self.NumQuestions = 20
	        AO = AnswerObject()
	        AO.Title = "Simple Addition"
	        AO.Instructions = "Addition - Add the Integers"
	        AO.N = []
	        Var1 = GetVariable("Integer", RangeSet)
		Var2 = GetVariable("Integer", RangeSet)
		a = max(Var1,Var2)
		b = min(Var1, Var2)
		AO.N.append(a)
		AO.N.append(b)
	        AO.Operator = "-"
	                #Perhaps define an object to return - with the number of questions included
	        AO.Latex = "*-*="
	        #AO.AdjustSign: Adjust Addition Operator for negative numbers
	        AO.AdjustSign = False
	        AO.Answer = b-a
	        return AO



        def AR_Vertical_Addition(self,difficulty_level):
                Difficulty_Lookup = {0:(0,5),1:(0,8),2:(0,10),3:(0,12),4:(0,15),5:(0,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
                AO.N = []
		AO.Title = "Vertical Addition"
		AO.Instructions = "Add the Integers"
                for i in range(0,2):
                        AO.N.append(GetVariable("Integer", RangeSet))
                AO.Operator = ""

                AO.Latex =  "\\begin{array}{r}\\mbox{"+str(AO.N[0])+"}\\\\\\uline{\\mbox{"+str(AO.N[1])+"}}\\end{array}" 
                AO.Answer =  "\\begin{array}{r}\\mbox{"+str(AO.N[0])+"}\\\\\\mbox{"+str(AO.N[1])+"}\\\\\\mbox{"+str(sum(AO.N))+"}\\end{array}" 
                AO.AdjustSign = False
                AO.AdjustSign = False
                return AO

        def AR_Multiplication(self,difficulty_level):
                Difficulty_Lookup = {0:(2,10),1:(2,8),2:(2,10),3:(2,12),4:(2,15),5:(2,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
		AO.Title = "Multiplication"
		AO.Instructions = "Multiply the Integers"
                AO.N = []
                for i in range(0,2):
                        AO.N.append(GetVariable("Integer", RangeSet))
                AO.Operator = "\\times"

                AO.Latex =  "*X* = "
                AO.AdjustSign = False
                AO.Answer = AO.N[0]*AO.N[1]
                return AO

        def AR_Percents(self,difficulty_level):
                Difficulty_Lookup = {0:(2,10),1:(2,8),2:(2,10),3:(2,12),4:(2,15),5:(2,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
		AO.Title = "Percents"
		AO.Instructions = "Convert the Given Fractions to Percentages"
                AO.N = []
                for i in range(0,2):
                        AO.N.append(GetVariable("Integer", RangeSet))
		if AO.N[1] < AO.N[0]:
			temp = AO.N[0]
			AO.N[0] = AO.N[1]
			AO.N[1] = temp
		AO.Operator = ""
                AO.Latex =  "\\dfrac{"+str(AO.N[0])+"}{"+str(AO.N[1])+"}"
		AO.Answer = (1.0*AO.N[0])/(1.0*AO.N[1])
		return AO

###################################################################################################################
# Fractions
###################################################################################################################
	def FR_Prime_Factorization(self, difficulty_level):
		Difficulty_Lookup = {0:(5, 20), 1:(20, 50), 2: (25,100), 3: (50,250)}
		RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
		AO = AnswerObject()
		AO.N = []
		AO.Title = "Prime Factorization"
		AO.Instructions = "Find the prime factorization of the given integers."
		q = GetVariable("Integer", RangeSet)
		AO.N.append(q)
		AO.Operator = ""
		AO.Latex = "*"
		AO.AdjustSign = False
		AO.Answer = Prime_Factorization(q)
		return AO

        def FR_Greatest_Common_Divisor(self, difficulty_level):
                Difficulty_Lookup = {0:(2,10), 1:(2,12), 2:(2,15), 3:(2,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
                AO.N = []
		AO.Title = "Greatest Common Divisor"
		AO.Instructions = "Find the greatest common divisor (GCD) of the two numbers"
                q = GetVariable("Integer", RangeSet)
                for i in range(0,2):
                        AO.N.append(GetVariable("Integer", RangeSet)*q)
                AO.Operator = "" 
                AO.Latex = "GCD( * , * )"
                AO.AdjustSign = False
                AO.Answer = gcd(AO.N[0], AO.N[1])
                return AO

        def FR_Least_Common_Multiple(self, difficulty_level):
                Difficulty_Lookup = {0:(2,10), 1:(2,12), 2:(2,15),3:(2,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                self.NumQuestions = 20
                AO = AnswerObject()
                AO.N = []
		AO.Title = "Least Common Multiple"
		AO.Instructions = "Find the least common multiple (LCM) of the two integers"
                for i in range(0,2):
                        AO.N.append(GetVariable("Integer", RangeSet))
                AO.Operator = "" 
                AO. Latex = "LCM( * , * )"
                AO.AdjustSign = False
                AO.Answer = lcm(AO.N[0], AO.N[1])
                return AO

        def FR_Fraction_Addition(self, difficulty_level):
                Difficulty_Lookup = {0:(2,5),1:(2,8),2:(2,10),3:(2,12),4:(2,15),5:(2,20)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
                AO = AnswerObject()
                AO.N = []
		AO.Title = "Fraction Addition"
		AO.Instructions = "Add the given fractions"
                for i in range(0,2):
                        AO.N.append(GetVariable("Fraction", RangeSet))
                if AO.N[1].numerator*AO.N[1].denominator >= 0:
                        sign = "+"
                else:
                        sign = "-"
                AO.Latex = "\\dfrac{"+str(AO.N[0].numerator) +"}{"+str(AO.N[0].denominator)+"}"+sign+"\\dfrac{"+str(AO.N[1].numerator) +"}{"+str(AO.N[1].denominator)+"}"
                AO.Operator = ""
                AO.Answer = "\\dfrac{"+str((AO.N[0] + AO.N[1]).numerator)+ "}{"+str((AO.N[0] + AO.N[1]).denominator)+"}"
                return AO
###################################################################################################################
# Quadratics
###################################################################################################################


        def QU_Number_of_Roots(self, difficulty_level):
                Difficulty_Lookup = {0:(-10,10),1:(-100,100), 2:(-200,200), 3:(-250,250)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
                AO = AnswerObject()
                AO.Latex = "* x^2 * x * "
                AO.N = []
		AO.Title = "Number of Roots"
		AO.Instructions = "Find the number of roots of the given quadratic equation"

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
                
        def QU_Factor_Quadratic_Expressions(self,difficulty_level):
                #A = 1
                Difficulty_Lookup = {0:(-10,10),1:(-12,12),2:(-15,15),3:(-18,18)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20                
		AO = AnswerObject()
                AO.Latex = "* x^2 * x * "
                AO.N = []
		AO.Title = "Factor Quadratic Expressions"
		AO.Instructions = "Factor the given quadratic expressions"
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


        def QU_Quadratic_Formula(self, difficulty_level):
                Difficulty_Lookup = {0:(-10,10),1:(-12,12), 2:(-15,15), 3:(-18,18)}
                RangeSet = NumberRange(Difficulty_Lookup[difficulty_level])
		self.NumQuestions = 20
                AO = AnswerObject()
                AO.Latex = "* x^2 * x * "
                AO.N = []
		AO.Title = "Quadratic Formula"
		AO.Instructions = "Find the root(s), if any, using the quadratic formula"
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
##############################################################################################################
# Algebra
##############################################################################################################
'''	def AL_Add_Polynomials(self, difficulty_level):
		RangeSet = NumberRange(-10,10)
		AO = AnswerObject()
		AO.Latex = "* "
		AO.Title = "Polynomials - Addition"
		AO.Instructions = "Add the given polynomials"
		AO.N = []
		for i in range(0, difficulty_level+2):
			AO.N.append(GetVariable("Integer", RangeSet))
		PolyObject = Polynomial(difficulty_level+2)
		B = PolyObject.Polynomial(difficulty_level+2)
		AO.Answer = PolyAdd(A,B)
		AO.AnswerLatex = GenerateLatexString(AO.Answer)
		return AO
'''
class ApplicationData:
        def __init__(self):
                self.topicChoice = -1
                self.subtopicChoice = -1

class AnswerObject:
        def __init__(self): 
                pass


