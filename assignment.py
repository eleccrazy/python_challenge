"""
File: assignment.py
Desc: This module contains the python script to represent the employee in a given
      dataset. It also contains two functions that compute the missed minute from
      the given check_in and check_out time and date information.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 6 2022
"""
from datetime import datetime as d
from datetime import timedelta


def calculate_missed_time2(check_in, check_out):
    """
    This function computes the missed minutes from the work-time.
    """
    # Allowed work-time from monday to friday in standard timedelta format.
    mtof = timedelta(hours=9, minutes=0, seconds=0)
    # Allowed work-time on saturday in standard timedelta format.
    saturday = timedelta(hours=4, minutes=0, seconds=0)

    # The check_in time must not be greater than the check_out time.
    # if the in time is greater than the out time a ValueError exception is raised.
    if check_in > check_out:
        raise ValueError("Please Give appropriate values for check_in and check_out time.")

    # The following statement computes the actual work-time of an employee in a standard timedelta format.
    # We require this format so that we can be able to subtract and get the missed time result.
    st = check_out - check_in

    # Sunday is day-off,  no computation.
    if check_in.strftime('%A') == 'Sunday':
        return
    # On saturday, the work time is only 4 hours
    elif check_in.strftime('%A') == 'Saturday':
        # if the actual work time is greater than the allowed time set by the company
        # then, the program should have to return 0 as missed time.
        if st > saturday:
            return 0
        return int((saturday - st).total_seconds() / 60)
    # From monday to friday the work time is 9 hours
    else:
        if st > mtof:
            return 0
        return int((mtof - st).total_seconds() / 60)


class Employee:
    """
    This class represents an Employee with the given three attributes as
    employee ID number, check-in time and date, and check_out time and date.
    """
    # Constructor to initialize all the attributes.
    def __init__(self, emp_id=0, check_in=None, check_out=None):
        """
        This function instantantiates those attributes.
        """
        self.emp_id = emp_id
        self.check_in = check_in
        self.check_out = check_out

    @property
    def emp_id(self):  # Getter method for emp_id
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, id_info):  # Setter method for emp_id
        if type(id_info) != int:
            raise TypeError("The ID should must be an integer.")
        if id_info < 0:
            raise ValueError("The ID must be greater than 0.")
        self.__emp_id = id_info

    @property
    def check_in(self):  # Getter method for check_in
        return self.__check_in

    @check_in.setter
    def check_in(self, info):  # Setter method for check_in
        if type(info) != d:
            raise TypeError("The check_in time and date must be in the standard timedate format.")
        self.__check_in = info

    @property
    def check_out(self):  # Getter method for check_out
        return self.__check_out

    @check_out.setter
    def check_out(self, info):  # Setter method for check_out
        if type(info) != d:
            raise TypeError("The check_out time and date must be in the standard timedate format.")
        self.__check_out = info

    def calculate_missed_time(self):
        """
        This function computes the missed time from the standard work time.
        """
        # Allowed work-time from monday to friday in standard timedelta format.
        mtof = timedelta(hours=9, minutes=0, seconds=0)
        # Allowed work-time on saturday in standard timedelta format.
        saturday = timedelta(hours=4, minutes=0, seconds=0)

        # The check_in time must not be greater than the check_out time.
        # if the in time is greater than the out time a ValueError exception is raised.
        if self.__check_in > self.__check_out:
            raise ValueError("Please Give appropriate values for check_in and check_out time.")
        # The following statement computes the actual work-time of an employee in a standard timedelta format.
        # We require this format so that we can be able to subtract and get the missed time result.
        st = self.__check_out - self.__check_in

        # Sunday is day-off,  no computation.
        if self.__check_in.strftime('%A') == 'Sunday':
            return
        # On saturday, the work time is only 4 hours
        elif self.check_in.strftime('%A') == 'Saturday':
            # if the actual work time is greater than the allowed time set by the company
            # then, the program should have to return 0 as missed time.
            if st > saturday:
                return 0
            return int((saturday - st).total_seconds() / 60)
        # From monday to friday the work time is 9 hours
        else:
            if st > mtof:
                return 0
            return int((mtof - st).total_seconds() / 60)


# Creating five objects for Employee class with the given dataset.

emp1 = Employee(10, d(2022, 8, 5, 4, 0, 0), d(2022, 8, 5, 11, 30, 0))
emp2 = Employee(20, d(2022, 8, 5, 2, 30, 0), d(2022, 8, 5, 10, 30, 0))
emp3 = Employee(30, d(2022, 8, 5, 3, 15, 0), d(2022, 8, 5, 11, 30, 0))
emp4 = Employee(40, d(2022, 8, 6, 2, 30, 0), d(2022, 8, 6, 8, 30, 0))
emp5 = Employee(50, d(2022, 8, 7, 3, 15, 0), d(2022, 8, 7, 6, 30, 0))

# An array representation of the Employee with the given dataset.

employee_array_list = [emp1, emp2, emp3, emp4, emp5]

print("\nComputation using the outside function\n")

for emp in employee_array_list:
    missed = calculate_missed_time2(emp.check_in, emp.check_out)

    if missed is None:
        print("It is sunday, Enjoy your time!")
    else:
        print("Employee {} worked from {} to {}".format(emp.emp_id, emp.check_in, emp.check_out))
        print("Employee {} missed {} minutes from work time.\n".format(emp.emp_id, missed))

print("\nComputation using the public function of the class Employee\n")

for emp in employee_array_list:
    missed = emp.calculate_missed_time()

    if missed is None:
        print("It is sunday, Enjoy your time!")
    else:
        print("Employee {} worked from {} to {}".format(emp.emp_id, emp.check_in, emp.check_out))
        print("Employee {} missed {} minutes from work time.\n".format(emp.emp_id, missed))
