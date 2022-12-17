##########################################################
# Title: Alberta Hospital (AH) Management System 
# Author: Mark Anthony Pagarigan
# Version : v1.1
# Project: Classes Individual
##########################################################

class Laboratory:
    list_lab = []
    def __init__(self,lab_name ="",cost=0) :
        self.lab_name = lab_name
        self.cost = cost

    def addLabToFile(self): #Adds and writes the lab name to the file in the format of the data that is in the file
        self.list_lab.append(self.enterLaboratoryInfo() )
        self.writeListOfLabsToFile()

    def writeListOfLabsToFile(self): #Writes the list of labs into the file laboratories.txt
        file = open('laboratories.txt', 'w')
        for index in range(len(self.list_lab)):
            file.write(self.formatLabInfo(self.list_lab[index]))
        file.close()

    def displayLabsList(self): #Displays the list of laboratories
        for index in range(len(self.list_lab)):
            print(self.list_lab[index])

    def formatLabInfo(self,obj): #Formats the Laboratory object similar to the laboratories.txt file
        return (" ".join(str(obj).split()).replace(" ","_")+"\n")
    
    def enterLaboratoryInfo(self): #Info Asks the user to enter lab name and cost and forms a Laboratory object
        lab_facility = input("Enter Laboratory facility: ")
        lab_cost = float(input("Enter Laboratory cost: "))
        obj_lab = Laboratory(lab_facility, lab_cost)
        return obj_lab

    def readLaboratoriesFile(self): #Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
            file = open('laboratories.txt','r')
            file_content = file.readlines()
            for eachline in file_content:
                self.list_lab.append(Laboratory(*eachline.rstrip('\n').split('_')))  
            file.close()

    def __str__(self):
        return ("{:<15}  {:<0} ".format(self.lab_name, self.cost ))
    

    def labMenu(self):
        
        while True:
            self.readLaboratoriesFile()
            lab_option = int(input("""Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

Option: """))

            if lab_option == 1:
                self.displayLabsList()
            if lab_option == 2:
                self.addLabToFile()
            if lab_option == 3:
                break

            print("\nBack to the prevoius Menu")
            self.list_lab.clear()