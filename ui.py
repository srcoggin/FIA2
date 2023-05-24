class Ui:
    """
    This class provides the user interface for The Southport School Health Centre's Pathology Application
    """
    def __init__(self):
        self.welcome_text = \
            """
####################################################################################################################
####################################################################################################################
####################################################################################################################
##  ______     __  __     __   __     _____     __  __        __    __     ______     _____     __     ______     ##
## /\  == \   /\ \/\ \   /\ "-.\ \   /\  __-.  /\ \_\ \      /\ "-./  \   /\  ___\   /\  __-.  /\ \   /\  ___\    ##
## \ \  __<   \ \ \_\ \  \ \ \-.  \  \ \ \/\ \ \ \____ \     \ \ \-./\ \  \ \  __\   \ \ \/\ \ \ \ \  \ \ \____   ##
##  \ \_____\  \ \_____\  \ \_\\"\_\  \ \____-  \/\_____\     \ \_\ \ \_\  \ \_____\  \ \____-  \ \_\  \ \_____\  ##
##   \/_____/   \/_____/   \/_/ \/_/   \/____/   \/_____/      \/_/  \/_/   \/_____/   \/____/   \/_/   \/_____/  ##
##                                                                                                                ##
####################################################################################################################
####################################################################################################################
####################################################################################################################
            """
        self.menu_text = \
            """
Please make a selection from the menu below to complete the required operation (1-9):
 -----------------------
1. Display Patients
2. Search Patient
3. Update / Insert Patient Results
4. Add / Remove Patient
 -----------------------
5. Display All Test Types
6. Display Patient Tests
7. Update Test Type
8. Add / Remove Test Type
 -----------------------
9. Quit

> """

        self.display_patient = \
            """
Choose Patient:    
> """

        self.continue_update_selection_text = \
            """
Select Another? (y/n)
> """

        self.add_remove_patient_text = \
            """
1. Add Patient
2. Remove Patient
> """

        self.update_add_patient_tests_text = \
            """
1. Update Patient
2. Add Patient Test
> """

        self.add_remove_test_text = \
            """
1. Add Test
2. Remove Test
> """

    def welcome(self):
        print(self.welcome_text)
        print()
        input("Press Enter to continue ...")

    def menu(self):
        """
        Returns the selected menu value from the menu to the main module
        """
        selection = input(self.menu_text)
        if selection.isdigit():
            selection = int(selection)
        else:
            selection = -1

        return selection

    def continue_selection(self):
        selection = input(self.continue_update_selection_text).casefold()
        if not selection.isdigit():
            selection = str(selection)
        else:
            selection = -1

        return selection

    def add_remove_patient(self):
        selection = input(self.add_remove_patient_text)
        if selection.isdigit():
            selection = str(selection)
        else:
            selection = -1

        return selection

    def update_add_patient_test(self):
        selection = input(self.update_add_patient_tests_text)
        if selection.isdigit():
            selection = str(selection)
        else:
            selection = -1

        return selection

    def add_remove_test(self):
        selection = input(self.add_remove_test_text)
        if selection.isdigit():
            selection = str(selection)
        else:
            selection = -1

        return selection

    @staticmethod
    def update_patient_menu(patient):
        """
        Returns the selected value to update from the menu to the main module
        """

        selection = input("""Select the patient's aspect to update:
1. Student Number.      Current: {}
2. Date of Birth.       Current: {}
3. Address.             Current: {}
4. Postcode.            Current: {}
5. Height.              Current: {}
6. Weight.              Current: {}  

> """.format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))

        if selection.isdigit():
            selection = int(selection)
        else:
            selection = -1

        return selection

    @staticmethod
    def add_patient_test_menu():
        name = str(input("Enter Patient:    "))
        code = str(input("Enter Test Code:  "))
        date = str(input("Enter Date Taken: "))
        result = str(input("Enter Result:   "))
        return name, code, date, result

    @staticmethod
    def update_input():
        value = input("Enter updated value: ")
        return value

    @staticmethod
    def updated_text():
        print()
        print("Updated values: ")

    @staticmethod
    def add_text():
        print()
        print("Add patient values:")

    @staticmethod
    def add_input():
        name = str(input("Enter Patient Name: "))
        num = int(input("Enter Student Number: "))
        dob = str(input("Enter New D.O.B: "))
        add = str(input("Enter New Address: "))
        postcode = str(input("Enter New Postcode: "))
        height = str(input("Enter New Height: "))
        weight = str(input("Enter New Weight: "))
        return name, num, dob, add, postcode, height, weight

    @staticmethod
    def remove_text():
        print()
        print("Remove Patient:")

    @staticmethod
    def remove_input():
        name = str(input("Enter Patient to Remove: "))
        return name

    @staticmethod
    def bad_input():
        print(" *** Invalid Option *** ")
        input("Press Enter to continue ...")

    @staticmethod
    def complete_input():
        print()
        print(" *** Task Complete ***")
        input("Press Enter to continue ...")

    @staticmethod
    def select_patient():
        print()
        patient = str(input("Choose Patient:  "))
        return patient

    @staticmethod
    def record_updated():
        """
        Displays a confirmation message to the user
        """
        print()
        print(" *** Record Updated Successfully ***")
        input("Press Enter to continue ...")

    @staticmethod
    def show_individual_patient(patient):
        """
        Displays Date of birth, address, postcode, height and weight visable for the user.
        """

        print("""Student Number: {}
Date of Birth: {}
Address:  {}
Postcode: {}
Height:   {}
Weight:   {}""".format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))

    @staticmethod
    def show_individual_test(test):
        """
        Displays Date of birth, address, postcode, height and weight visable for the user.
        """

        print("""Name:         {}
Description:  {}
Price:        {}""".format(test[0], test[1], test[2]))

    @staticmethod
    def show_patients(patient_list):
        for i in patient_list:
            print(i)

    @staticmethod
    def show_updated_patient():
        print()

    @staticmethod
    def patient_test_input():
        patient = input("Patient's test's to display: ")
        return patient

    @staticmethod
    def test_type_input():
        code = input("Test Code: ")
        return code

    @staticmethod
    def show_all_tests(code):
        for k, i in code:
            print("""
Test Code:  {}
Expanded:   {}
Definition: {}
Price:      {}
""".format(k, i[0], i[1], i[2]))

    @staticmethod
    def show_patient_tests(info):
        for i in info:
            print("""
Test Type: {}
- Date:    {}
- Result:  {}""".format(i[0], i[1], i[2]))

    @staticmethod
    def update_test_menu(test):
        """
        Returns the selected value to update from the menu to the main module
        """
        selection = input("""Select the test's aspect to update:
1. Name.            Current: {}
2. Description.     Current: {}
3. Price.           Current: {}

> """.format(test[0], test[1], test[2]))

        if selection.isdigit():
            selection = int(selection)
        else:
            selection = -1

        return selection

    @staticmethod
    def add_test_input():
        code = str(input("Enter Test Code: "))
        name = str(input("Enter Test Name: "))
        description = str(input("Enter Description: "))
        price = str(input("Enter Test Price: "))
        return code, name, description, price

