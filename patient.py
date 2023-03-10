##########################################################
# Title: Alberta Hospital (AH) Management System 
# Author: Mark Anthony Pagarigan
# Version : v1.1
# Project: Classes Individual
##########################################################

class Patient:

    list_patients = []
    def __init__(self , pid=0, name="", disease="", gender="" ,age=0) :
        self.pid = pid 
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

# Method Name	
    def formatPatientInfo(self,obj):#	Formats patient information to be added to the file
        return ("\n"+" ".join(str(obj).split()).replace(" ","_"))

    def enterPatientInfo(self):#	Asks the user to enter the patient info 
        pid= int(input("Enter Patient id: "))
        name= input("Enter Patient name: ")
        disease= input("Enter Patient disease: ")
        gender= input("Enter Patient gender: ")
        age= int(input("Enter Patient age:"))

        patient = Patient(pid,name,disease,gender,age)
        return patient

    def readPatientsFile(self):#	Reads from file patients.txt
        file = open('patients.txt' , 'r')
        file_content = file.readlines()

        for eachline in file_content:
            self.list_patients.append(Patient(*eachline.rstrip('\n').split('_'))) 

    def searchPatientById(self):#	Searches for a patient using their ID
        search_patient_id = input("Enter the Patient Id: ")
        for index in range(1,len(self.list_patients)):#not include title
            if search_patient_id == self.list_patients[index].pid:
                print(self.list_patients[0]) 
                self.displayPatientInfo(index)
                break
        else:
            print("Can't find the patient with the same ID on the system")
        
    def displayPatientInfo(self,value):#	Displays patient info
        print(self.list_patients[value])

    def editPatientInfo(self): #	Asks the user to edit patient information
        search_id= input("Please enter the id of the Patient that you want to edit their information:  ")
        for index in range(1,len(self.list_patients)):
            if search_id == self.list_patients[index].pid:

                name= input("Enter new Name: ")
                disease= input("Enter new disease: ")
                gender= input("Enter new gender: ")
                age= int(input("Enter new age: "))

                updated_patient = Patient(search_id,name,disease,gender,age)
       
                self.list_patients[index]  = self.formatPatientInfo(updated_patient)
                self.writeListOfPatientsToFile()
                break
        else:
            print("Can't find the patient with the same ID on the system")

    def displayPatientsList(self):#	Displays the list of patients
        for index in range(len(self.list_patients)):
            print(self.list_patients[index])

    def writeListOfPatientsToFile(self):#	Writes a list of patients into the patients.txt file
        file = open('patients.txt', 'w')
        for index in range(len(self.list_patients)):
            file.write(self.formatPatientInfo(self.list_patients[index]))
        file.close()
    
    def addPatientToFile(self): #	Adds a new patient to the file
        file = open('patients.txt', 'a')
        newPatient = self.enterPatientInfo()
        file.write(self.formatPatientInfo(newPatient))
        file.close()
    
    def __str__(self):       
        return ("{:<5}  {:<12} {:<15} {:<15} {:<15}".format(self.pid, self.name, self.disease, self.gender, self.age))
            

    def patientMenu(self):
        while True:
            self.readPatientsFile()
            patient_option = int(input(""" Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

Option: """))

            if patient_option == 1:
                self.displayPatientsList()
            elif patient_option == 2:
                self.searchPatientById()
            elif patient_option == 3:
                self.addPatientToFile()
            elif patient_option == 4:
                self.editPatientInfo()
            elif patient_option == 5:
                break
            
            print("\nBack to the prevoius Menu")
            self.list_patients.clear()