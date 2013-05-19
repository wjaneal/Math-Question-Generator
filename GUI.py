import tkMessageBox
import Tkinter

import base_classes


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
	self.subtopicChoice = 0
	self.stc = []

        for i in range(0,len(self.Data.SubTopics[self.Data.topicChoice])):
		self.stc.append(Tkinter.IntVar())
                B.append(Tkinter.Checkbutton(otherFrame, text = self.Data.SubTopics[self.Data.topicChoice][i], variable = self.stc[i], onvalue=i, offvalue = -1, justify = 'right', background = 'white', borderwidth=0, highlightthickness=0, font =  "Arial 18"))

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
		
    def makeChoice(self):
        #Make a New Topic Here
	self.T1 = base_classes.Topic(self.Data.Topics[self.Data.topicChoice])
	#Set the Difficulty Level
	self.T1.DifficultyLevel = self.Data.DifficultyLevel
	#Add questions here according to the number specified for the problem type.
	self.T1.AddProblems(self.Data.SubTopics[self.Data.topicChoice][self.Data.subtopicChoice], self.T1.DifficultyLevel, self.Data.SpecialCode[self.Data.topicChoice][self.Data.subtopicChoice])
	print "Made a choice"
	#Generate QuestionTypes
	#Generate Questions	
        print self.T1.Problems[0].QuestionForms[0].Format_String
        print self.T1.Problems[0].QuestionForms[0].Answers
	for i1 in range(0,len(self.T1.Problems)):
		for i2 in range(0,len(self.T1.Problems[i1].QuestionForms)):
			print self.T1.Problems[i1].QuestionForms[i2].Equation_String

	#print self.T1.Problems[0].ProblemName

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
