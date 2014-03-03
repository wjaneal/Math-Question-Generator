#########################################################################################
# Import Required Modules
#########################################################################################

#Modules for GUI
import tkMessageBox
import Tkinter

#Modules containing background information
import special_problem_code #Underlying mathematics problem functionality

#Module to Generate Worksheets
#from worksheet_generator import *

import inspect #For compiling a list of problems from the functions in base_classes

#########################################################################################
#Get a list of the Problem Types to AutoMatically Generate Menus
#########################################################################################

#The following should somehow be fixed to be automated and incorporated into objects...
class TopicObject:
        def __init__(self):
                
                self.SPC = special_problem_code.SpecialProblemCode()
                self.ProblemNames = inspect.getmembers(self.SPC, predicate=inspect.ismethod)
                self.Data = special_problem_code.ApplicationData()
                self.Data.ProblemNames = inspect.getmembers(self.SPC, predicate = inspect.ismethod)
                self.TopicGenerator = []
                for i in self.Data.ProblemNames:
                        if i <> "__init__" and i[0][:2] <> "__":
                                self.TopicGenerator.append([i[0][:2], i[0][3:].replace("_"," ")])
                print self.TopicGenerator
                self.TopicCategoriesLookup = {}
                self.TopicCategories = [["AR","Arithmetic"],["FR","Fractions"],["QU","Quadratic Functions"],["CA","Calculus"],["VE", "Vectors"]]
        
                for item in self.TopicCategories:
                        self.TopicCategoriesLookup[item[0]] = item[1]

                self.TopicLookup = {}
                self.ReverseTopicLookup = {}
                for i in range(0,len(self.TopicGenerator)):
                        self.TopicLookup[self.TopicGenerator[i][0]] = self.TopicCategoriesLookup[self.TopicGenerator[i][0]]
                        self.ReverseTopicLookup[self.TopicCategoriesLookup[self.TopicGenerator[i][0]]] = self.TopicGenerator[i][0]
                self.TopicKeys = self.TopicLookup.keys()
                self.TopicValues = self.TopicLookup.values()
TopicObject1 = TopicObject()
##########################################################################################
# Main Program
##########################################################################################
class simpleapp_tk(Tkinter.Tk):
    from worksheet_generator import *

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
        self.Data = special_problem_code.ApplicationData()
        B = []
        self.tc = Tkinter.IntVar()
        #////////////////////////////////////////////////////////////////////
        #Generate Menus from Functions in Special Problem Code Class:
        #////////////////////////////////////////////////////////////////////
        SPC = special_problem_code.SpecialProblemCode()
        self.ProblemNames = inspect.getmembers(SPC, predicate=inspect.ismethod)
        self.Data.ProblemNames = inspect.getmembers(SPC, predicate = inspect.ismethod)
        print "Problem Names: ", self.Data.ProblemNames
        self.SortedProblems = []
        for i in range(0, len(self.Data.ProblemNames)):
            if self.Data.ProblemNames[i][0] != "__init__":
                self.SortedProblems.append(self.Data.ProblemNames[i][0])
        self.SortedProblems.sort()
        print self.SortedProblems
        self.Data.Topics = []
        self.Data.TopicPrefixes = []
        self.Data.subTopics = []
        self.Data.TopicIndex = []
        #Parse Names of Problems; sort into 2D list by two letter prefix
        for i in range (0, len(self.ProblemNames)):
            if self.ProblemNames[i][0] != '__init__':
                if TopicObject1.TopicLookup[self.ProblemNames[i][0][:2]]  not in self.Data.Topics:           
                    self.Data.Topics.append(TopicObject1.TopicLookup[self.ProblemNames[i][0][:2]])
                    self.Data.TopicPrefixes.append(self.ProblemNames[i][0][:2])
                    self.Data.TopicIndex.append(self.ProblemNames[i][0][:2])
                self.Data.subTopics.append([self.ProblemNames[i][0][:2],self.ProblemNames[i][0][3:]])
                    
                #self.CurrentModule = self.ProblemNames[i][0][:2]
        print self.Data.Topics, 'List of Topics'
        for i in range(0,len(self.Data.Topics)):
            B.append(Tkinter.Radiobutton(self, text = self.Data.Topics[i], variable = self.tc, value=i, justify = 'right', background = 'white', borderwidth=0, highlightthickness=0, font = "Arial 18"))
        #print B
        for i in range(0, len(B)):
            B[i].grid(column = 0, row = i+1, sticky = 'W')
        topicButton = Tkinter.Button(self,text="Select",background = "lightgreen", font = "Arial 20 bold", command = self.openFrame)
        topicButton.grid(column=0,row=len(self.Data.Topics)+2, sticky = 'W')
        exitButton = Tkinter.Button(self,text = "Exit", background = "red", font = "Arial 20 bold", command = self.destroy)
        exitButton.grid(column=1, row = len(self.Data.Topics)+2, sticky = 'W')
