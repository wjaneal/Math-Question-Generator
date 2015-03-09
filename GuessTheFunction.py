#Function Guessing Program
#Generates a Random Graph.
#Students Must Guess the Associated Function
#Graphs of Student Functions are Compared to the Original Graph

#Required Modules
from pylab import *
from optparse import OptionParser
from numpy import *
from random import *
from Polynomials import *
import os

figures = []
ax = []
GraphRange = 10.0
GraphPadding = 0.05
GraphTitle = 'Plot of Quadratic Function'

def Abs_Extrema(F, Range):
	F_X_Min = F.Evaluate_Self(Range[0])
	F_X_Max = F.Evaluate_Self(Range[1])
	print F.Coefficients, Range[0], F_X_Min, Range[1], F_X_Max, 'Evaluated at Endpoints'
	print F.Coefficients, F.Derivative, 'Diffd'
	Roots = F.Newtons_Method(Polynomial(len(F.Derivative)-1, F.Derivative))
	print Roots, 'Root.....'
	Root_Values = []
	for R in Roots:
		Root_Values.append([R, F.Evaluate_Self(R)])
	Root_Values.append([Range[0], F_X_Min])
	Root_Values.append([Range[1], F_X_Max])
	Abs_Minimum = Root_Values[0][1] 
	Abs_Maximum = Root_Values[0][1]
	for Array in Root_Values:
		if Array[1] < Abs_Minimum:
			Abs_Minimum = Array[1]
		if Array[1] > Abs_Maximum:
			Abs_Maximum = Array[1]
	return[Abs_Minimum, Abs_Maximum]	
	
def Plot_Function(x,y, Limits, FunctionAttributes):
	X_LOW = Limits[0]
	X_HIGH = Limits[1]
	Y_LOW = Limits[2]
	Y_HIGH = Limits[3]
	clf()
	fig = figure(1, figsize=(6,6))
	ax = fig.add_subplot(111)
	ax.set_ylabel(FunctionAttributes['Y_Axis_Name'])
	ax.set_xlabel(FunctionAttributes['X_Axis_Name'])
	ax.set_title(FunctionAttributes['Graph_Title'])
	plot(x,y)
	xlim(X_LOW, X_HIGH)
	ylim(Y_LOW, Y_HIGH)
	grid()
	legend()
	savefig('Images/'+ FunctionAttributes['File_Name'])

def Plot_Functions(Polynomial_Collection, GraphRange, GraphPadding, GraphName):
	clf()
	for Polynomial in Polynomial_Collection:
		[x, y, Limits, FunctionAttributes] = SetQuadraticParameters(Polynomial.Coefficients, GraphRange, GraphPadding, GraphName)
		try:
			MasterLimits
		except:
			MasterLimits = Limits
		if Limits[0]<MasterLimits[0]:
			MasterLimits[0] = Limits[0]
		if Limits[1]>MasterLimits[1]:
			MasterLimits[1] = Limits[1]
		if Limits[2]<MasterLimits[2]:
			MasterLimits[2] = Limits[2]
		if Limits[3]>MasterLimits[3]:
			MasterLimits[3] = Limits[3]
		plot(x,y)
	xlim(MasterLimits[0], MasterLimits[1])
	ylim(MasterLimits[2], MasterLimits[3])
	grid()
	legend()
	savefig('Images/'+FunctionAttributes['File_Name'])
	

#Generate a Random Function:
def GenerateRandomPolynomial(Order, Low, High):
	Poly = []
	for i in range(0, Order+1):	
		Poly.append(int(random()*(High-Low))+Low)
	print Poly
	if Poly[Order] == 0:
		Poly[Order] = 1
	return Poly

def SetQuadraticParameters(Poly, GraphRange, GraphPadding, GraphName):
	a = Poly[2]
	b = Poly[1]
	c = Poly[0]
	X_LOW = -b/(2*a)-GraphRange/2.0-GraphPadding*(GraphRange)
	X_HIGH = -b/(2*a)+GraphRange/2.0+GraphPadding*(GraphRange)
	x = linspace(X_LOW,X_HIGH)
	y = x*x+b*x+c
	#y = a*x*x+b*x+c
	Poly1 = Polynomial(2, [c, b, a])
	Extrema = Abs_Extrema(Poly1, [X_LOW, X_HIGH])
	Y_LOW = Extrema[0]-GraphPadding*(Extrema[1]-Extrema[0])
	Y_HIGH = Extrema[1]+GraphPadding*(Extrema[1]-Extrema[0])
	Limits = [X_LOW, X_HIGH, Y_LOW, Y_HIGH]
	FunctionAttributes = {'Graph_Title': 'Plot of Quadratic Function', 'X_Axis_Name': 'X-Axis', 'Y_Axis_Name': 'Y-Axis', 'File_Name':GraphName}
	return [x,y, Limits, FunctionAttributes]

#Create a Plot of the Function:

GraphName = "OriginalGraph"
Poly1 = GenerateRandomPolynomial(2, -10, 10)
[x, y, Limits, FunctionAttributes] = SetQuadraticParameters(Poly1, GraphRange, GraphPadding, GraphName)
Plot_Function(x, y, Limits, FunctionAttributes)

NumStudents = input('Please enter the number of students')
PolynomialCollection = [Polynomial(2,Poly1)]
for i in range(0, NumStudents):
	print "Student "+str(i)+ ", please enter your coefficients."
	a = input('a: ')
	b = input('b: ')
	c = input('c: ')
	PolynomialCollection.append(Polynomial(2, [c,b,a]))
GraphName = "Comparison"
Plot_Functions(PolynomialCollection, GraphRange, GraphPadding, GraphName)


	
'''
# Make a square figure and axes
for i in range (0,10): 
	clf()
	a = int(random()*21)-10.0
	b = int(random()*21)-10.0
	c = int(random()*21)-10.0
	if a == 0:
		a=1
	fig = figure(1, figsize=(6,6))
	figures.append(fig)
	ax1 = fig.add_subplot(111)
	ax1.set_ylabel('Y Axis')
	ax1.set_xlabel('X Axis')
	ax1.set_title(GraphTitle)

	ax.append(ax1)
	
	X_LOW = -b/(2*a)-GraphRange/2.0-GraphPadding*(GraphRange)
	X_HIGH = -b/(2*a)+GraphRange/2.0+GraphPadding*(GraphRange)
	print X_LOW, X_HIGHy
	x = linspace(X_LOW,X_HIGH)
	y = a*x*x+b*x+c
	Poly1 = Polynomial(2, [c, b, a])
	Extrema = Abs_Extrema(Poly1, [X_LOW, X_HIGH])
	Y_LOW = Extrema[0]-GraphPadding*(Extrema[1]-Extrema[0])
	Y_HIGH = Extrema[1]+GraphPadding*(Extrema[1]-Extrema[0])
	print Y_LOW, Y_HIGH, 'Extrema'
	plot(x,y)
	
	xlim(X_LOW, X_HIGH)
	ylim(Y_LOW, Y_HIGH)
	grid()
	legend()
	savefig('Images/foo'+str(i)+'.png')
'''
