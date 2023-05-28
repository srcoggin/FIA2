from PyQt5.QtWidgets import QMainWindow
import sys
from UserInterface import Ui_MainWindow
from datastore import DataStore
from PyQt5.QtWidgets import QMessageBox

ds = DataStore()

class MainWindow():
    def __init__(self):
        msg = QMessageBox()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
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
        self.ui.Patient_Test_2.clicked.connect(self.Patients)
        self.ui.Home_Test_2.clicked.connect(self.Home)
        self.ui.Tests_Test_2.clicked.connect(self.Tests)
        self.ui.TestsTaken_Test_2.clicked.connect(self.TestsTaken)
        
        #Patient Banner Buttons
        self.ui.Home_Patient.clicked.connect(self.Home)
        self.ui.Tests_Patient.clicked.connect(self.Tests)
        self.ui.TestsTaken_Patient.clicked.connect(self.TestsTaken)

        #Patient 2 Banner Buttons
        self.ui.Home_Patient_2.clicked.connect(self.Home)
        self.ui.Tests_Patient_2.clicked.connect(self.Tests)
        self.ui.TestsTaken_Patient_2.clicked.connect(self.TestsTaken)
        self.ui.Patient_Patient_2.clicked.connect(self.Patients)
        

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
        self.ui.Insert_Patient_Name.clear()
        self.ui.Insert_Test_Code.clear()
        self.ui.Insert_Date_Test_Taken.clear() 
        self.ui.Insert_Test_Results.clear()


    def Search_TestTaken(self):
        patient = ""
        for i in ds.select_patient_results_all_tests(self.ui.Search_Test_Taken_Name.text()):
            print(i)
            patient += f"{i} \n"
        self.ui.TestTaken_Seach_Field.setText(patient)

    def Update_Test_Details(self):
        tests = self.ui.Update_Test_Code.text()
        tests_list = ds.retrieve_test_code()
        if tests not in tests_list:
            self.error()
        else:
            if self.ui.Test_Name_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    updated_value = self.ui.UpdateTest_Name.text()
                    updated_selection = 0
                    ds.update_test(updated_selection, updated_value, tests)
                    self.successful_popup()
                    self.ui.Update_Test_Code.clear()
                    self.ui.UpdateTest_Name.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close
            
            elif self.ui.Test_DDescription_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    updated_value = self.ui.Update_Test_Desc.text()
                    updated_selection = 1
                    ds.update_test(updated_selection, updated_value, tests)
                    self.successful_popup()
                    self.ui.Update_Test_Code.clear()
                    self.ui.Update_Test_Desc.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Test_Price_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    updated_value = self.ui.Update_Test_Price.text()
                    updated_selection = 2
                    ds.update_test(updated_selection, updated_value, tests)
                    self.successful_popup()
                    self.ui.Update_Test_Code.clear()
                    self.ui.Update_Test_Price.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close
            else:
                self.error()
        

    def Update_Patient_Details(self):
        #Gets the patients name
        patient = self.ui.Update_Patient_Name.text()
        patients = ds.select_patients_from_list()
        #Checks to see if the name is in the data store
        if patient not in patients:
            #if not it errors
            self.error()
        else:
            #checks to see if this is the radio thats selected
            if self.ui.Patient_Address_Radio_2.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                #Check which button was clicked
                if button_clicked == QMessageBox.Yes:
                #grabs all the updated info and updates it in data store
                    address = self.ui.Update_Patient_Address_2.text()
                    updated_selection = 2
                    ds.update_patient(updated_selection, address, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_Address_2.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Patient_DOB_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    dob = self.ui.Update_Patient_DOB.text() 
                    updated_selection = 1
                    ds.update_patient(updated_selection, dob, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_DOB.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Student_Number_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    student_num = self.ui.Update_Patient_Student_Number.text()
                    updated_selection = 0
                    ds.update_patient(updated_selection, student_num, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_Student_Number.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Patient_Height_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    patient_height = self.ui.Update_Patient_Height.text()
                    updated_selection = 4
                    ds.update_patient(updated_selection, patient_height, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_Height.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Patient_Weight_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    patient_weight = self.ui.Update_Patient_Weight.text()
                    updated_selection = 5
                    ds.update_patient(updated_selection, patient_weight, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_Weight.clear()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close

            elif self.ui.Patient_Postcode_Radio.isChecked():
                msg = QMessageBox()
                #sets text of the pop up
                msg.setText("Are you sure you want to do this?")
                msg.setWindowTitle("Are You Sure?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Show the message box and retrieve the button clicked
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    patient_postcode = self.ui.Update_Patient_Postcode.text() 
                    updated_selection = 3
                    ds.update_patient(updated_selection, patient_postcode, patient)
                    self.successful_popup()
                    self.ui.Update_Patient_Name.clear()
                    self.ui.Update_Patient_Postcode.clear()
                if button_clicked == QMessageBox.No:
                        QMessageBox.close
            #if none of the options are selected it pops up with the error box
            else:
                self.error()

     


    def Add_New_Test(self):
        #grabs all the text in the line edits
        code = self.ui.Add_Test_Code.text()
        name = self.ui.Add_Test_Name.text()
        description = self.ui.Add_Test_Desc.text()
        price = self.ui.Add_Test_Price.text()
        #creates the new test in data store
        ds.insert_new_test(code, name, description, price)
        #Clears Line Edit
        self.ui.Add_Test_Code.clear()
        self.ui.Add_Test_Name.clear()
        self.ui.Add_Test_Desc.clear()
        self.ui.Add_Test_Price.clear()
        #displays that the action was successful
        self.successful_popup()

    def Add_New_Patient(self):
        #gets all of the text in the line edits
        name = self.ui.Add_Patient_Name.text()
        num = self.ui.Add_Patient_Student_Number.text()
        dob = self.ui.Add_Patient_DOB.text()
        add = self.ui.Add_Patient_Address.text()
        postcode = self.ui.Add_Patient_Postcode.text()
        height = self.ui.Add_Patient_Height.text()
        weight = self.ui.Add_Patient_Weight.text()
        #adds new patient in the data store
        ds.insert_patient(name, num, dob, add, postcode, height, weight)
        #Clears Line Edit
        self.ui.Add_Patient_Name.clear()
        self.ui.Add_Patient_Student_Number.clear()
        self.ui.Add_Patient_DOB.clear()
        self.ui.Add_Patient_Address.clear()
        self.ui.Add_Patient_Postcode.clear()
        self.ui.Add_Patient_Height.clear()
        self.ui.Add_Patient_Weight.clear()
        #displays that the action was successful
        self.successful_popup()


    def Previous_Page_Tests(self):
        #changes to the previous page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Test)

    def Next_Page_Tests(self):
        #changes to the next page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Tests2)   

    def Previous_Page_Patients(self):
        #changes to the previous page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patient)

    def Next_Patient_Page(self):
        #changes to the next page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients_2)

    def Search_Patient(self):
        #gets the patient name that's in the line edit
        patient = self.ui.Search_Patient_Name.text()
        patients = ds.select_patients_from_list()
        #checks to see if the name given is in the data store
        if patient not in patients:
            #if there is not a matching name it pops up with the error pop up
            self.error()
        else:
            #if there was a matching name, it grabs all of the patients info from data store and displays it in the label
            patient = ds.select_patient(patient)
            self.ui.Search_Patient_Field.setText(
                """
            Student Number: {}
            Date of Birth: {}
            Address:  {}
            Postcode: {}
            Height:   {}
            Weight:   {}""".format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))

    #this function legit does nothing, i replaced it but woudl rather just keep it here than delete it
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
      

    def Remove_Patient(self):
        msg = QMessageBox()
        #sets text of the pop up
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are You Sure?")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and retrieve the button clicked
        button_clicked = msg.exec()
        #Check which button was clicked
        if button_clicked == QMessageBox.Yes:
            #gets the patients name from the line edit
            patient = self.ui.Remove_Patient_Name.text()
            patients = ds.select_patients_from_list()
            #checks to see if that name exsists in the data store
            if patient not in patients:
                #if there isn't a match the error pop up appears
                self.error()
            else:
                #if there was a match the patient is removed
                ds.remove_patient(patient)
                self.successful_popup()
        elif button_clicked == QMessageBox.No:
            #if the user wants to back out this closes the safety box and does not excute the action
            QMessageBox.close
   

    def Remove_Test(self):
        msg = QMessageBox()
        #sets the text of the pop up box
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are You Sure?")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and retrieve the button clicked
        button_clicked = msg.exec()
        #Check which button was clicked
        if button_clicked == QMessageBox.Yes:
            #gets the test code from the line edit
            code = self.ui.Remove_Test_Code.text()
            test = ds.retrieve_test_code()
            #checks to see if that code exsists in the data store
            if code not in test:
                #if there isn't a match the error pop up appears
                self.error()
            else:
                #if there was a match then it removes the test from data store
                ds.remove_test(code)
                self.successful_popup()
        elif button_clicked == QMessageBox.No:
            #if the client selects no, the pop up box closes and the action is not excecuted
            QMessageBox.close

    def ListOfPatients(self):
        #gathers the list of patients from data store and displays them
        name =  ""
        for i in ds.select_patients_from_list():
            name += f"{i} \n"
        self.ui.List_Of_Patients_Field.setText(name)

    def ListOfTests(self):
        #gathers the list of tests from data store and displays them
        code =  ""
        for i in ds.display_all_tests():
            code += f"{i} \n"
        self.ui.List_Of_Tests_Field.setText(code)
        
    def ssshhhSECRET(self):
        msg = QMessageBox()
        #sets the text of the pop up box, obviously. This is the 3rd or 4th time I've had to say this corey come on man
        msg.setText("look at u bro, this is kinda like the moment where you click freddys nose in fnaf like fr.")
        msg.setWindowTitle("SECRET FOUND!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Show the message box and retrieve the button clicked (excecutes the pop up)
        msg.exec()

    def error(self):
        msg = QMessageBox()
        # Set the text and title
        msg.setText("Error! Something has Gone Wrong! Please Try Again.")
        msg.setWindowTitle("ERROR!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Shows the message box
        msg.exec()

    def Exit(self):
        #exit the program, obviously
        exit()

    def show(self):
        #man like i dont even know
        self.main_win.show()

    def TestsTaken(self):
        #sets the current page
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
        brad = "Brad"
        github = ("@srcoggin")
        # Set the text and title
        msg.setText(f"""
        Thank you for using Bundy Health Care! 
        This App was Coded and Developed by Will Coggins 
        This App was Devleoped from 23/05/2023 to 26/05/2023
        Please Enjoy my other works such as {fia1}, {tutor_app}, and {brad}. 
        All of which and many more fun and serious Python coded projects can be found on my github: 
        {github}: Please follow and Star my Repos
                    """)
        msg.setWindowTitle("About Me!")
        #Set the buttons to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Show the message box
        msg.exec()

    def Home(self):
        #sets the current page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def Tests(self):
        #sets the current page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Test)

    def Patients(self):
        #sets the current page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patient)

    