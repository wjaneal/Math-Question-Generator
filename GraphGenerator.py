#Graph Generator for Mathemtatics Question Generator Program

#Required Modules
from pylab import *
from optparse import OptionParser
from numpy import *
from random import *
from Polynomials import *
import os

figures = []

def Abs_Extrema(F, Range):
	F_X_Min = F.Evaluate_Self(Range[0])
	F_X_Max = F.Evaluate_Self(Range[1])
	Roots = F.Newtons_Method(F)
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
	
	


# Make a square figure and axes
for i in range (0,10): 
	clf()
	a = int(random()*21)-10.0
	b = int(random()*21)-10.0
	c = int(random()*21)-10.0
	if a == 0:
		a=1
	figures.append(figure(1, figsize=(6,6)))
	X_LOW = -b/(2*a)-5
	X_HIGH = -b/(2*a)+5
	print X_LOW, X_HIGH
	x = linspace(X_LOW,X_HIGH)
	y = a*x*x+b*x+c
	Poly1 = Polynomial(2, [a,b,c])
	Extrema = Abs_Extrema(Poly1, [X_LOW, X_HIGH])
	Y_LOW = Extrema[0]
	Y_HIGH = Extrema[1]
	print Y_LOW, Y_HIGH, 'Extrema'
	plot(x,y)
	xlim(X_LOW, X_HIGH)
	#ylim(Y_LOW, Y_HIGH)
	grid()
	legend()
	savefig('Images/foo'+str(i)+'.png')