########################################################################################
    def hide(self):
        """"""
        self.withdraw()
########################################################################################
    #OpenFrame - This executes when a topic is selected.
    def openFrame(self):
        self.hide()
        self.Data.topicChoice = self.tc.get()
        self.Data.TopicCode = self.Data.TopicIndex[self.Data.topicChoice]
        print self.Data.TopicCode , "......................"
        print self.Data.topicChoice
        print self.Data.subTopics
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
        D = [] # Difficulty Buttons
        self.Data.subtopicChoice = 0
        self.stc = Tkinter.IntVar() 
        self.dl = Tkinter.IntVar() 
        #####################################################################################
        # subTopic Names
        #####################################################################################
        '''
        self.Data.SubTopics = []
        for i in range(0,len(self.SortedProblems)):
            print self.SortedProblems[i][:2], self.Data.TopicCode
            if self.SortedProblems[i][:2].upper() == self.Data.TopicCode.upper():
                self.Data.SubTopics.append(self.SortedProblems[i][3:].replace("_", " "))
        print self.Data.SubTopics
        '''
        for i in range(0,len(self.Data.subTopics)):
            if self.Data.subTopics[i][0] == self.Data.TopicCode:    
                    B.append(Tkinter.Checkbutton(otherFrame, text = self.Data.subTopics[i][1], variable = self.stc, onvalue=i, offvalue = -1, justify = 'right', background = 'white', borderwidth=0, highlightthickness=0, font =  "Arial 18"))
        D = Tkinter.OptionMenu(otherFrame, self.dl, 0, 1, 2, 3, 4, 5)
            #print B
        for i in range(0, len(B)):
                B[i].grid(column = 0, row = i+1, sticky = 'W')
        D.grid(column = 0, row = len(B)+1, sticky = 'W')
        print "Testing 123;ssd", special_problem_code.Topic(self.Data.subTopics[self.Data.subtopicChoice]).TopicName[1]
        #Place Difficulty Level Pulldowns here.
        #Set Difficulty to 0 for Now
        self.Data.DifficultyLevel = self.dl
        #Check self.Data.SubTopics[self.Data.topicChoice]
        choiceButton = Tkinter.Button(otherFrame,text="Select",background = "lightgreen", font = "Arial 20 bold", command = self.makeChoice)
        print self.Data.topicChoice, self.Data.subTopics
        choiceButton.grid(column=0,row=len(self.Data.subTopics[self.Data.topicChoice])+5, sticky = 'W')
        closeButton = Tkinter.Button(otherFrame, text="Close", command=handler, background = "orange", font = "Arial 20 bold")
        closeButton.grid(row = len(self.Data.subTopics[self.Data.topicChoice])+6, column=0,sticky = "W")


#########################################################################################
# Executes when a subTopic choice is made
#########################################################################################
    def makeChoice(self):
        #Make a New Topic Here
        self.Data.subtopicChoice=self.stc.get()
        print self.Data.subtopicChoice, "....#####.....##### Testing"
        self.T1 = special_problem_code.Topic(self.Data.subTopics[self.Data.subtopicChoice])
        #Set the Difficulty Level
        #self.T1.DifficultyLevel = self.Data.DifficultyLevel
#       self.T1.DifficultyLevel = 3
        self.T1.DifficultyLevel = self.dl.get()
        #Add questions here according to the number specified for the problem type.
        #Problem Here - define Special Problem Code at the Level of Topic Instead.\
        #This will allow for more smooth handling of data.
        #Retrieve from either a textbox or an object within the hierarchy
        self.T1.NumQuestions=20
        #print self.Data.topicChoice, self.Data.subtopicChoice
        for i in range(0, self.T1.NumQuestions):
            #*************************************************************************************************************************************************#
            self.T1.AddProblems(self.Data.subTopics[self.Data.subtopicChoice], self.T1.DifficultyLevel, self.Data.ProblemNames[self.Data.subtopicChoice][0])
            #*************************************************************************************************************************************************#
        print "Made a choice", self.Data.subtopicChoice, self.Data.topicChoice
        print TopicObject1, "...................................Hello"
        print self.Data.subTopics
        self.generateWorksheet(self.T1.Problems, self.Data.subTopics, TopicObject1, self.Data.subtopicChoice, self.Data.topicChoice, self.dl.get()) 
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







