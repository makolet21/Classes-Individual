##########################################################
# Title: Alberta Hospital (AH) Management System 
# Author: Mark Anthony Pagarigan
# Version : v1.3
# Project: Classes Individual
##########################################################


class Doctor:

    doctor_list = []
    def __init__(self ,id = 0, name = "",specialization = "", working_time = "", qualification = "", room_number = ""):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
 
#Formats each doctor’s information (propertis) in the same format used in  the .txt file (i.e., has uderscores between values)
    def formatDrInfo(self, obj):
        return ("\n"+" ".join(str(obj).split()).replace(" ","_"))
   
 #Asks the user to enter doctor properties (listed in the Properties point)
    def enterDrInfo(self): 
        id= int(input("Enter the doctor’s ID: "))
        name= input("Enter the doctor’s Name: ")
        specialization= input("Enter the doctor’s specialization: ")
        working_time= input("Enter the doctor’s working_time: ")
        qualification= input("Enter the doctor’s qualification: ")
        room_number= int(input("Enter the doctor’s room_number: "))

        doctor = Doctor(id,name.replace(" ",""),specialization,working_time,qualification,room_number)
        return doctor
        

#Reads from “doctors.txt” file and fills the doctor objects in a list
    def readDoctorsFile(self):
        file = open('doctors.txt' , 'r')
        file_content = file.readlines()

        for eachline in file_content:
            #append list of object and remove any spaces between ex Dr. Ross to Dr.Ross
            self.doctor_list.append(Doctor(*eachline.replace(" ","").rstrip('\n').split('_')))                        
        #print(self.doctor_list) 
        
 # Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    def searchDoctorById(self):   
        search_doc_id = input("Enter Doctor's ID: ")
        for index in range(1,len(self.doctor_list)):#not include title
            if search_doc_id == self.doctor_list[index].id:
                print(self.doctor_list[0]) #print title
                self.displayDoctorInfo(index)
                break
        else:
            print("Can't find the doctor with the same ID on the system")

# Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    def searchDoctorByName(self): 
        search_doc_name = input("Enter Doctor's Name: ")
        for index in range(1,len(self.doctor_list)):
            if search_doc_name == self.doctor_list[index].name:
                print(self.doctor_list[0]) 
                self.displayDoctorInfo(index)
                break
        else:
            print("Can't find the doctor with the same name on the system")

 # Displays doctor information on different lines, as a list
 #single?
    def displayDoctorInfo(self , value):
        print(self.doctor_list[value])

# Asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    def editDoctorInfo(self):
        search_id= input("Please enter the id of the doctor that you want to edit their information: ")
        for index in range(1,len(self.doctor_list)):
            if search_id == self.doctor_list[index].id:

                name= input("Enter new Name: ")
                specialization= input("Enter new Specilist in: ")
                working_time= input("Enter new Timing:  ")
                qualification= input("Enter new Qualification: ")
                room_number= int(input("Enter new Room number: "))

                updated_doctor = Doctor(search_id,name.replace(" ",""),specialization,working_time,qualification,room_number)
       
                self.doctor_list[index]  = self.formatDrInfo(updated_doctor)
                self.writeListOfDoctorsToFile()
                break
        else:
            print("Can't find the doctor with the same ID on the system")

# Displays all the doctors’ information, read from the file, as a report/table
    def displayDoctorsList(self): 
        
        for index in range(len(self.doctor_list)):
            print(self.doctor_list[index])

# Writes the list of doctors to the doctors.txt file after formatting it correctly 
    def writeListOfDoctorsToFile(self): 
        file = open('doctors.txt', 'w')
        for index in range(len(self.doctor_list)):
            file.write(self.formatDrInfo(self.doctor_list[index]))
        file.close()

# Writes doctors to the doctors.txt file after formatting it correctly
    def addDrToFile(self):
        file = open('doctors.txt', 'a')
        newDoctor = self.enterDrInfo()
        file.write(self.formatDrInfo(newDoctor))
        file.close()
 

    def __str__(self):
        return ("{:<5}  {:<12} {:<15} {:<15} {:<15} {:0}".format(self.id, self.name, self.specialization, self.working_time, self.qualification, self.room_number ))
    
#===============================================

    def docMainMenu(self):
        while True:   
            
            self.readDoctorsFile()
            doctors_menu = int(input('''Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

Option: '''))

            if doctors_menu == 1:
                self.displayDoctorsList()
            elif doctors_menu == 2:
                self.searchDoctorById()
            elif doctors_menu == 3:
                self.searchDoctorByName()
            elif doctors_menu == 4:
                self.addDrToFile()
            elif doctors_menu == 5:
                self.editDoctorInfo()
            
            print("\nBack to the prevoius Menu")
         
         
            if doctors_menu == 6:
                break
            
            self.doctor_list.clear()
              