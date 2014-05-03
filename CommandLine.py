#Testing of Command Line

import os
import subprocess as sub
#p = sub.Popen('pdflatex Answers.tex', stdout=sub.PIPE,stderr=sub.PIPE)
#output, errors = p.communicate()
#print output
os.system('pdflatex Answers.tex -interaction nonstopmode')
#for i in p.readlines():
#	print "Results: ", i

