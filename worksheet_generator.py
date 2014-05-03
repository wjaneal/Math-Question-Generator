###############################################################
#Python Mathematical Question Generator - Worksheet Generator
###############################################################

#Worksheet generation sub-functions:
from worksheet_headers import *
#Functions for generating mathematical worksheets
import os
import subprocess
from time import *
from datetime import *


##########################################################################################
#Function to read and return the contents of a file.
##########################################################################################
def FileGetContents(self, filename):
    with open(filename) as a_file:
        return a_file.read()

def MakeLatexTitle(self,Title):
    return "\begin{center}"+Title+"\end{center}"

def MakeLatexParagraph(self,Paragraph):
    return "\paragraph{}"+Paragraph

#########################################################################################
def generateWorksheet(self, QuestionSet, subTopics, TopicObject1, subTopicChoice, topicChoice,difficulty_level):

#########################################################################################
    self.Data.subTopic = subTopics[self.stc.get()][1]
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
    #print self.Questions
    #print self.Answers
    #Generate the Latex File
    Equations = "\\begin{multicols}{"+str(self.NumColumns)+"}"
    for i in range(0,self.NumQuestions-1):
        Equations += "("+str(i+1)+") $ "+self.Questions[i] + "$\hspace{3 mm}\line(1,0){"+str(self.LineLength)+"}\\\\\\\\"
    Equations += "("+str(self.NumQuestions)+") $"+self.Questions[self.NumQuestions-1]+"$\line(1,0){"+str(self.LineLength)+"}"
    Equations += "\\end{multicols}"
    Header = self.FileGetContents(header)
    #print QuestionSet[0].QuestionForms[0]
    #print QuestionSet[0].QuestionForms[0].__dict__
    #print QuestionSet[0].__dict__
    #Header += self.MakeLatexTitle(QuestionSet[0].QuestionForms[0].Title)
    #Header += self.MakeLatexParagraph(self.QuestionSet[0].QuestionForms[0].Instructions)
    Footer = self.FileGetContents(footer)

    #Equations = "\\begin{tabluar}\\\\"
    #Equations = ""
    #print CurrentModule
    #print self.Data.subtopicChoice
    self.CurrentModule = TopicObject1.TopicKeys[self.Data.topicChoice]
    TopicObject1.TopicPrefix = TopicObject1.TopicCategories[self.Data.topicChoice][0]
    #TopicPrefix = str(self.Data.ProblemNames[self.Data.subtopicChoice][0][:2]).replace(" ", "_")
    #TopicName = str(TopicLookup[self.Data.ProblemNames[self.Data.subtopicChoice][0][:2]])
    #TopicName = TopicValues[self.Data.topicChoice]
    #print TopicPrefix,TopicName
    FileName = TopicObject1.TopicPrefix+"_Q_"+self.Data.subTopic+"_"+str(difficulty_level)+".tex"
    if not os.path.isdir(TopicObject1.TopicPrefix):
        os.makedirs(TopicObject1.TopicPrefix)
    f = open( "./"+TopicObject1.TopicPrefix+"/"+FileName, 'w' )
    f.write( Header+Equations+Footer )
    f.close()
    #print self.tc.get(), self.CurrentModule, TopicLookup[self.CurrentModule], "....Test..."
    os.system("pdflatex ./"+TopicObject1.TopicPrefix+"/"+FileName+" -interaction nonstopmode -output-directory "+TopicObject1.TopicLookup[self.CurrentModule].replace(" ","_"))

        
    Equations = "\\begin{multicols}{"+str(self.NumColumns)+"}"
    for i in range(0,self.NumQuestions-1):
        if type(self.Answers[i]) is list and len(self.Answers[i])==2:
        #print "Testing.............................1"
            Answer = str(self.Answers[i][0]) + "\hspace{3 mm} and \hspace{3 mm} "+str(self.Answers[i][1])
        #print "Answer 1. ", Answer
        else:
            Answer = str(self.Answers[i])
        #print "Answer 2", Answer
            Equations += "("+str(i+1)+") $"+ Answer + "$\\\\"
    if type(self.Answers[self.NumQuestions-1]) is list and len(self.Answers[self.NumQuestions-1])==2:
        Answer = str(self.Answers[self.NumQuestions-1][0])+ "\hspace{3 mm} and \hspace{3 mm} " + str(self.Answers[self.NumQuestions-1][1])
    else:
        Answer = str(self.Answers[self.NumQuestions-1])
        Equations += "(" + str(self.NumQuestions) +") $"+ Answer+"$\\\\"
    #print Answer
    Equations += "\end{multicols}"
    Header = self.FileGetContents(header)
    Footer = self.FileGetContents(footer)
    #form1 = QuestionForm(string1)
    FileName = TopicObject1.TopicPrefix+"_A_"+self.Data.subTopic+"_"+str(difficulty_level)+".tex"
    #FileName = (TopicLookup[self.CurrentModule]).replace(" ","_")+"_answers_"+str(self.Data.subtopicChoice)+".tex"
    f = open( "./"+TopicObject1.TopicPrefix+"/"+FileName, 'w' )
    f.write( Header+Equations+Footer )
    f.close()
    os.system("pdflatex ./"+(TopicObject1.TopicPrefix)+"/"+FileName+" -interaction nonstopmode -output-directory "+TopicObject1.TopicLookup[self.CurrentModule])
    os.system("rm *.aux")
    os.system("rm *.log")
    os.system("rm *.out")
    os.system("rm *.tex")
    for topicList in TopicObject1.TopicCategories:
	try:
	        os.system("mv "+topicList[0]+"*.pdf "+topicList[0])
	except:
		pass



