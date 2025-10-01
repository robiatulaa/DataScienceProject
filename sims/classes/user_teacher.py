"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: classes/user_teacher.py
Description: Extends the User class to define UserTeacher, containing functionalities specific to a teacher's role.
"""

import re
import matplotlib.pyplot as plt
from .user import User
from .unit import Unit
from config import *
from file_readwrite import *


class UserTeacher(User):
    """
    Represents a teacher with specific functionalities related to teaching units.

    Inherits from the User class and adds methods specific to a teacher,
    such as managing teaching units and interacting with student information.
    """

    def __init__(self, user_id=User.default_user_id, user_name=User.default_user_name,
                 user_password=User.default_user_password, user_role='TA',
                 user_status=User.default_user_status, teach_units=None):
        """
        Initialize a UserTeacher instance with specific attributes.
        
        Args:
            user_id (int): Unique identifier for the user.
            user_name (str): Username for the teacher account. 
            user_password (str): Password for the teacher account. Will be encrypted. 
            user_role (str): Role of the user, set to 'TA' for teacher.
            user_status (str): Status of the user, either 'enabled' or 'disabled'. 
            teach_units (list): List of unit codes taught by the teacher. 
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.teach_units = teach_units if teach_units is not None else []

    def __str__(self):
        """
        Return the teacher information as a formatted string.

        Returns:
            str: Formatted string representing the teacher's information.
        """
        user_str = User.__str__(self)
        teacher_str = user_str + f",{self.teach_units}"
        return teacher_str

    def teacher_menu(self):
        """
        Display and handle the teacher menu options.

        Provides a list of operations specific to a teacher, including managing teaching units,
        viewing student enrollments, and handling unit scores.
        """
        while True:
            print('''
            Teacher Menu:
            1. List teaching units
            2. Add a teaching unit
            3. Delete a teaching unit
            4. List enrolled students in a unit
            5. Show unit's average, maximum, and minimum score
            6. Plot student scores for a unit
            7. Log out
            ''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.list_teach_units()
            elif choice == '2':
                unit_obj = self.get_unit_details()
                self.add_teach_unit(unit_obj)
            elif choice == '3':
                unit_code = input("Enter the unit code to delete: ")
                self.delete_teach_unit(unit_code)
            elif choice == '4':
                unit_code = input("Enter the unit code to list students: ")
                self.list_enrol_students(unit_code)
            elif choice == '5':
                unit_code = input("Enter the unit code for score details: ")
                self.show_unit_avg_max_min_score(unit_code)
            elif choice == '6':
                unit_code = input("Enter the unit code to plot scores: ")
                self.plot_student_unit_score(unit_code)
            elif choice == '7':
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_unit_details(self):
        """
        Prompt the teacher to enter details for a new unit and create a Unit object.

        Returns:
            Unit: A new Unit object created based on the input details.
        """
        print("Enter the details for the new unit:")

        # Create a new unit object, validate each user input
        while True:
            try:
                unit_code = input("Unit Code (Please start the unit code with 'ITI' followed by 4 digits) : ")
                if not re.match(r"^ITI\d{4}$", unit_code):
                    raise ValueError("Unit code must be in the format 'ITI' followed by four digits.")

                unit_name = input("Unit Name: ")
                if not all(name.isalnum() or name.isspace() for name in unit_name):
                    raise ValueError("Unit Name must contain only letters or numbers.")

                unit_capacity = input("Unit Capacity: ")
                if not unit_capacity.isdigit():
                    raise ValueError("Invalid Unit Capacity. It must be a numeric value.")

                return Unit(unit_code=unit_code, unit_name=unit_name, unit_capacity=int(unit_capacity))
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.")

        return Unit(unit_code=unit_code, unit_name=unit_name, unit_capacity=int(unit_capacity))

    def list_teach_units(self):
        """
        Display the information of all units taught by the current teacher.
        """
        if not self.teach_units:
            print("No units are currently assigned to the current teacher.")
            return

        units_data = read_from_file(unit_file_path)
        found_units = []

        # check each teach unit to the unit.txt file
        for unit_code in self.teach_units:
            if not unit_code.isalnum():
                print(f"Invalid unit code format: {unit_code}")
                continue
            pattern = re.compile(rf'{re.escape(unit_code)},.*$',
                                 re.MULTILINE)  # Using regex library to search a pattern
            # pattern starts with each unit_code
            for line in units_data:
                match = pattern.search(line)  # match the pattern to each line in the units file
                if match:
                    found_units.append(match.group())

        if found_units:
            print("Units taught by the teacher:")
            for unit in found_units:
                print(unit)
        else:
            print("No matching units found in the system for the assigned teaching units.")

    def add_teach_unit(self, unit_obj):
        """
        Add a new unit's information to unit_file_path and update the teacher's 'teach_units' list.
        The unit name and capacity are input by the teacher.
        """

        # Creating a new Unit object with a generated unit ID and unit code
        new_unit = unit_obj

        # Update unit_file_path file
        units = read_from_file(unit_file_path)
        # for unit in units:
        #     print('unit: ', unit)
        if any(new_unit.unit_code in unit for unit in units):
            print(f"Unit with code {new_unit.unit_code} already exists.")
            return

        units.append(new_unit.__str__())
        write_to_file(unit_file_path, units)

        # Update the teacher's 'teach_units' list and reflect this in user_file_path
        if new_unit.unit_code not in self.teach_units:
            self.teach_units.append(new_unit.unit_code)
            users = read_from_file(user_file_path)
            for i, line in enumerate(users):
                user_data = line.strip().split(',')
                if user_data[0] == str(self.user_id):
                    users[i] = self.__str__() + '\n'
                    break
            write_to_file(user_file_path, users)
            print(f"Unit {new_unit.unit_code} added successfully and assigned to teacher.")
        else:
            print(f"Unit {new_unit.unit_code} is already being taught by other teacher.")

    def delete_teach_unit(self, unit_code):
        """
        Delete a unit from the list of units taught by the teacher and update relevant records.

        Args:
            unit_code (str): The code of the unit to be removed.
        """

        # Validate the input unit_code
        if not all(code.isalnum() or code.isspace() for code in unit_code):
            print("Invalid unit code. It must be alphanumeric.")
            return

        if unit_code not in self.teach_units:
            print(f"{unit_code} is not in the teacher's teach list.")
            return

        self.teach_units.remove(unit_code)

        # Remove unit from 'user.txt' (both teacher's list and student enrollments)
        users = read_from_file(user_file_path)
        updated_users = self.update_users_file(users, unit_code)
        write_to_file(user_file_path, updated_users)

        # Remove unit from 'unit.txt'
        units = read_from_file(unit_file_path)
        for i, line in enumerate(units):
            updated_units = []
            unit_data = line.strip().split(',')
            if unit_data[1] == str(unit_code):
                units.pop(i)
        updated_units.extend(units)
        updated_units = [line for line in units if not line[1].startswith(unit_code)]
        write_to_file(unit_file_path, updated_units)
        print(f"Unit {unit_code} has been successfully removed from the teacher's list and student enrollments.")

    def update_users_file(self, users, unit_code):
        for i, line in enumerate(users):
            updated_users = []
            user_data = line.strip().split(',', 4)
            if user_data[0] == str(self.user_id):
                users[i] = self.__str__() + '\n'
            elif user_data[3] == 'ST':
                enrolled_units = user_data[4].split(',', 1)[1]
                user_status = user_data[4].split(',', 1)[0]
                units = [unit for unit in eval(enrolled_units) if not unit[0].startswith(
                    unit_code)]  # Remove student's unit if the delete unit function is called
                users[i] = ','.join(
                    user_data[:4] + [user_status, str(units)])  # Replace the line with the updated student user data
        updated_users.extend(users)
        return updated_users

    def list_enrol_students(self, unit_code):
        """
        Display the information of all students currently enrolled in a specific unit.

        Args:
            unit_code (str): The code of the unit for which to list enrolled students.
        """
        # Validate the input unit_code
        if not unit_code.isalnum():
            print("Invalid unit code. It must be alphanumeric.")
            return

        students_enrolled = []
        users = read_from_file(user_file_path)
        all_units = read_from_file(unit_file_path)
        unit_exists = [unit.split(',')[1] for unit in all_units]

        for i, line in enumerate(users):
            user_data = line.strip().split(',', 4)

            # if the user_role is student, split the last element by 1 comma to get their enrolled units
            if user_data[3] == 'ST':
                enrolled_units = user_data[4].split(',', 1)[1]
                if unit_code in enrolled_units:
                    students_enrolled.append(user_data[1])  # Assuming username is at index 1
                    
        if unit_code not in unit_exists:
            print('existing unit:', unit_exists)
            print(f"Unit code {unit_code} doesn't exist in the system")
        
        if students_enrolled:
            print(f"Students enrolled in {unit_code}:")
            for student in students_enrolled:
                print(student)
        else:
            print(f"No students are found enrolled in the unit {unit_code} within the system.")

    def show_unit_avg_max_min_score(self, unit_code):
        """
        Display the average, maximum, and minimum scores for a specific unit.

        Args:
            unit_code (str): The code of the unit to calculate scores for.
        """

        # Validate the input unit_code
        if not unit_code.isalnum():
            print("Invalid unit code. It must be alphanumeric.")
            return

        users = read_from_file(user_file_path)
        scores = []

        # Collect scores associated with the unit_code from every unit's enrolled students
        for line in users:
            user_data = line.strip().split(',', 4)
            if user_data[3] == 'ST':
                enrolled_units = user_data[4].split(',', 1)[1]
                for unit in eval(enrolled_units):
                    if unit[0].startswith(unit_code):
                        score = str(unit[1])
                        if score.isdigit():
                            scores.append(int(score))
        if scores:  # create the average, max, and min score from the chosen unit_code
            average_score = sum(scores) / len(scores)
            max_score = max(scores)
            min_score = min(scores)
            print(f"Unit {unit_code} - Average: {average_score}, Max: {max_score}, Min: {min_score}")
        else:
            print(f"No scores found for unit {unit_code}.")

    def plot_student_unit_score(self, unit_code):
        """
        Create and save a bar chart showing the distribution of student scores for a specific unit.

        Args:
            unit_code (str): The code of the unit to plot scores for.
        """

        # Validate the input unit_code
        if not unit_code.isalnum():
            print("Invalid unit code. It must be alphanumeric.")
            return

        scores = []
        student_ids = []
        users = read_from_file(user_file_path)

        # Collect scores associated with the unit_code
        for line in users:
            user_data = line.strip().split(',', 4)
            if user_data[3].strip() == 'ST':
                # Extract the part containing enrolled units
                enrolled_units_str = user_data[4].strip().split(',', 1)[1]

                # Manually parse the enrolled units string
                enrolled_units_str = enrolled_units_str.strip("[]")
                enrolled_units = [tuple(unit.strip("()").split(',')) for unit in enrolled_units_str.split('), (')]

                for unit in enrolled_units:
                    if unit[0].strip("'\"") == unit_code and int(
                            unit[1].strip()) != -1:  # Check for the unit code and valid scores
                        scores.append(int(unit[1].strip()))
                        student_ids.append(user_data[1].strip())

                        # print(f"Debug: scores for {unit_code} = {scores}")  # Debug print

        if not scores:
            print(f"No scores found for unit {unit_code}.")
            return
        else:
            # Plotting the scores with student IDs as x-ticks
            plt.figure(figsize=(10, 6))
            bars = plt.bar(range(len(scores)), scores, color='blue')
            plt.xlabel('Students')
            plt.ylabel('Scores')
            plt.title(f'Score Distribution for {unit_code}')
            plt.xticks(range(len(scores)), student_ids, rotation=45)  # Rotate labels if they overlap

            # Adding the score labels on top of the bars
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom')

            # Save the plot as an image file
            plt.savefig(f'score_charts/{unit_code}_scores.png')
            print(f"Bar chart for unit {unit_code} saved as '{unit_code}_scores.png' in 'score_charts' folder.")

            # Display the plot
            plt.show()

            plt.close()

    @classmethod
    def from_user(cls, user):
        return cls(user_id=user.user_id, user_name=user.user_name,
                   user_password=user.user_password, user_role=user.user_role,
                   user_status=user.user_status)
