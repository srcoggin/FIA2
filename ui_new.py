from PyQt5.QtWidgets import QMainWindow
import sys
from MainWindow import Ui_Form
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
        

        #TestsTaken Banner Buttons
        self.ui.Home_TestTaken.clicked.connect(self.Home)
        self.ui.Tests_TestTaken.clicked.connect(self.Tests)
        self.ui.Patient_TestTaken.clicked.connect(self.Patients)


        #Patient Use Buttons
        self.ui.ListOfPatient_Button.clicked.connect(self.ListOfPatients)
        self.ui.Search_Patient_Button.clicked.connect(self.Search_Patient)

        #Test Use Buttons
        self.ui.ListOfTests_Button.clicked.connect(self.ListOfPatients)

    def Search_Patient(self):
        name = str(self.ui.Search_Patient_Name.text())
        patients = ds.select_patients_from_list()
        if name not in patients:
            self.error()
        else:
            patient = ds.select_patient(patient)
            self.ui.Search_Patient_Field.setText(
                """Student Number: {}
Date of Birth: {}
Address:  {}
Postcode: {}
Height:   {}
Weight:   {}""".format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5])
                                                 
                                                 
                                                 
                                                 )

    def Remove_Patient(self):
        name = self.ui.Remove_Patient_Name.text()
        ds.remove_patient(name)

    def ListOfPatients(self):
        self.ui.List_Of_Patients_Field.setText(ds.select_patients_from_list())

    def ListOfTests(self):
        self.ui.List_Of_Tests_Field.setText(ds.display_all_tests)
        
    def error(self, Feild):
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

    