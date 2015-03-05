'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

from random import *
from math import *
#Polynomial:
#List of Coefficients
#Predetermined Roots

#Notes:
#Generate a factoring question - second order polynomial
# Latex Output: (x-r1)*(x-r2) where r1 and r2 are two roots chosen within the ranges set by the program
#Format string "(x-*)(x-*)"
#RandomNumbersArray [r1,r2]
#Parsed Format String Array: ["(x-",")(x-",")"]
#LatexOutput Places this all together



class Polynomial:
	def __init__(self,order, coefficients=[]):	
		self.Order = order
		if len(coefficients) == 0:
			self.Coefficients = self.Generate_Random_Coefficients(order)
		else:
			self.Coefficients = coefficients
		self.Derivative = self.Differentiate(self.Coefficients)
		self.SecondDerivative = self.Differentiate(self.Derivative)

	def Generate_Latex_String(self, A):
		print A
		A_Order= len(A)
		if A[A_Order-1] == 0:	
			String1 = ""
		elif A[A_Order-1] == 1:
			String1 = "x^{"+str(A_Order-1)+"}"
		else:
			String1 = str(A[A_Order-1])+"x^{"+str(A_Order-1)+"}"
		for i in range(A_Order-2,-1,-1):
			if A[i]>0:
				String1 +="+"+str(A[i])
				
			elif A[i] == 0:
				pass
			else:
				String1 +=str(A[i])
			if i>1:
				String1+= "x^{"+str(i)+"}"
			if i == 1:
				String1+="x"
			
		print String1
		return String1

	def PolyAdd(self, A,B):
		A_Order = len(A)
		B_Order = len(B)
		Order = max(A_Order,B_Order)
		Sum = [0]*Order
		for i in range(0,len(A)):
			Sum[i]+=A[i]
		for i in range(0,len(B)):
			Sum[i]+=B[i]
		return Sum


	def PolyMult(self, A,B):
		A_Order = len(A)
		B_Order = len(B)
		Product = [0]*(A_Order+B_Order-1)
		for i in range(0,A_Order):
			for j in range(0,B_Order):
				Product[i+j]+=A[i]*B[j]
		return Product

	def Differentiate(self, A):
		A_Order = len(A)
		Derivative = []
		for i in range(1,len(A)):
			Derivative.append(A[i]*i)
		return Derivative
				
	def GenerateIntRoots(self,Range):
		self.Roots = []
		Max = Range.Maximum
		Min = Range.Minimum
		ValueRange = Max-Min+1
		
		for i in range(0,self.Order):	
			self.Roots.append(int(random()*ValueRange)+Min)
			print (self.Roots)

	def GenerateCoefficients(self):
		print self.Roots, " roots"
		self.Coefficients = [-self.Roots[0],1]	
		print self.Coefficients
		for i in range(1, len(self.Roots)):			
			self.Coefficients = self.PolyMult(self.Coefficients,[-self.Roots[i],1])
			print self.Coefficients
		return self.Coefficients
	
	def Generate_Random_Coefficients(self,order):
		A = []
		for i in range(0,order+1):
			A.append(int(random()*21)-10)
		return A

	#Evaluate a polynomial in the form of a list:
	def Evaluate(self,A, x):
		Value = 0
		for i in range(0, len(A)):
			Value += A[i]*(x**i)
			
		return Value

	def Evaluate_Self(self,x):
		Value = 0
		for i in range(0,len(self.Coefficients)):
			Value+=self.Coefficients[i]*(x**i)
		return Value
	def Newtons_Method(self, A):
		Tolerance = 100
		Roots = []
		xold = -1000000.123456
		xnew = 0.0
		difference = 10000000
		Count = 0
		while difference > 0.000001 and Count < 100:
			xold = xnew
			xnew = xnew - (float(self.Evaluate(A.Coefficients, xnew)))/(float(self.Evaluate(A.Derivative,xnew))+0.000000001)
			print xnew, self.Evaluate(A.Derivative,xnew), self.Evaluate(A.Coefficients,xnew)
			difference = abs(xnew-xold)
			Count +=1
		if Count < 100:
			Roots.append(xnew)
		if len(Roots) == 1:
			for i in range(-1000,1000):
				Count = 0
				xnew = float(i)
				xold = -1000000.012345
				difference = 1000000
				while difference >0.0000001 and Count < 100:
					xold = xnew
					xnew = xnew -(float(self.Evaluate(A.Coefficients,xnew)))/float(self.Evaluate(A.Derivative,xnew)+0.000000001)
					difference = abs(xnew-xold)
					Count +=1
				if Count < 100:
					New = 1
					for i in Roots:
						if abs(xnew-i)<=0.000001:
							New =0
					if New == 1:
						Roots.append(xnew)
		print "The roots are: ", Roots
		return Roots
