from PyQt5.QtWidgets import QMainWindow
import sys
from UserInterface import Ui_Form
from datastore import DataStore
from PyQt5.QtWidgets import QMessageBox

ds = DataStore()

class MainWindow():
    def __init__(self):
        msg = QMessageBox()
        self.main_win = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Welcome_Page)
        
        #Welcome Page Buttons
        self.ui.Continue_Button.clicked.connect(self.Home)
        self.ui.Exit_Button.clicked.connect(self.Exit)
        self.ui.Author_Button.clicked.connect(self.About_Me_Popup)

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
        self.ui.Logo_Button.clicked.connect(self.ssshhhSECRET)
        self.ui.Add_Test_Button.clicked.connect(self.Add_New_Test)
        
        #Patient 2 Use Buttons
        self.ui.Add_Patient_Button.clicked.connect(self.Add_New_Patient)
        self.ui.Previous_Page_Patients.clicked.connect(self.Previous_Page_Patients)
        self.ui.Update_Patient_Button.clicked.connect(self.Update_Patient_Details)

        #TestTaken Use Buttons
        self.ui.Search_TestTaken_Button.clicked.connect(self.Search_TestTaken)
        self.ui.Insert_Patient_Test_Button.clicked.connect(self.Add_Test_Taken)

    def Add_Test_Taken(self):
        name = self.ui.Insert_Patient_Name.text()
        code = self.ui.Insert_Test_Code.text() 
        date = self.ui.Insert_Date_Test_Taken.text() 
        result = self.ui.Insert_Test_Results.text() 
        ds.insert_patient_test_results(name, code, date, result)
        self.successful_popup()

    def Search_TestTaken(self):
        patient = self.ui.Search_Test_Taken_Name.text()
        info = ds.select_patient_results_all_tests(patient)
        self.ui.TestTaken_Seach_Field.setText(info)

    def Update_Test_Details(self):
        test = self.ui.Update_Test_Code.text()
        tests_list = ds.retrieve_test_code()
        if test not in tests_list:
            self.error()
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

            elif self.ui.Student_Number_Radio.isChecked():
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
                self.error()

     


    def Add_New_Test(self):
        code = self.ui.Add_Test_Code.text()
        name = self.ui.Add_Test_Name.text()
        description = self.ui.Add_Test_Desc.text()
        price = self.ui.Add_Test_Price.text()
        ds.insert_new_test(code, name, description, price)
        self.successful_popup()

    def Add_New_Patient(self):
        name = self.ui.Add_Patient_Name.text()
        num = self.ui.Add_Patient_Student_Number.text()
        dob = self.ui.Add_Patient_DOB.text()
        add = self.ui.Add_Patient_Address.text()
        postcode = self.ui.Add_Patient_Postcode.text()
        height = self.ui.Add_Patient_Height.text()
        weight = self.ui.Add_Patient_Weight.text()
        ds.insert_patient(name, num, dob, add, postcode, height, weight)
        self.successful_popup()


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
        patient = self.ui.Search_Patient_Name.text()
        patients = ds.select_patients_from_list()
        if patient not in patients:
            self.error()
        else:
            patient = ds.select_patient(patient)
            self.ui.Search_Patient_Field.setText(
                """
            Student Number: {}
            Date of Birth: {}
            Address:  {}
            Postcode: {}
            Height:   {}
            Weight:   {}""".format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))


    def safety_popup(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are You Sure?")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Show the message box and retrieve the button clicked
        button_clicked = msg.exec()
        #Check which button was clicked
        if button_clicked == QMessageBox.Yes:
            print("Real 100")
        elif button_clicked == QMessageBox.No:
            print("Brad")
        # Show the message box

    def Remove_Patient(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are You Sure?")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and retrieve the button clicked
        button_clicked = msg.exec()
        #Check which button was clicked
        if button_clicked == QMessageBox.Yes:
            patient = self.ui.Remove_Patient_Name.text()
            patients = ds.select_patients_from_list()
            if patient not in patients:
                self.error()
            else:
                ds.remove_patient(patient)
                self.successful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
   

    def Remove_Test(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are You Sure?")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and retrieve the button clicked
        button_clicked = msg.exec()
        #Check which button was clicked
        if button_clicked == QMessageBox.Yes:
            code = self.ui.Remove_Test_Code.text()
            test = ds.retrieve_test_code()
            if code not in test:
                self.error()
            else:
                ds.remove_test(code)
                self.successful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close





    def ListOfPatients(self):
        self.ui.List_Of_Patients_Field.setText(ds.select_patients_from_list, 1)

    def ListOfTests(self):
        self.ui.List_Of_Tests_Field.setText(ds.display_all_tests, 1)
        
    def ssshhhSECRET(self):
        msg = QMessageBox()
        msg.setText("look at u bro, this is kinda like the moment where you click freddys nose in fnaf like fr.")
        msg.setWindowTitle("SECRET FOUND!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.close)
        # Show the message box and retrieve the button clicked
        msg.exec()

    def error(self):
        msg = QMessageBox()
        # Set the text and title
        msg.setText("Error! Something has Gone Wrong! Please Try Again.")
        msg.setWindowTitle("ERROR!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Show the message box
        msg.exec()

    def Exit(self):
        exit()

    def show(self):
        self.main_win.show()

    def TestsTaken(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.TestsTaken)

    def successful_popup(self):
        msg = QMessageBox()
        # Set the text and title
        msg.setText("Operation Complete!")
        msg.setWindowTitle("Done!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Show the message box
        msg.exec()

    def About_Me_Popup(self):
        msg = QMessageBox()
        fia1 = "Fia1"
        tutor_app = ("Tutor App")
        github = ("@srcoggin")
        # Set the text and title
        msg.setText(f"""
                Thank you for using Bundy Health Care! 
                This App was Coded and Developed by Will Coggins 
                This App was Devleoped from 23/05/2023 to 26/05/2023
                Please Enjoy my other works such as {fia1}, and {tutor_app}. 
                Both of which can be found on my github: {github}
                    """)
        msg.setWindowTitle("About Me!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
    
        # Show the message box
        msg.exec()

    def Home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def Tests(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Test)

    def Patients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patient)

    