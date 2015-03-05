#Graph Generator for Mathemtatics Question Generator Program

#Required Modules
from pylab import *
from optparse import OptionParser
from numpy import *
from random import *
import os

figures = []

def Abs_Extrema(F, Range):
	DF = Differentiate(F):
	F_X_Min = Evaluate(F, Range[0])
	F_X_Max = Evaluate(F, Range[1])
	Roots = Zeros(F)
	Root_Values = []
	for Root in Roots:
		Root_Values.append([Root, Evaluate(F, Root)])
	
	
	


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
	Polynomial = [a,b,c]
	[Y_LOW, Y_HIGH] = Abs_Extrema(Polynomial)
	plot(x,y)
	xlim(X_LOW, X_HIGH)
	ylim(Y_LOW, Y_HIGH)
	axis('equal')
	grid()
	legend()
	savefig('foo'+str(i)+'.png')

