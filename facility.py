##########################################################
# Title: Alberta Hospital (AH) Management System 
# Author: Mark Anthony Pagarigan
# Version : v1.1
# Project: Classes Individual
##########################################################

class Facility:

    list_facility = []
    def __init__(self, name=""):
        self.name = name 
        
# # Methods
    def addFacility(self):#Adds and writes the facility name to the file
        name = input("Enter Facility name: ")
        self.list_facility.append("\n"+name )
        self.writeListOffacilitiesToFile()
    

    def displayFacilities(self): #Displays the list of facilities
        self.list_facility.clear()
        file = open('facilities.txt', 'r')
        file_content = file.readlines()   
        for eachline in file_content:
            self.list_facility.append(eachline)
        print  ("".join(self.list_facility) + "\n")
        

    def writeListOffacilitiesToFile(self): #writes the facilities list to facilities.txt
        file = open('facilities.txt' , 'w')
        file.write("".join(self.list_facility))
        file.close()

#======================================================
    def facilityMenu(self):
        while True:
            facility_option = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\nOption: "))
            if facility_option == 1:
                self.displayFacilities()
            elif facility_option == 2:
                self.addFacility()
            elif facility_option == 3:
                break

            print("\nBack to the prevoius Menu")
        
       