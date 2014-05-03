'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

###############################################################################
# Arithmetic Functions - Module for Math Question Generator
###############################################################################
from math import *
#def lcm(a, b):
#        return (a * b) // gcd(a, b)
#        return reduce(lcm, numbers, 1)

def isprime(x):
	is_prime = True
	for i in range(2,x):
		if x*1.0/i == int(x*1.0/i):
			print x, i
			is_prime = False
	return is_prime
	


def primes(n):
	numbers = []
	for i in range(0, n+1):
		numbers.append(i)
	i = 2
	while i < n:
		x = i*2
		while x <= len(numbers)-1:
			numbers[x] = 0
			x+=i
		done = 0
		while done == 0 and i <= len(numbers)-2:
			i+=1
			if numbers[i] <> 0:
				done = 1
	primenumbers = []
	for i in range(2,len(numbers)-1):
		if numbers[i] <> 0:
			primenumbers.append(i)
	return primenumbers

def get_next_prime(x):
	primes_list = primes(1000)
	i = 0
	if x not in primes_list:
		print "Error!!!!"
	while x <> primes_list[i]:
		i+=1
	return primes_list[i+1]

			
			


def Prime_Factorization(a):
	q = a*1.0
	x = 2.0
	prime_factorization = []
	print "a:    ", a
	while q > 1:
		done_number = 0
		while done_number == 0:
			if q/x == int(q/x):
				q/=x
				prime_factorization.append(x)
				print q, x#, prime_factorization[x]
			else:
				done_number = 1
				x = get_next_prime(x)
	return prime_factorization		

print primes(1000)
print Prime_Factorization(992)
