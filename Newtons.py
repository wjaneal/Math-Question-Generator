from math import *
def f(x):
	return 3*x*x + 2*x -5
def df(x):
	return 6*x+2
def next_guess(a):
	return -f(a)/df(a)+a
a = 400000001.0
tolerance = 10**(-5)
count = 0
difference = 1.0
while abs(difference)>tolerance and count < 10000:
	a_new = next_guess(a)#Find new a
	print a_new
 	difference = a_new - a #Find the difference
	a = a_new #Reset the old a - give it the value of the new a
	count += 1
	#Add one to the count
#Print result - a
print(a)










