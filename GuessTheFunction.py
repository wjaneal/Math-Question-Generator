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
	clf()
	fig = figure(1, figsize=(6,6))
	ax = fig.add_subplot(111)
	ax1.set_ylabel(FunctionAttributes['Y_Axis_Name'])
	ax1.set_xlabel(FunctionAttributes['X_Axis_Name'])
	ax1.set_title(FunctionAttributes['Name'])
	
#Generate a Random Function:
a = int(random()*21)-10.0
b = int(random()*21)-10.0
c = int(random()*21)-10.0
if a== 0:
	a== 1

X_LOW = -b/(2*a)-GraphRange/2.0-GraphPadding*(GraphRange)
X_HIGH = -b/(2*a)+GraphRange/2.0+GraphPadding*(GraphRange)
x = linspace(X_LOW,X_HIGH)
y = a*x*x+b*x+c
Poly1 = Polynomial(2, [c, b, a])
Extrema = Abs_Extrema(Poly1, [X_LOW, X_HIGH])
Y_LOW = Extrema[0]-GraphPadding*(Extrema[1]-Extrema[0])
Y_HIGH = Extrema[1]+GraphPadding*(Extrema[1]-Extrema[0])
Limits = [X_LOW, X_HIGH, Y_LOW, Y_HIGH]
#Create a Plot of the Function:
FunctionAttributes = {'Graph_Title'=>'Plot of Quadratic Function', 'X_Axis_Name'=>'X-Axis', 'Y_Axis_Name'=>'Y-Axis'}
Plot_Function(x, y, Limits, FunctionAttributes)
	
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
