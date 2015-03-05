from numpy import *
from pylab import *
class circle:
	# Constructor:
	def __init__(self, r, cx, cy, n = 100):
		self.R = r
		self.Cx = cx
		self.Cy = cy
		self.n = n
		# And now the points for plotting:
		self.ptsx = []
		self.ptsy = []
		da = 2*pi/self.n
		for i in range(n):
			self.ptsx.append(self.Cx + self.R * cos(i * da))
			self.ptsy.append(self.Cy + self.R * sin(i * da))
			self.ptsx.append(self.Cx + self.R)
			self.ptsy.append(self.Cy + 0)
			# Method to return circle area:
	def area(self):
		return pi * self.R**2
	# Method to return perimeter:
	def perimeter(self):
		return 2 * pi * self.R
	def draw(self, label):
		axis('equal')
		plot(self.ptsx, self.ptsy, label = label)
		legend()
# Create an instance:
C1 = circle(1, 0, 0)
print "Area and perimeter of circle 1:", \
C1.area(), C1.perimeter()
C2 = circle(0.5, 1, 0)
print "Area and perimeter of circle 2:", \
C2.area(), C2.perimeter()
C3 = circle(0.25, 1.5, 0)
print "Area and perimeter of circle 3:", \
C3.area(), C3.perimeter()

clf()
C1.draw("First circle")
C2.draw("Second circle")
C3.draw("Third circle")
show()


