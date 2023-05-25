from PyQt5.QtWidgets import QMainWindow
import sys
from UserInterface import Ui_Form
from datastore import DataStore

ds = DataStore()

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Welcome_Page)
        
        #Welcome Page Buttons
        self.ui.Continue_Button.clicked.connect(self.Home)
        self.ui.Exit_Button.clicked.connect(self.Exit)

        #Home Banner Buttons
        self.ui.Tests_Home.clicked.connect(self.Tests)
        self.ui.Patient_Home.clicked.connect(self.Patients)
        self.ui.TestsTaken_Home.clicked.connect(self.TestsTaken)

        #Test Banner Buttons
        self.ui.Home_Test.clicked.connect(self.Home)
        self.ui.TestsTaken_Test.clicked.connect(self.TestsTaken)
        self.ui.Patient_Test.clicked.connect(self.Patients)

        #Test 2 Banner Buttons
        self.ui.Patient_Test_2.clicked.connect(self.Tests)
        self.ui.Home_Test_2.clicked.connect(self.Home)
        self.ui.TestsTaken_Test_2.clicked.connect(self.TestsTaken)
        
        #Patient Banner Buttons
        self.ui.Home_Patient.clicked.connect(self.Home)
        self.ui.Tests_Patient.clicked.connect(self.Tests)
        self.ui.TestsTaken_Patient.clicked.connect(self.TestsTaken)

        #Patient 2 Banner Buttons
        self.ui.Home_Patient_2.clicked.connect(self.Home)
        self.ui.Tests_Patient_2.clicked.connect(self.Tests)
        self.ui.TestsTaken_Patient_2.clicked.connect(self.TestsTaken)
        self.ui.Previous_Page_Patients.clicked.connect(self.Previous_Page_Patients)
        

        #TestsTaken Banner Buttons
        self.ui.Home_TestTaken.clicked.connect(self.Home)
        self.ui.Tests_TestTaken.clicked.connect(self.Tests)
        self.ui.Patient_TestTaken.clicked.connect(self.Patients)


        #Patient Use Buttons
        self.ui.ListOfPatient_Button.clicked.connect(self.ListOfPatients)
        self.ui.Search_Patient_Button.clicked.connect(self.Search_Patient)
        self.ui.Remove_Patient_Button.clicked.connect(self.Remove_Patient)
        self.ui.Next_Page_Patients.clicked.connect(self.Next_Patient_Page)

        #Test Use Buttons
        self.ui.Remove_Test_Button.clicked.connect(self.Remove_Test)
        self.ui.Next_Page_Tests.clicked.connect(self.Next_Page_Tests)
        self.ui.Update_Test_Details_Button.clicked.connect(self.Update_Test_Details)

        #Test 2 Use Buttons
        self.ui.Previous_Page_Test.clicked.connect(self.Previous_Page_Tests)
        self.ui.ListOfTests_Button.clicked.connect(self.ListOfTests)
        self.ui.Add_Test_Button.clicked.connect(self.Add_New_Test)
        
        #Patient 2 Use Buttons
        self.ui.Add_Patient_Button.clicked.connect(self.Add_New_Patient)
        self.ui.Previous_Page_Patients.clicked.connect(self.Previous_Page_Patients)
        self.ui.Update_Patient_Button.clicked.connect(self.Update_Patient_Details)

        #TestTaken Use Buttons
        self.ui.Search_TestTaken_Button.clicked.connect(self.Search_TestTaken)
        self.ui.Insert_Patient_Test_Button.clicked.connect(self.Add_Test_Taken)

    def Add_Test_Taken(self):
        output = "Test has been Updated!"
        name = self.ui.Insert_Patient_Name.text()
        code = self.ui.Insert_Test_Code.text() 
        date = self.ui.Insert_Date_Test_Taken.text() 
        result = self.ui.Insert_Test_Results.text() 
        ds.insert_patient_test_results(name, code, date, result)
        self.ui.TestTaken_Confirm.setText(output)

    def Search_TestTaken(self):
        patient = self.ui.Search_Test_Taken_Name.text()
        info = ds.select_patient_results_all_tests(patient)
        self.ui.TestTaken_Seach_Field.setText(info)

    def Update_Test_Details(self):
        test = self.ui.Update_Test_Code.text()
        tests_list = ds.retrieve_test_code()
        if test not in tests_list:
            self.error
        else:
            if self.ui.Test_Name_Radio.isChecked():
                tests = ds.select_test(test)
                updated_value = self.ui.UpdateTest_Name.text()
                updated_selection = 0
                ds.update_test(updated_selection, updated_value, tests)
            
            elif self.ui.Test_DDescription_Radio.isChecked():
                tests = ds.select_test(test)
                updated_value = self.ui.Update_Test_Desc.text()
                updated_selection = 1
                ds.update_test(updated_selection, updated_value, tests)

            elif self.ui.Test_Price_Radio.isChecked():
                tests = ds.select_test(test)
                updated_value = self.ui.Update_Test_Price.text()
                updated_selection = 2
                ds.update_test(updated_selection, updated_value, tests)
            else:
                self.error()
        

    def Update_Patient_Details(self):
        patient = self.ui.Update_Patient_Name.text()
        patients = ds.select_patients_from_list()
        if patient not in patients:
            self.error()
        else:
            if self.ui.Patient_Address_Radio_2.isChecked():
                address = self.ui.Update_Patient_Address.text()
                select_patient = ds.select_patient(patient)
                updated_selection = 2
                ds.update_patient(updated_selection, address, select_patient)

            elif self.ui.Patient_DOB_Radio.isChecked():
                dob = self.ui.Update_Patient_DOB.text()
                select_patient = ds.select_patient(patient)
                updated_selection = 1
                ds.update_patient(updated_selection, dob, select_patient)

            elif self.ui.Student_Number_Radio.ischecked():
                student_num = self.ui.Update_Patient_Student_Number.text()
                select_patient = ds.select_patient(patient)
                updated_selection = 0
                ds.update_patient(updated_selection, student_num, select_patient)

            elif self.ui.Patient_Height_Radio.ischecked():
                patient_height = self.ui.Update_Patient_Height.text()
                select_patient = ds.select_patient(patient)
                updated_selection = 4
                ds.update_patient(updated_selection, patient_height, select_patient)

            elif self.ui.Patient_Weight_Radio.isChecked():
                patient_weight = self.ui.Update_Patient_Weight.text()
                select_patient  = ds.select_patient(patient)
                updated_selection = 5
                ds.update_patient(updated_selection, patient_weight, select_patient)

            elif self.ui.Patient_Postcode_Radio.isChecked():
                patient_postcode = self.ui.Update_Patient_Postcode.text()
                select_patient = ds.select_patient(patient)
                updated_selection = 3
                ds.update_patient(updated_selection, patient_postcode, select_patient)
            else:
                self.error

     


    def Add_New_Test(self):
        output = "Test Added!"
        code = self.ui.Add_Test_Code.text()
        name = self.ui.Add_Test_Name.text()
        description = self.ui.Add_Test_Desc.text()
        price = self.ui.Add_Test_Price.text()
        ds.insert_new_test(code, name, description, price)
        self.ui.Add_Test_Confirm.setText(output)

    def Add_New_Patient(self):
        output = "Patient Added!"
        name = self.ui.Add_Patient_Name.text()
        num = self.ui.Add_Patient_Student_Number.text()
        dob = self.ui.Add_Patient_DOB.text()
        add = self.ui.Add_Patient_Address.text()
        postcode = self.ui.Add_Patient_Postcode.text()
        height = self.ui.Add_Patient_Height.text()
        weight = self.ui.Add_Patient_Weight.text()
        ds.insert_patient(name, num, dob, add, postcode, height, weight)
        self.ui.Add_Patient_Confirm.setText(output)


    def ListOfTests(self):
        self.ui.List_Of_Tests_Field.setText(ds.display_all_tests)    

    def Previous_Page_Tests(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Test)

    def Next_Page_Tests(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Tests2)   

    def Previous_Page_Patients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patient)

    def Next_Patient_Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients_2)

    def Search_Patient(self):
        paitent = self.ui.Search_Patient_Name.text()
        patients = ds.select_patients_from_list()
        if patient not in patients:
            self.error()
        else:
            patient = ds.select_patient(patient)
            self.ui.Search_Patient_Field.setText(
                """Student Number: {}
                    Date of Birth: {}
                    Address:  {}
                    Postcode: {}
                    Height:   {}
                    Weight:   {}""".format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))


    def Remove_Patient(self):
        name = self.ui.Remove_Patient_Name.text()
        patients = ds.select_patients_from_list
        if name not in patients:
            self.error()
        else:
            output = "Patient Removed"
            ds.remove_patient(name)
            self.ui.Remove_Patient_Confirm_Field.setText(output)

    def Remove_Test(self):
        code = self.ui.Remove_Test_Code.text()
        test = ds.retrieve_test_code()
        if code not in test:
            self.error()
        else:
            output = "Test Removed"
            ds.remove_test(code)
            self.ui.Remove_Test_Confirm_Field.setText(output)

    def ListOfPatients(self):
        self.ui.List_Of_Patients_Field(ds.select_patients_from_list())

    def ListOfTests(self):
        self.ui.List_Of_Tests_Field.setText(ds.display_all_tests)
        
    def error(self):
        pass
    #PLEASE MAKE ME A POP UP, DONT FORGET AGAIN IDIOT

    def Exit(self):
        exit()

    def show(self):
        self.main_win.show()

    def TestsTaken(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.TestsTaken)

    def Home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def Tests(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Test)

    def Patients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patient)

    