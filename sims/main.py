"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: main.py
Description: Main application entry point including login.
Initializes the application and provides the main menu for user interaction.
"""

import os
import random
from classes.unit import Unit
from classes.user import User
from classes.user_admin import UserAdmin
from classes.user_student import UserStudent
from classes.user_teacher import UserTeacher
from file_readwrite import *
from config import *


def initialize_directory():
    """
    Create the data and score_charts directory if it doesn't exist.
    """
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('score_charts'):
        os.makedirs('score_charts')


def main_menu():
    """
    Display the main menu of the program and handle user choices.
    """
    monash_logo = """
                                                                                
                                                                                
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                @@@ #    , # ,.    & @@@@@@@@@#  %@*@@@ @/@@@@@@@               
                @@@ #&#    #    *& & @@@@@@@@,/.@@@.@@@@@ @ @@@@@               
                @@@ #@@*   #   .%@ & @@@@@@@,@.@@@@.@@@@@@./@@@@@               
                @@@ #%@&. ,#  ./@% & @@@@@@@.*,@@@@.@@@@@@@@ @@@@               
                @@@ #      #       @ @@@@@@@@ @&@@    .@@.,,@@@@@               
                @@@                  @@@@@@@@@@  /@* @@@ .@@@@@@@               
                @@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@               
                @@@@@@@@@@@@@@@@@@@          *@@@@@@@@@@@@@@@@@@@               
                @@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@               
                @@@@@@@@@@@@@/          @          @@@@@@@@@@@@@@               
                @@@@@@@@@@&          @@@@@@(          @@@@@@@@@@*               
                .@@@@@@@          &@@@@@@@@@@@           @@@@@@@                
                 @@@@          /@@@@@@    *@@@@@@          *@@@/                
           *@     @         .@@@@@@@@@#   @@@@@@@@@@         .@    #@           
         @,  @@(@  @      @@@@@@@@@@@@@@@@@@@@@ @@@@@@&      @  @@&&  @@        
       @   @@    @  @  @@@@@@@,, *(@@@@@@@@@@@    @@@@@@@/ .@  @    @/  @*      
        @ .@      @  @@@@@@@@#    ,@@@@@@@@ @@@@@@@@@@@@@@@% ,@     %@ &(       
         @ @@.(&/@ @. *@@@@@@@@@@@@@@@@@@@ .(@@@@@@@@@@@@@  @*.@/  @*%@*        
          @@,*@      @  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, ,@  @(@ @ @@          
           .@. @ ( @ ..@  @@@@@@@@@@@@/@ @.@@@@@@@@@@@.  @ @@   &% &@           
                 @    /  @   @@@@@@@@/     @@@@@@@@@  &@    % .@                
                   @ #     &@   @@@@@@@@ @@@@@@@&  .@,  #@@ *@                  
                     @/  & .  #@,  .@@@@@@@@&   %@  @ #   @&                    
                       ,@.    @.* (@&      .@@.  @   % @@                       
                           @@  @   &@   *  %@  * @  @@                          
                              .@@  #*  .@   .. ,@@                              
                                   .@@&  *@@#                                   
                                                                                

    """
    while True:
        print(monash_logo)
        print("\nWelcome to the Student Information Management System")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            if choice == '1':
                user = attempt_login()
                if user:
                    go_to_role_menu(user)
                else:
                    print("Login failed. Please check your username and password or contact admin.")
            elif choice == '2':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Please enter a valid option (1 or 2).")

# def masked_input(prompt="Password: "):
#     """
#     Simulates masked password by displaying asterisks (*) for each character
#     Does not offer real security
#     But at least the password is not visible by the real character
#     Args:
#         prompt (str): The prompt displayed to the user. Defaults to "Password: ".
#
#     Returns:
#         str: The password entered by the user, as a single string.
#     """
#     print(prompt, end='', flush=True)
#
#     entered_password = []
#     while True:
#         char = input()
#         if char == '\n':
#             break
#         else:
#             entered_password.append(char)
#             print("*", end='', flush=True)
#
#     return ''.join(entered_password)


def attempt_login():
    """
    Attempt to authenticate a user and return the user object if successful.
    """
    user_name = input("Username: ")
    user_password = input("Password: ")
    user = login(user_name, user_password)
    return user


def go_to_role_menu(user):
    """
    Go to the specific menu based on the user's role.
    """
    if user.user_role == 'AD':
        user.admin_menu()
    elif user.user_role == 'ST':
        user.student_menu()
    elif user.user_role == 'TA':
        user.teacher_menu()
    else:
        print("Unrecognized user role.")


def login(user_name, user_password):
    """
    Authenticate the user by matching the username and encrypted password.

    Args:
        user_name (str): The input username.
        user_password (str): The input (non-encrypted) password.

    Returns:
        User object if authentication is successful, None otherwise.
    """
    return User.login(user_name, user_password)


def generate_admin_user():
    """
    Generate a default admin user.

    Returns:
        UserAdmin: An instance of UserAdmin representing the default admin user.
    """
    return UserAdmin(user_id=User.generate_user_id(),
                     user_name="admin",
                     user_password="password",
                     user_role="AD",
                     user_status="enabled")


def generate_teachers_and_units():
    """
    Generate teacher and unit test data.
    """
    teachers = []
    units = []

    for i in range(1, 4):  # Assuming we need three teachers and three units
        unit_id = Unit.generate_unit_id()
        unit_code = f"ITI{random.randint(1000, 9999)}"  # Generate a random unit code
        unit_name = f"Unit {i}"
        unit_capacity = 30  # Assuming each unit has a capacity of 30

        # Print the generated unit ID for debugging purposes
        print(f"Generated unit ID: {unit_id}, Type: {type(unit_id)}")

        # Create a new Unit object
        unit = Unit(unit_id=unit_id, unit_code=unit_code, unit_name=unit_name, unit_capacity=unit_capacity)
        units.append(unit)

        # Generate teacher data
        teacher_user = UserTeacher(user_id=User.generate_user_id(),
                                   user_name=f"teacher{i}",
                                   user_password="password",
                                   user_role="TA",
                                   user_status="enabled",
                                   teach_units=[unit_code])
        teachers.append(teacher_user)

    return teachers, units


def generate_students(units):
    """
    Generate a list of student users.

    Each student is assigned to all the provided units with a default score of -1, indicating not graded.

    Args:
        units (list): A list of Unit objects to which students will be enrolled.

    Returns:
        list: A list of UserStudent instances representing the generated student users.
    """
    students = []
    for i in range(1, 11):
        student = UserStudent(user_id=User.generate_user_id(),
                              user_name=f"student{i}",
                              user_password="password",
                              user_role="ST",
                              user_status="enabled",
                              enrolled_units=[(unit.unit_code, -1) for unit in units])
        students.append(student)

    return students


def generate_test_data():
    """
    Generate test data for the program.

    This includes creating default users, units, and assigning them appropriately.
    """

    initialize_directory()
    admin_user = generate_admin_user()
    teachers, units = generate_teachers_and_units()
    students = generate_students(units)

    # Write user data
    user_data = [str(admin_user)] + [str(teacher) for teacher in teachers] + [str(student) for student in students]
    write_to_file(user_file_path, user_data)

    # Write unit data
    unit_data = [str(unit) for unit in units]
    write_to_file(unit_file_path, unit_data)

    print("Test data generated successfully.")


def main():
    """
    Main function to initiate the program.

    It generates test data and shows the main menu.
    """
    # try:
    #     generate_test_data()
    #     main_menu()
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    # generate_test_data()
    main_menu()


if __name__ == "__main__":
    main()
