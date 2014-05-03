'''
Copyright 2014, William Neal

The Math Question Generator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Math Question Generator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Math Question Generator.  If not, see <http://www.gnu.org/licenses/>.

'''
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


#MQG_Command.py - Command Line Interface for Math Question Generator
import special_problem_code #Underlying mathematics problem functionality

#Module to Generate Worksheets
#from worksheet_generator import *

import inspect #For compiling a list of problems from the functions in base_classes

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
def FileGetContents(filename):
    with open(filename) as a_file:
        return a_file.read()

def MakeLatexTitle(Title):
    return "\begin{center}"+Title+"\end{center}"

def MakeLatexParagraph(Paragraph):
    return "\paragraph{}"+Paragraph

#########################################################################################
def generateWorksheet(QuestionSet, subTopic, TopicObject1, subTopicChoice, topicChoice,difficulty_level):

#########################################################################################
    Data = subTopic
    Questions = []
    Answers = []
    NumQuestions = len(QuestionSet)
    NumColumns = 2
    LineLength = 125
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
    for i in range(0,NumQuestions):
        Questions.append(QuestionSet[i].QuestionForms[0].Equation_String)
        Answers.append(QuestionSet[i].QuestionForms[0].Answers)
    #print self.Questions
    #print self.Answers
    #Generate the Latex File
    Equations = "\\begin{multicols}{"+str(NumColumns)+"}"
    for i in range(0,NumQuestions-1):
        Equations += "("+str(i+1)+") $ "+Questions[i] + "$\hspace{3 mm}\line(1,0){"+str(LineLength)+"}\\\\\\\\"
    Equations += "("+str(NumQuestions)+") $"+Questions[NumQuestions-1]+"$\line(1,0){"+str(LineLength)+"}"
    Equations += "\\end{multicols}"
    Header = FileGetContents(header)
    #print QuestionSet[0].QuestionForms[0]
    #print QuestionSet[0].QuestionForms[0].__dict__
    #print QuestionSet[0].__dict__
    #Header += self.MakeLatexTitle(QuestionSet[0].QuestionForms[0].Title)
    #Header += self.MakeLatexParagraph(self.QuestionSet[0].QuestionForms[0].Instructions)
    Footer = FileGetContents(footer)

    #Equations = "\\begin{tabluar}\\\\"
 #Equations = ""
    #print CurrentModule
    #print self.Data.subtopicChoice
    CurrentModule = TopicObject1.TopicKeys[topicChoice]
    TopicObject1.TopicPrefix = TopicObject1.TopicCategories[topicChoice][0]
    #TopicPrefix = str(self.Data.ProblemNames[self.Data.subtopicChoice][0][:2]).replace(" ", "_")
    #TopicName = str(TopicLookup[self.Data.ProblemNames[self.Data.subtopicChoice][0][:2]])
    #TopicName = TopicValues[self.Data.topicChoice]
    #print TopicPrefix,TopicName
    FileName = TopicObject1.TopicPrefix+"_Q_"+str(subTopic)+"_"+str(difficulty_level)+".tex"
    if not os.path.isdir(TopicObject1.TopicPrefix):
        os.makedirs(TopicObject1.TopicPrefix)
    f = open( "./"+TopicObject1.TopicPrefix+"/"+FileName, 'w' )
    f.write( Header+Equations+Footer )
    f.close()
    #print self.tc.get(), self.CurrentModule, TopicLookup[self.CurrentModule], "....Test..."
    os.system("pdflatex ./"+TopicObject1.TopicPrefix+"/"+FileName+" -interaction nonstopmode -output-directory "+TopicObject1.TopicLookup[CurrentModule].replace(" ","_"))


    Equations = "\\begin{multicols}{"+str(NumColumns)+"}"
    for i in range(0,NumQuestions-1):
        if type(Answers[i]) is list and len(Answers[i])==2:
        #print "Testing.............................1"
            Answer = str(Answers[i][0]) + "\hspace{3 mm} and \hspace{3 mm} "+str(Answers[i][1])
        #print "Answer 1. ", Answer
        else:
            Answer = str(Answers[i])
        #print "Answer 2", Answer
            Equations += "("+str(i+1)+") $"+ Answer + "$\\\\"
    if type(Answers[NumQuestions-1]) is list and len(Answers[NumQuestions-1])==2:
        Answer = str(Answers[NumQuestions-1][0])+ "\hspace{3 mm} and \hspace{3 mm} " + str(Answers[NumQuestions-1][1])
    else:
        Answer = str(Answers[NumQuestions-1])
        Equations += "(" + str(NumQuestions) +") $"+ Answer+"$\\\\"
    #print Answer
    Equations += "\end{multicols}"
    Header = FileGetContents(header)
    Footer = FileGetContents(footer)
    #form1 = QuestionForm(string1)
    FileName = TopicObject1.TopicPrefix+"_A_"+str(subTopic)+"_"+str(difficulty_level)+".tex"
    #FileName = (TopicLookup[self.CurrentModule]).replace(" ","_")+"_answers_"+str(self.Data.subtopicChoice)+".tex"
    f = open( "./"+TopicObject1.TopicPrefix+"/"+FileName, 'w' )
    f.write( Header+Equations+Footer )
    f.close()
    os.system("pdflatex ./"+(TopicObject1.TopicPrefix)+"/"+FileName+" -interaction nonstopmode -output-directory "+TopicObject1.TopicLookup[CurrentModule])
    os.system("rm *.aux")
    os.system("rm *.log")
    os.system("rm *.out")
    os.system("rm *.tex")
    for topicList in TopicObject1.TopicCategories:
        try:
                os.system("mv "+topicList[0]+"*.pdf "+topicList[0])
        except:
                pass

NumQuestions=20
subtopicChoice = 0
DifficultyLevel= 0
ProblemName = "AR_Addition_Pairs"
TopicChoice = 1
subTopic = 0
T1 = special_problem_code.Topic(subtopicChoice)
for i in range(0, NumQuestions):
	T1.AddProblems(subtopicChoice, DifficultyLevel, ProblemName)
generateWorksheet(T1.Problems, subTopic, TopicObject1, subtopicChoice, TopicChoice, DifficultyLevel)




