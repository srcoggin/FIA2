# imports the relevant classes from each of our modular files
from datastore import DataStore
from MainWindow import MainWindow
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

# creates variables that can be accessed to call functions from the other modules.
data_store = DataStore()


def display_patients():
    """
    Searches the database and returns all of the users added to the clinic database

    """
    patients = data_store.select_patients_from_list()
    ui.show_patients(patients)
    ui.complete_input()


def search_patients():
    """
    Gets input from the user to search the database and return specific info about the patient.
    Then ask the user if they would like to repeat the function again for another or the same patient
    """
    patient = ui.select_patient()
    patients = data_store.select_patients_from_list()
    if patient not in patients:
        ui.bad_input()
    else:
        patient = data_store.select_patient(patient)
        ui.show_individual_patient(patient)
        ui.complete_input()
        yorn = ui.continue_selection()
        if yorn == 'y':
            search_patients()


def update_or_add_patient_test():
    """
    Gets the user to pick from 2 options and then sends them to the function they require
    """
    selection = ui.update_add_patient_test()
    if selection == '1':
        update_patient()
    elif selection == '2':
        add_patient_test()


def update_patient():
    """
    Gets Input from the user for a specific patient
    Gets that patient from the database and returns all info about the patient
    Send all information to be displayed to the ui for user to pick which info to update
    selection from the ui then gets sent to database to update in database
    """
    patient_ui = ui.select_patient()
    patients = data_store.select_patients_from_list()
    if patient_ui not in patients:
        ui.bad_input()
    else:
        patient = data_store.select_patient(patient_ui)
        updated_selection = ui.update_patient_menu(patient)
        updated_value = ui.update_input()
        updated_selection -= 1
        data_store.update_patient(updated_selection, updated_value, patient_ui)
        ui.updated_text()
        ui.show_individual_patient(patient)
        yorn = ui.continue_selection()
        if yorn == 'y':
            update_patient()


def add_remove_patient():
    option = ui.add_remove_patient()
    if option == '1':
        add_new_patient()
    elif option == '2':
        remove_patient()


def add_new_patient():
    ui.add_text()
    name, num, dob, add, postcode, height, weight = list(ui.add_input())
    data_store.insert_patient(name, num, dob, add, postcode, height, weight)
    ui.complete_input()


def remove_patient():
    ui.remove_text()
    name = ui.remove_input()
    data_store.remove_patient(name)
    ui.complete_input()


def display_tests_types():
    code = data_store.display_all_tests()
    ui.show_all_tests(code)
    ui.complete_input()


def add_patient_test():
    name, code, date, result = ui.add_patient_test_menu()
    data_store.insert_patient_test_results(name, code, date, result)
    ui.complete_input()

def add_remove_test_type():
    selection = ui.add_remove_test()
    if selection == '1':
        add_new_test()
    elif selection == '2':
        remove_test()


def add_new_test():
    code, name, description, price = ui.add_test_input()
    data_store.insert_new_test(code, name, description, price)
    ui.complete_input()


def remove_test():
    code = ui.test_type_input()
    data_store.remove_test(code)
    ui.complete_input()


def display_patient_tests():
    patient = ui.patient_test_input()
    info = data_store.select_patient_results_all_tests(patient)
    ui.show_patient_tests(info)
    ui.complete_input()


def update_test_types():
    test_ui = ui.test_type_input()
    tests_list = data_store.retrieve_test_code()
    if test_ui not in tests_list:
        ui.bad_input()
    else:
        tests = data_store.select_test(test_ui)
        updated_selection = ui.update_test_menu(tests)
        updated_value = ui.update_input()
        updated_selection -= 1
        data_store.update_test(updated_selection, updated_value, test_ui)
        ui.updated_text()
        ui.show_individual_test(tests)
        yorn = ui.continue_selection()
        if yorn == 'y':
            update_patient()


def option_quit():
    exit()


##########################################################
# if __name__ == '__main__':
app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
app.exec_()
# ui.welcome()

# Application Menu
running = True
while running:
    QtCore.QCoreApplication.processEvents()
    menu_selection = ui.menu()
    # if menu_selection == 1:
    #     display_patients()
    # elif menu_selection == 2:
    #     search_patients()
    # elif menu_selection == 3:
    #     update_or_add_patient_test()
    # elif menu_selection == 4:
    #     add_remove_patient()
    # elif menu_selection == 5:
    #     display_tests_types()
    # elif menu_selection == 6:
    #     display_patient_tests()
    # elif menu_selection == 7:
    #     update_test_types()
    # elif menu_selection == 8:
    #     add_remove_test_type()
    # elif menu_selection == 9:
    #     option_quit()
    #     running = False
