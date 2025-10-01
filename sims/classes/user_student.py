"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: classes/user_student.py
Description: Extends the User class to define UserStudent, containing functionalities specific to a student's role.
"""

import random
import re
from .user import User
from config import *
from file_readwrite import read_from_file, write_to_file


class UserStudent(User):
    def __init__(self, user_id=User.default_user_id, user_name=User.default_user_name,
                 user_password=User.default_user_password, user_role='ST',
                 user_status=User.default_user_status, enrolled_units=None):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        """
        Initialize a UserStudent object with user details and enrolled units.

        Args:
            user_id (int): Unique identifier for the user.
            user_name (str): Unique username, consisting of numbers, letters, and underscores.
            user_password (str): Encrypted password for the user.
            user_role (str): Role of the user, set to 'ST' for student.
            user_status (str): Status of the user, either 'enabled' or 'disabled'.
            enrolled_units (list of tuples): List of enrolled units and their scores.
        """
        self.enrolled_units = enrolled_units if enrolled_units is not None else []

    def __str__(self):
        """
        Return a string representation of the student's attributes.

        Returns:
            str: Formatted string including user ID, name, password, role, status, and enrolled units.
        """
        user_str = User.__str__(self)
        student_str = user_str + f",{self.enrolled_units}"
        return student_str

    def student_menu(self):
        """
        Display and handle the student-specific operations menu.
        Allows students to manage their enrolled units and check scores.
        """
        while True:
            print("\nStudent Menu:")
            print("1. List available units")
            print("2. List enrolled units")
            print("3. Enroll in a unit")
            print("4. Drop a unit")
            print("5. Check scores")
            print("6. Generate score for a unit")
            print("7. Log out")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.list_available_units()
            elif choice == '2':
                self.list_enrolled_units()
            elif choice == '3':
                unit_code = input("Enter unit code to enroll: ").strip()
                if unit_code:
                    self.enrol_unit(unit_code)
                else:
                    print("No unit code entered. Please try again.")
            elif choice == '4':
                unit_code = input("Enter unit code to drop: ").strip()
                if unit_code:
                    self.drop_unit(unit_code)
                else:
                    print("No unit code entered. Please try again.")
            elif choice == '5':
                unit_code = input("Enter unit code to check score (leave empty for all units): ").strip()
                self.check_score(unit_code if unit_code else None)
            elif choice == '6':
                unit_code = input("Enter unit code to generate score: ").strip()
                if unit_code:
                    self.generate_score(unit_code)
                else:
                    print("No unit code entered. Please try again.")
            elif choice == '7':
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def list_available_units(self):
        """
        Display all units available for the student to enroll.
        Lists units not currently enrolled by the student.
        """
        all_units = read_from_file(unit_file_path)
        enrolled_unit_codes = [unit[0] for unit in self.enrolled_units]

        # Create a dictionary to hold unit capacities
        unit_capacities = {}
        for unit in all_units:
            unit_id, unit_code, unit_name, capacity = unit.strip().split(',')
            unit_capacities[unit_code] = int(capacity)
        print('unit capacities: ', unit_capacities)

        # Count current enrollments for each unit
        current_enrollments = {code: 0 for code in unit_capacities.keys()}
        users = read_from_file(user_file_path)
        for user in users:
            user_data = user.strip().split(',', 4)
            if user_data[3] == 'ST':
                enrolled_units = user_data[4].split(',', 1)[1]
                for unit in eval(enrolled_units):
                    unit_code = unit[0]
                    if unit_code in current_enrollments.keys():
                        current_enrollments[unit_code] += 1
        print('current enrollments: ', current_enrollments)

        # Determine available units based on enrollment and capacity
        available_units = []
        for unit in all_units:
            unit_id, unit_code, unit_name, capacity = unit.strip().split(',')
            if unit_code not in enrolled_unit_codes and current_enrollments[unit_code] < unit_capacities[unit_code]:
                capacity = int(unit_capacities[unit_code] - current_enrollments[unit_code])
                unit = [unit_code, unit_name, capacity]
                available_units.append(unit)

        if available_units:
            print("Available units:")
            print("unit_code, unit_name, student capacity left")
            for unit in available_units:
                print(unit)
        else:
            print("No available units to enroll.")

    def list_enrolled_units(self):
        """
        Display all units that the student is currently enrolled in.
        Lists each unit along with the student's enrollment status.
        """
        if not self.enrolled_units:
            print("You are not currently enrolled in any units.")
            return

        print("Enrolled units:")
        for unit_code, score in self.enrolled_units:
            unit_details = self.get_unit_details(unit_code)
            if unit_details:
                unit_name = unit_details[1]  # Extracting unit name
                print(f"Unit Code: {unit_code}, Unit Name: {unit_name}, Score: {score}")
            else:
                print(f"Unit Code: {unit_code}, Details Not Found")

    def get_unit_details(self, unit_code):
        """
        Fetch details of a unit based on its code.

        Args:
            unit_code (str): The code of the unit to find details for.

        Returns:
            str: A string containing details of the unit, or None if not found.
        """
        all_units = read_from_file(unit_file_path)
        for units in all_units:
            unit = units.split(',')
            if unit[1] == unit_code:
                return units.strip()
        return None

    def enrol_unit(self, unit_code):
        """
        Enroll the student into a specified unit.

        Args:
            unit_code (str): The code of the unit to enroll in.

        Note:
            The student can enroll in a maximum of 3 units.
        """
        if len(self.enrolled_units) >= 3:
            print('Student has reached the maximum number of enrolled units.')
            return

        all_units = read_from_file(unit_file_path)
        unit_exists = any(unit_code in unit.split(',')[1] for unit in all_units)
        enrolled_unit_codes = [unit[0] for unit in self.enrolled_units]

        if unit_code in enrolled_unit_codes:
            print(f"Student is has already enrolled with unit {unit_code} .")
            return
        
        if not re.match(r"^ITI\d{4}$", unit_code):
            print(f"Invalid unit code format: {unit_code}. Expected format: 'ITI' followed by 4 digits.")
            return

        if not unit_exists:
            print(f"Unit with code {unit_code} does not exist.")
            return

        # Check if the unit has available capacity
        if not self.is_unit_available(unit_code):
            print(f"No available capacity in unit {unit_code}.")
            return

        # Enrolling in the unit
        self.enrolled_units.append((unit_code, -1))
        self.update_user_data()
        print(f"Enrolled in unit: {unit_code}")

    def is_unit_available(self, unit_code):
        """
        Check if a unit has available capacity for enrollment.

        Args:
            unit_code (str): The code of the unit to check.

        Returns:
            bool: True if the unit has available capacity, False otherwise.
        """
        all_units = read_from_file(unit_file_path)
        enrolled_unit_codes = [unit[0] for unit in self.enrolled_units]
        code = unit_code

        # Create a dictionary to hold unit capacities
        unit_capacities = {}
        for unit in all_units:
            unit_id, unit_code, unit_name, capacity = unit.strip().split(',')
            unit_capacities[unit_code] = int(capacity)

        # Count current enrollments for each unit
        current_enrollments = {code: 0 for code in unit_capacities.keys()}
        users = read_from_file(user_file_path)
        for user in users:
            user_data = user.strip().split(',', 4)
            if user_data[3] == 'ST':
                enrolled_units = user_data[4].split(',', 1)[1]
                for unit in eval(enrolled_units):
                    unit_code = unit[0]
                    if unit_code in current_enrollments.keys():
                        current_enrollments[unit_code] += 1

        # Find the capacity of the specified unit
        available_units = []
        unit_capacity = None
        for unit in all_units:
            unit_id, unit_code, unit_name, capacity = unit.strip().split(',')
            if unit_code not in enrolled_unit_codes and current_enrollments[unit_code] < unit_capacities[unit_code]:
                capacity = int(unit_capacities[unit_code] - current_enrollments[unit_code])
                unit = [unit_code, unit_name, capacity]
                available_units.append(unit)

        for unit in available_units:
            if code == unit[0]:
                unit_capacity = unit[2]

        if not unit_capacity:
            return False
        else:
            return True

    def update_user_data(self):
        """
        Update the user's data in the user.txt file.
        """
        users = read_from_file(user_file_path)
        updated_users = []
        for i, line in enumerate(users):
            user_data = line.strip().split(',', 4)
            if user_data[0] == str(self.user_id):
                users[i] = self.__str__() + '\n'
        updated_users.extend(users)
        write_to_file(user_file_path, updated_users)

    def drop_unit(self, unit_code):
        """
        Remove a specified unit from the student's enrolled units list.

        Args:
            unit_code (str): The code of the unit to be dropped.
        """
        # Validate if the unit_code is not empty and is in the correct format
        if not unit_code or not unit_code.strip():
            print("No unit code entered. Please provide a valid unit code.")
            return

        # Regex to validate the unit_code format (e.g., 'ITI9136')
        if not re.match(r"^ITI\d{4}$", unit_code.strip()):
            print(f"Invalid format for unit code: {unit_code}. Expected format: 'ITI' followed by 4 digits.")
            return

        # Validate if the unit_code corresponds to an existing unit
        all_units = read_from_file(unit_file_path)
        if unit_code not in [unit.split(',')[1] for unit in all_units]:
            print(f"Invalid unit code: {unit_code}. No such unit found.")
            return

        # Check if the student is currently enrolled in the unit
        if any(unit[0] == unit_code for unit in self.enrolled_units):
            self.enrolled_units = [unit for unit in self.enrolled_units if unit[0] != unit_code]
            self.update_user_data()
            print(f"Unit {unit_code} has been dropped.")

        else:
            print(f"You are not enrolled in unit {unit_code}. Cannot drop a unit you are not enrolled in.")

    def check_score(self, unit_code):
        """
        Display the score for a specified unit or for all enrolled units.

        Args:
            unit_code (str): The code of the unit to check the score for.
            If empty, scores for all enrolled units are displayed.
        """
        # Input validation for unit_code
        if unit_code is not None and not isinstance(unit_code, str):
            print("Invalid input: unit_code must be a string.")
            return

        if unit_code and not unit_code.strip():
            print("Invalid input: unit_code cannot be empty or just spaces.")
            return

        if unit_code:
            # Check for a specific unit
            for unit in self.enrolled_units:
                if unit_code == unit[0]:
                    print(f"Score for unit {unit_code}: {unit[1]}")
                    return
                else:
                    print(f"You are not enrolled in unit {unit_code}.")
        else:
            # Display scores for all enrolled units
            if not self.enrolled_units:
                print("You are not currently enrolled in any units.")
            else:
                print("Scores for all enrolled units:")
                for unit_code, score in self.enrolled_units:
                    print(f"Unit {unit_code}: Score {score}")

    def generate_score(self, unit_code):
        """
        Generate and update a random score for a specified unit.

        Args:
            unit_code (str): The code of the unit for which to generate a score.
        """
        # Validate unit_code format (e.g., 'ITI9136') with regex
        if not re.match(r"^ITI\d{4}$", unit_code):
            print(f"Invalid unit code format: {unit_code}. Expected format: 'ITI' followed by 4 digits.")
            return

        # Check if the student is enrolled in the specified unit
        enrolled_unit = next((unit for unit in self.enrolled_units if unit[0] == unit_code), None)

        all_units = read_from_file(unit_file_path)
        if unit_code not in [unit[0] for unit in self.enrolled_units]:
            print('enrolled units: ',[unit[0] for unit in self.enrolled_units])
            print(
                f"You are not enrolled in unit {unit_code}. Cannot generate score for a unit you are not enrolled in.")
            return
        
        # Generate a random score and update the enrolled unit
        new_score = random.randint(0, 100)
        self.enrolled_units[self.enrolled_units.index(enrolled_unit)] = (unit_code, new_score)
        print(f"Generated score {new_score} for unit {unit_code}.")

        # Update the student's data in user.txt
        self.update_user_data()

    @classmethod
    def from_user(cls, user):
        return cls(user_id=user.user_id, user_name=user.user_name,
                   user_password=user.user_password, user_role=user.user_role,
                   user_status=user.user_status)
