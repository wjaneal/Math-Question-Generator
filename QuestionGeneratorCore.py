'''

Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''

#import required modules
import os 
from time import *
from datetime import *
from random import *
from base_classes import *
from visual import *
from vectors import *
from worksheet_headers import *
from arithmetic import *
from Polynomials import *

#The following should somehow be fixed to be automated....
Modules_List = ["Arith"]
CurrentModule = 0
#CurrentModule = "Fract"
#CurrentModule = "Vecto"
#CurrentModule = "Polyn"
#CurrentModule = "Calcu"


  
#Function to read and return the contents of a file.
def FileGetContents(filename):
	with open(filename) as a_file:
		return a_file.read()

#Get the CurrentDate
CurrentDate = str(date.today())
#Generate a timestamp
TimeStamp = time.localtime()

#print TimeStamp.year, TimeStamp.month, TimeStamp.day, TimeStamp.hour, TimeStamp.minute


'''Header = Header_File("Worksheet_header.txt","London International Academy - Mathematics Worksheet", "Mathematics and Science Department", CurrentDate)
Header.Write_Header()'''
Header = Header_File("Worksheet_header.txt", "White Oaks Institute - Mathematics Worksheet", "Arithmetic", CurrentDate,TimeStamp)
Header.Write_Header()



#Dictionary to Manage Vector Question Functions:
#Get_QA_Function = {1: Vector_Magnitude, 2:Dot_Product, 3:Cross_Product}
#Dictionary to Manage Arithmetic Question Functions:

#*******Roll the Function Names into the Class Attributes - May 2, 2013*********
Get_QA_Function = {0:Arith_QA_Function}
Get_Function_Name = {0:"Arithmetic Pairs", 1:"Arithmetic Pairs Plus One", 2:"Addition to 12", 3:"Addition to 15", 4:"Addition to 20", 5:"Vertical Addition to 20"}

header = "./Worksheet_header.txt"
footer = "./footer.txt"

#Loop through each question type and generate a question and answer sheet.
#***********This part should be automated through Checkboxes in a GUI*********
for QuestionType in range(6,7):
	#Later:  Make the Num_Questions_Array depend on the current module being used.
	#Retrieve this from the Num_Questions_Array in the module
	NumQuestions = Num_Questions_Array[QuestionType]
	NumColumns = Num_Columns_Array[QuestionType]
	LineLength = Line_Length_Array[QuestionType]
	Questions = []
	Answers = []
	#Look up the Correct Function and Return the Question and Answer Latex Strings
	for i in range(0,NumQuestions):
		QA_Function = Get_QA_Function[CurrentModule][QuestionType]
		Function_Name = Get_Function_Name[CurrentModule][QuestionType]
		[Q,A] = QA_Function()
		Questions.append(Q)
		Answers.append(A)
	print Questions
	print Answers
	#Generate the Latex File
	Equations = "\\begin{multicols}{"+str(NumColumns)+"}"
	for i in range(0,NumQuestions-1):
		Equations += "("+str(i+1)+") "+Questions[i] + "\line(1,0){"+str(LineLength)+"}\\\\\\\\"
	Equations += "("+str(NumQuestions)+")"+Questions[NumQuestions-1]+"\line(1,0){"+str(LineLength)+"}"
	Equations += "\end{multicols}"
	Header = FileGetContents(header)
	Footer = FileGetContents(footer)

	#Equations = "\\begin{tabluar}\\\\"
	#Equations = ""
	FileName = Modules_List[CurrentModule]+"_quest_"+str(QuestionType)+".tex"
	if not os.path.isdir(Modules_List[CurrentModule]):
		os.makedirs(Modules_List[CurrentModule])
	f = open( "./"+Modules_List[CurrentModule]+"/"+FileName, 'w' )
	f.write( Header+Equations+Footer )
	f.close()

#Repeat loop for answer sheets:
#********This part should also be automated through checkboxes in a GUI*************
for QuestionType in range(1,6):
	Equations = "\\begin{multicols}{"+str(NumColumns)+"}"
	for i in range(0,NumQuestions-1):
		Equations += "("+str(i+1)+") "+ Answers[i] + "\\\\"
	Equations += "("+str(NumQuestions)+")"+Answers[NumQuestions-1] 
	Equations += "\end{multicols}"
	Header = FileGetContents(header)
	Footer = FileGetContents(footer)
	#form1 = QuestionForm(string1)
	FileName = Modules_List[CurrentModule]+"_answers_"+str(QuestionType)+".tex"
	f = open( "./"+Modules_List[CurrentModule]+"/"+FileName, 'w' )
	f.write( Header+Equations+Footer )
	f.close()


#Old code chunks....
'''#Generate Equations:
for q in range(1,11):
	F = Polynomial(3)
	F.GenerateIntRoots(Range1)
	F.GenerateCoefficients()
	F.Derivative = F.Differentiate(F.Coefficients)
	Questions.append(F)

print "....."
print Questions[0].Generate_Latex_String(Questions[0].Coefficients)

for q in range(0,len(Questions)):
	string1 = Questions[q].Generate_Latex_String(Questions[q].Coefficients)
	string1 += "\line(1,0){150}"
	string1 = MakeLatexEquation(string1)
	Equations += "("+str(q)+")  "+string1+"\\\\"
#Equations += "\\end{tabular}\end{multicols}"
Header = FileGetContents(header)
Footer = FileGetContents(footer)
#form1 = QuestionForm(string1)'''

'''
Equations = ""
for q in range(0,len(Questions)):
	string1 = "f(x) = "+Questions[q].Generate_Latex_String(Questions[q].Coefficients)+"\\\\"
	string1 = MakeLatexEquation(string1)
	Equations += "("+str(q)+")  "+string1+"\\\\"
	string1 = "f'(x) = " + Questions[q].Generate_Latex_String(Questions[q].Derivative)
	string1 = MakeLatexEquation(string1)
	Equations += string1 + "\\\\"
#Equations += "\\end{tabular}"'''
