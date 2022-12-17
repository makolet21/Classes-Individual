##########################################################
# Title: Alberta Hospital (AH) Management System 
# Author: Mark Anthony Pagarigan
# Version : v1.1
# Project: Classes Individual
##########################################################

from doctor import Doctor
from facility import Facility
from laboratory import Laboratory
from patient import Patient

class Management:
    def DisplayMenu ():
    
        while True:
            menu_option = int (input('''\nWelcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 1

Option: '''))
            
            if menu_option == 1:
                Doctor().docMainMenu()
            elif menu_option == 2:
                Facility().facilityMenu()
            elif menu_option == 3:
                Laboratory().labMenu()
            elif menu_option == 4:
                Patient().patientMenu()
            elif menu_option == 0:
                break
    DisplayMenu ()



