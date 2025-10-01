"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: classes/user.py
Description: Defines the base User class, which is extended by specific user types
Such as students, teachers, and administrators.
"""


import random
from config import *
from file_readwrite import *


class User:
    # Encryption character pools
    str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    str_2 = "!#$%&()*+-./:;<=>?@\\^_`{|}~"
    password_prefix = "^^^"
    password_suffix = "$$$"

    # Default values for constructor arguments
    default_user_id = -1
    default_user_name = "new_user"
    default_user_password = "password"
    default_user_role = "undefined"
    default_user_status = "disabled"

    def __init__(self, user_id=None, user_name=None, user_password=None, user_role=None, user_status=None):
        # if user_id is None:
        #     self.user_id = self.generate_user_id()
        # else:
        #     self.user_id = User.default_user_id
        self.user_id = user_id if user_id is not None else self.generate_user_id()
        self.user_name = user_name if user_name is not None else self.default_user_name
        self.user_password = self.encrypt(user_password) if user_password is not None else self.encrypt(
            self.default_user_password)
        self.user_role = user_role if user_role is not None else self.default_user_role
        self.user_status = user_status if user_status is not None else self.default_user_status

    def __str__(self):
        return f"{self.user_id},{self.user_name},{self.user_password},{self.user_role},{self.user_status}"

    @staticmethod
    def generate_user_id():
        # Method implementation to generate a unique 5 digits user ID
        return random.randint(10000, 99999)

    @staticmethod
    def check_username_exist(user_name):
        """
        Check if a username already exists in the user file.

        Args:
            user_name (str): The username to check.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        users = read_from_file(user_file_path)
        if not users:  # If users list is empty, either file not found or error occurred
            return False

        for user_line in users:
            existing_name = user_line.split(',')[1].strip()
            if user_name == existing_name:
                return True
        return False

    @staticmethod
    def check_user_id_exist(user_id):
        """
        Check if a user ID already exists in the user file.

        Args:
            user_id (int): The user ID to check.

        Returns:
            bool: True if the user ID exists, False otherwise.
        """
        users = read_from_file(user_file_path)
        if not users:  # If users list is empty, either file not found or error occurred
            return False

        for user_line in users:
            existing_id = user_line.strip().split(',')[0].strip()
            if existing_id.isdigit() and int(existing_id) == user_id:
                return True
        return False

    @classmethod
    def encrypt(self, user_password):
        """
        Encrypts the given password using a custom encryption algorithm.

        Args:
            user_password (str): The password to be encrypted.

        Returns:
            str: The encrypted password.

        Raises:
            ValueError: If the password is not a string or is empty.
        """
        # Validate the password
        if not isinstance(user_password, str):
            raise ValueError("Password must be a string.")
        if user_password == "":
            raise ValueError("Password cannot be empty.")

        # Encrypt the password
        encrypted_password = self.password_prefix
        for i, char in enumerate(user_password):
            index_str1 = ord(char) % len(self.str_1)
            encrypted_char1 = self.str_1[index_str1]
            index_str2 = i % len(self.str_2)
            encrypted_char2 = self.str_2[index_str2]
            encrypted_password += encrypted_char1 + encrypted_char2
        encrypted_password += self.password_suffix

        return encrypted_password

    @staticmethod
    def login(user_name, user_password):
        """
        Authenticate a user based on username and password.

        Args:
            user_name (str): The username of the user trying to log in.
            user_password (str): The password of the user trying to log in.

        Returns:
            User object if authenticated, None otherwise.
        """
        if not isinstance(user_name, str) or not isinstance(user_password, str):
            print("Invalid input: Username and password must be strings.")
            return None

        if not user_name.strip() or not user_password.strip():
            print("Invalid input: Username and password cannot be empty.")
            return None

        encrypted_password = User.encrypt(user_password)  # Call encrypt as a static method

        users = read_from_file(user_file_path)
        user_obj = None

        for user_line in users:
            user_data = user_line.strip().split(',', 4)
            if len(user_data) == 5:
                user_id, stored_user_name, stored_encrypted_password, user_role, user_status = user_data

                # Check for role and create a user object
                if stored_user_name == user_name and encrypted_password == stored_encrypted_password:
                    if user_status.startswith('disabled'):
                        print('User is disabled, please contact admin to enable it')
                        return
                    
                    if user_role == 'AD':
                        from classes.user_admin import UserAdmin
                        print('logged in as admin')
                        return UserAdmin(user_id=int(user_id), user_name=stored_user_name,
                                         user_password=user_password, user_role=user_role,
                                         user_status=user_status)
                    elif user_role == 'TA':
                        teacher = user_status.split(',', 1)
                        user_status = teacher[0]
                        teach_units = eval(teacher[1])
                        print('logged in as teacher')
                        from classes.user_teacher import UserTeacher
                        return UserTeacher(user_id=int(user_id), user_name=stored_user_name,
                                           user_password=user_password, user_role=user_role,
                                           user_status=user_status, teach_units=teach_units)
                    elif user_role == 'ST':
                        student = user_status.split(',', 1)
                        user_status = student[0]
                        enrolled_units = eval(student[1])
                        print('logged in as student')
                        from classes.user_student import UserStudent
                        return UserStudent(user_id=int(user_id), user_name=stored_user_name,
                                           user_password=user_password, user_role=user_role,
                                           user_status=user_status, enrolled_units=enrolled_units)
                    break
            else:
                print("Unexpected data format in user file.")
                return user_obj
        else:
            print("Username or password does not match.")
            return user_obj
