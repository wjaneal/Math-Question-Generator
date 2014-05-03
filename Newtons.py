'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

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










