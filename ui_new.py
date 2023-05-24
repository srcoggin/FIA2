from PyQt5.QtWidgets import QMainWindow
import sys
from MainWindow import Ui_Form

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
        self.ui.Patient_Test.clicked.connect(self.Tests)

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

    