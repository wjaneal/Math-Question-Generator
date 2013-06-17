import tkMessageBox
import Tkinter

import base_classes
from worksheet_headers import *

import os
import subprocess
from time import *
from datetime import *


import inspect

#Get a list of the Problem Types to AutoMatically Generate Menus
#print Problems

#The following should somehow be fixed to be automated and incorporated into objects...
TopicLookup = {"AR":"Arithmetic","QU":"Quadratic Functions","CA":"Calculus","FR":"Fractions","VE": "Vectors"}
CurrentModule = 0
#CurrentModule = "Fract"
#CurrentModule = "Vecto"
#CurrentModule = "Polyn"
#CurrentModule = "Calcu"


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
	self.geometry = ("800x600")
	self.TitleLabel = Tkinter.Label(text = "Topic", background = "white", font = "Arial 20 bold")
	self.TitleLabel.grid(column=0,row=0,sticky = 'W')
	self.Radiobuttons = []
	#for i in range(0,len(Topics)):
	self.Data = base_classes.ApplicationData()
	B = []
	self.tc = Tkinter.IntVar()
	#////////////////////////////////////////////////////////////////////
	#Generate Menus from Functions in Special Problem Code Class:
	#////////////////////////////////////////////////////////////////////
	SPC = base_classes.SpecialProblemCode()
	self.ProblemNames = inspect.getmembers(SPC, predicate=inspect.ismethod)
	self.Data.Topics = []
	#Parse Names of Problems; sort into 2D list by two letter prefix
	for i in range (0, len(self.ProblemNames)):
		if self.ProblemNames[i][0] != '__init__':
			if TopicLookup[self.ProblemNames[i][0][:2]] not in self.Data.Topics:			
				self.Data.Topics.append(TopicLookup[self.ProblemNames[i][0][:2]])
	print self.Data.Topics
	for i in range(0,len(self.Data.Topics)):
		B.append(Tkinter.Radiobutton(self, text = self.Data.Topics[i], variable = self.tc, value=i, justify = 'right', background = 'white', borderwidth=0, highlightthickness=0, font = "Arial 18"))
	print B
	for i in range(0, len(B)):
		B[i].grid(column = 0, row = i+1, sticky = 'W')
	topicButton = Tkinter.Button(self,text="Select",background = "lightgreen", font = "Arial 20 bold", command = self.openFrame)
        topicButton.grid(column=0,row=len(self.Data.Topics)+2, sticky = 'W')
	exitButton = Tkinter.Button(self,text = "Exit", background = "red", font = "Arial 20 bold", command = self.destroy)
	exitButton.grid(column=1, row = len(self.Data.Topics)+2, sticky = 'W')
    def hide(self):
        """"""
        self.withdraw()

    #----------------------------------------------------------------------
    def openFrame(self):
        self.hide()
	self.Data.topicChoice = self.tc.get()
	self.Data.topicChoice
        otherFrame = Tkinter.Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("Select Sub-topic")
	otherFrame.configure(background = "white")
	otherFrame.grid()
        handler = lambda: self.onCloseOtherFrame(otherFrame)
	TitleLabel1 = Tkinter.Label(otherFrame, text = "Select Sub-Topic", background = "white", font = "Arial 20 bold")	
	TitleLabel1.grid(row = 0, column=0, sticky = "W")
	#Move this to base classes and beyond:
   	B = []
	self.Data.subtopicChoice = 0
	self.stc = Tkinter.IntVar() 
	#####################################################################################
	# subTopic Names
	#####################################################################################
	self.Data.SubTopics = []
	for i in range(0,len(self.ProblemNames)):
		if self.ProblemNames[i][0] != "__init__" and TopicLookup[self.ProblemNames[i][0][:2]] == self.Data.Topics[self.Data.topicChoice]:
			self.Data.SubTopics.append(self.ProblemNames[i][0][2:])
	print self.Data.SubTopics
	for i in range(0,len(self.Data.SubTopics)):
			#self.stc.append(Tkinter.IntVar())
        		B.append(Tkinter.Checkbutton(otherFrame, text = self.Data.SubTopics[i], variable = self.stc, onvalue=i, offvalue = -1, justify = 'right', background = 'white', borderwidth=0, highlightthickness=0, font =  "Arial 18"))

        print B
        for i in range(0, len(B)):
                B[i].grid(column = 0, row = i+1, sticky = 'W')

	#Place Difficulty Level Pulldowns here.
	#Set Difficulty to 0 for Now
	self.Data.DifficultyLevel = 0


	choiceButton = Tkinter.Button(otherFrame,text="Select",background = "lightgreen", font = "Arial 20 bold", command = self.makeChoice)
        choiceButton.grid(column=0,row=len(self.Data.SubTopics[self.Data.topicChoice])+4, sticky = 'W')

        closeButton = Tkinter.Button(otherFrame, text="Close", command=handler, background = "orange", font = "Arial 20 bold")
	closeButton.grid(row = len(self.Data.SubTopics[self.Data.topicChoice])+5, column=0,sticky = "W")

    #Function to read and return the contents of a file.
    def FileGetContents(self, filename):
	with open(filename) as a_file:
	    return a_file.read()


    def generateWorksheet(self, QuestionSet):
	self.Questions = []
	self.Answers = []
	self.NumQuestions = len(QuestionSet)
	self.NumColumns = 2
	self.LineLength = 125
	#Get the CurrentDate
        CurrentDate = str(date.today())
        #Generate a timestamp
        TimeStamp = localtime()
	#...Include a mechanism to optionally import file details from the GUI...
        '''Header = Header_File("Worksheet_header.txt","London International Academy - Mathematics Worksheet", "Mathematics and Science Department", CurrentDate)
        Header.Write_Header()'''
        Header = Header_File("Worksheet_header.txt", "White Oaks Institute - Mathematics Worksheet", "Arithmetic", CurrentDate,TimeStamp)
        Header.Write_Header()
	header = "./Worksheet_header.txt"
	footer = "./footer.txt"
