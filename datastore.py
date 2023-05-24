from typing import ClassVar, Dict, List, Union


class DataStore:
    """
    This class provides the interface for the Vikings Pathology application
    It holds the data store and functions to read and manipulate the patient test data.

    Attributes:
        test_type [Dict[str, List[Union[str, int]]] A test name, Description and Cost
        patient [Dict[str, List[str]]] A patient, their details
        tests_taken [Dict[str, List[List[str]]]] A List of patient tests and results
    """

    def __init__(self):
        self.test_type: ClassVar[Dict[str, List[Union[str, int]]]] = {}
        self.patient: ClassVar[Dict[str, List[str]]] = {}
        self.tests_taken: ClassVar[Dict[str, List[List[str]]]] = {}

        self.data_import()

    def insert_patient(self, name: str, num: int, dob: str, add: str, postcode: str, height: int, weight: int):
        """
            Description:
                Inserts a new patient record into the system
            Args:
                name (str): The new patient being added to the system
                num (int): The patient's studend ID number
                dob (str): The patients date of birth
                add (str): The new patient's address
                postcode (str): The new patient's postcode
                height (str): Patient height
                weight (str): Patient weight
        """
        self.patient[name] = [num, dob, add, postcode, height, weight]

    def remove_patient(self, name: str):
        """
            Desription:
                Removes specific patient the system
            Args:
                name (str): The patient that is to be deleted
        """
        del self.patient[name]

    def select_patient(self, name: str) -> List[str]:
        """
            Description:
                Selects the patient and returns the patient's contact information
            Args:
                name (str): The name of the patient being searched.

            Returns:
                patient (list containing Patient name, dob, address, postcode, height, weight)
        """
        patient = self.patient.get(name)
        return patient

    def update_patient(self, updated_selection, updated_value, patient):
        """
                    Description:
                        Overwrite the current selected patient's information with new values
                    Args:
                        updated_selection (int) - the selection order from the ui to select the list position
                        updated_value (str) - the new value to replace the old one
                        patient (str) - the selected patient to have values updated﻿﻿
        """
        self.patient[patient][updated_selection] = updated_value

    def update_test(self, updated_selection, updated_value, test):
        """
                    Description:
                        Overwrite the current selected test's information with new values
                    Args:
                        updated_selection (int) - the selection order from the ui to select the list position
                        updated_value (str) - the new value to replace the old one
                        test (str) - the selected test to have values updated﻿﻿
        """
        self.test_type[test][updated_selection] = updated_value

    def select_patients_from_list(self):
        """
            Description:
                Selects all patient from the dictionary
            Returns:
                patient_list
        """
        patient_list = list(self.patient.keys())
        return patient_list

    def insert_patient_test_results(self, name: str, test: str, result: str, datetime: str):
        """
            Description:
                Inserts a new test result into the system.
            Args:
                name (str): The name of the patient being searched.
                test (str): The name of the test taken.
                result (str): The value of the test result.
                datetime (str): The date and time the test was taken.
        """

        if name in self.tests_taken:
            self.tests_taken[name].append([test, result, datetime])
        else:
            self.tests_taken[name] = [(test, result, datetime)]

    def select_patient_results_all_tests(self, name: str) -> List[List[str]]:
        """
            Description:
                Selects the patient and
                returns test results
            Args:
                name (str): The name of the patient

            Returns:
                All test results for the given patient
                Empty List if no tests for patient exist
        """
        tests = []
        if name in self.patient:
            tests = self.tests_taken[name]
        return tests

    def select_test(self, code: str) -> List[str]:
        """
            Description:
                Selects the tests and returns the test's information
            Args:
                code (str): The code of the code to be searched.
            Returns:
                test (list conatining Code code, name, description, price)
        """
        test = self.test_type.get(code)
        return test

    def retrieve_test_code(self):
        """
            Description
                Obtains all the Codes for the different test types (mostly used to check if test code exists)

            Returns:
                A list of all the test type codes
        """
        test_list = list(self.test_type.keys())
        return test_list

    def display_all_tests(self):
        """
            Description
                Obtains all the Codes for the different test types

            Returns:
                A list of all the test type codes and values
        """
        code = self.test_type.items()
        return code

    def insert_new_test(self, code: str, name: str, description: str, price: str):
        """
            Description:
                Inserts a new patient record into the system
            Args:
                code (str): The new patient being added to the system
                name (str): The patients date of birth
                description (str): The new patient's address
                price (str): The new patient's postcode
        """
        self.test_type[code] = [name, description, price]

    def remove_test(self, code: str):
        """
            Desription:
                Removes specific test the system
            Args:
                code (str): The test that is to be deleted
        """
        if code in self.retrieve_test_code():
            del self.test_type[code]

    def data_import(self):
        # ###################################### #
        # ###### Populate Test Type Data ####### #
        # ###################################### #
        # ###### Name, Description, Price ###### #
        # ###################################### #
        self.test_type['FBC'] = [
            "Full Blood Count",
            "Provides information about the numbers and correct development of cells in the blood",
            25
        ]

        self.test_type['LFT'] = [
            "Liver Function Test",
            "Measures the enzymes, proteins and substances that are produced or excrete by the liver",
            32
        ]

        self.test_type['FeS'] = [
            "Iron Studies",
            "Measures the amount of iron in the blood",
            14
        ]

        self.test_type['TSH'] = [
            "Thyroid Stimulating Hormone",
            "Performed to screen, diagnose and monitor treatment of thyroid disorders",
            44
        ]

        self.test_type['UT'] = [
            "Urinalysis",
            "Performed on a sample of urine to look for some metabolic disorders and kidney disorders",
            28
        ]

        self.test_type['INR'] = [
            "International Normalised Ratio",
            "Performed to check how well clot-preventing medication is working",
            18
        ]
        self.test_type['PCR'] = [
            "Covid-19 Polymerase Chain Reaction Test",
            "Performed on a patient's nose swab to determine if the patient has Covid-19",
            150
        ]
        self.test_type['RAT'] = [
            "Covid-19 Rapid Antigen Test",
            "Performed on a patient's nose swab to determine if the patient has Covid-19",
            15
        ]

        # ############################################ #
        # ########## Populate Patient Data ########### #
        # ############# Student No, DOB, ############# #
        # #### Address, Postcode,  height, weight #### #
        # ############################################ #
        self.patient['Michael'] = [991192, '2008-06-14', '47 Nowhere Avenue, Voidville, QLD', '4378', 132, 58]
        self.patient['Gary'] = [998912, '2006-11-02', '938 Long Road, Largetown, QLD', '4928', 181, 87]
        self.patient['Bradley'] = [993284, '2004-02-24', '3 Short Street, Littleton, QLD', '4552', 179, 67]
        self.patient['Larry'] = [991231, '2009-08-30', '56 Oldie Avenue, Retrovale, QLD', '4981', 155, 108]
        self.patient['Barry'] = [995724, '2005-10-07', '82 Newbie Street, Newtown, QLD', '4710', 168, 58]
        self.patient['Brad'] = [999375, '2005-03-28', '15 Lonely Lane, Remote Waters, QLD', '4523', 194, 84]

        # ########################################## #
        # ####### Populate Tests Taken Data ######## #
        # ########################################## #
        # ####### [[ Test, Date, Result ], ] ####### #
        # ########################################## #
        self.tests_taken['Harry'] = [
            ['LFT', '2021-10-07', 'High'],
            ['FeS', '2021-12-29', 'Low'],
            ['FBC', '2021-01-14', 'Normal']
        ]
        self.tests_taken['Gary'] = [
            ['TSH', '2021-09-16', 'Low'],
        ]

        self.tests_taken['Bradley'] = [
            ['UT', '2021-06-11', 'Normal'],
            ['TSH', '2022-01-29', 'Low'],
            ['RAT' '2022-02-01', 'Negative']
        ]

        self.tests_taken['Larry'] = [
            ['FeS', '2021-10-07', 'High'],
            ['FeS', '2021-11-07', 'Normal'],
            ['INR', '2021-11-07', 'Normal']
        ]

        self.tests_taken['Barry'] = [
            ['LFT', '2021-02-28', 'Normal'],
        ]

        self.tests_taken['Brad'] = [
            ['TSH', '2021-06-11', 'High'],
            ['TSH', '2021-07-11', 'High'],
            ['UT', '2021-07-11', 'Low'],
            ['FeS', '2021-07-11', 'Normal'],
            ['UT', '2021-08-14', 'High']
        ]