#...Rewrite to access new object structure...
        for i in range(0,self.NumQuestions):
	    self.Questions.append(QuestionSet[i].QuestionForms[0].Equation_String)
	    self.Answers.append(QuestionSet[i].QuestionForms[0].Answers)
	print self.Questions
	print self.Answers
	#Generate the Latex File
	Equations = "\\begin{multicols}{"+str(self.NumColumns)+"}"
	for i in range(0,self.NumQuestions-1):
		Equations += "("+str(i+1)+") $ "+self.Questions[i] + "$\hspace{3 mm}\line(1,0){"+str(self.LineLength)+"}\\\\\\\\"
	Equations += "("+str(self.NumQuestions)+") $"+self.Questions[self.NumQuestions-1]+"$\line(1,0){"+str(self.LineLength)+"}"
	Equations += "\end{multicols}"
	Header = self.FileGetContents(header)
	Footer = self.FileGetContents(footer)

	#Equations = "\\begin{tabluar}\\\\"
	#Equations = ""
	print CurrentModule
	print self.Data.subtopicChoice
	FileName = Modules_List[CurrentModule]+"_quest_"+str(self.Data.SpecialCode[self.Data.topicChoice][self.Data.subtopicChoice])+".tex"
	if not os.path.isdir(Modules_List[CurrentModule]):
		os.makedirs(Modules_List[CurrentModule])
	f = open( "./"+Modules_List[CurrentModule]+"/"+FileName, 'w' )
	f.write( Header+Equations+Footer )
	f.close()
	os.system("pdflatex ./"+Modules_List[CurrentModule]+"/"+FileName+" -interaction nonstopmode -output-directory ./"+Modules_List[CurrentModule])

		
	Equations = "\\begin{multicols}{"+str(self.NumColumns)+"}"
        for i in range(0,self.NumQuestions-1):
		if len(self.Answers[i])==2:
			Answer = str(self.Answers[i][0]) + "\hspace{3 mm} and \hspace{3 mm} "+str(self.Answers[i][1])
		else:
			Answer = str(self.Answers[i])
                Equations += "("+str(i+1)+") $"+ Answer + "$\\\\"
	if len(self.Answers[self.NumQuestions-1])==2:
		Answer = str(self.Answers[self.NumQuestions-1])
	else:
		Answer = str(self.Answers[self.NumQuestions-1])
        Equations += "("+str(self.NumQuestions)+") $"+str(Answer)
        Equations += "$\end{multicols}"
        Header = self.FileGetContents(header)
        Footer = self.FileGetContents(footer)
        #form1 = QuestionForm(string1)
        FileName = Modules_List[CurrentModule]+"_answers_"+str(self.Data.subtopicChoice)+".tex"
        f = open( "./"+Modules_List[CurrentModule]+"/"+FileName, 'w' )
        f.write( Header+Equations+Footer )
        f.close()
	os.system("pdflatex ./"+Modules_List[CurrentModule]+"/"+FileName+" -interaction nonstopmode -output-directory ./"+Modules_List[CurrentModule])


    def makeChoice(self):
        #Make a New Topic Here
	self.Data.subtopicChoice=self.stc.get()
	self.T1 = base_classes.Topic(self.Data.Topics[self.Data.topicChoice])
	#Set the Difficulty Level
	self.T1.DifficultyLevel = self.Data.DifficultyLevel
	#Add questions here according to the number specified for the problem type.
	#Problem Here - define Special Problem Code at the Level of Topic Instead.\
	#This will allow for more smooth handling of data.
	#Retrieve from either a textbox or an object within the hierarchy
	self.T1.NumQuestions=20
	print self.Data.topicChoice, self.Data.subtopicChoice
	for i in range(0, self.T1.NumQuestions):
		self.T1.AddProblems(self.Data.SubTopics[self.Data.topicChoice][self.Data.subtopicChoice], self.T1.DifficultyLevel, self.Data.SpecialCode[self.Data.topicChoice][self.Data.subtopicChoice])
	print "Made a choice", self.Data.subtopicChoice, self.Data.topicChoice
	#Generate QuestionTypes
	#Generate Questions	
        #print self.T1.Problems[0].QuestionForms[0].Format_String
        #print self.T1.Problems[0].QuestionForms[0].Answers
	#for i1 in range(0,len(self.T1.Problems)):
		#for i2 in range(0,len(self.T1.Problems[i1].QuestionForms)):
			#print self.T1.Problems[i1].QuestionForms[i2].Equation_String
			#print self.T1.Problems[i1].QuestionForms[i2].Answers
	self.generateWorksheet(self.T1.Problems)
	#Generate Header + Content + Footer and save as a .tex file
	#Convert the .tex file to a .pdf file
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    #----------------------------------------------------------------------
    def show(self):
        """"""
        #self.root.update()
        self.deiconify()



    def SubTopicWindow(self):
	#tkMessageBox.showinfo('Choose a Sub-Topic')
	self.top=Tkinter.Toplevel()
	self.top.config(background = 'white')
  	self.top.grid()


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Automatic Test Generator Program')
    app.configure(background = 'white')
    app.mainloop()
exit()
