"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: classes/user_admin.py
Description: Extends the User class to define UserAdmin, containing functionalities specific to an administrator's role.
"""

from .user import User
from classes.user_student import UserStudent
from classes.user_teacher import UserTeacher
from config import *
from file_readwrite import *


class UserAdmin(User):
    """
    Represents an administrator with administrative functionalities.

    Inherits from the User class and provides additional methods 
    specific to administrative tasks such as managing users and units.
    """

    def __init__(self, user_id=User.default_user_id, user_name=User.default_user_name,
                 user_password=User.default_user_password, user_role='AD',
                 user_status=User.default_user_status):
        """
        Initialize a UserAdmin instance with specified attributes.
        
        Args:
            user_id (int): Unique identifier for the user. Defaults to -1.
            user_name (str): Username for the admin account. Defaults to 'new_admin'.
            user_password (str): Password for the admin account. Will be encrypted. Defaults to 'password'.
            user_role (str): Role of the user, set to 'AD' for admin. Defaults to 'AD'.
            user_status (str): Status of the user, either 'enabled' or 'disabled'. Defaults to 'disabled'.
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        """
        Return the admin information as a formatted string.

        Returns:
            str: Formatted string representing the admin's information.
        """
        return f"{self.user_id},{self.user_name},{self.user_password},{self.user_role},{self.user_status}"

    def admin_menu(self):
        """
        Display and handle the admin menu options.
        
        Continuously displays the admin menu and prompts for a selection 
        until the admin chooses to log out.
        """
        while True:
            print('''
            Admin Menu:
            1. Search user information
            2. List all users information
            3. List all units information
            4. Enable/Disable user
            5. Add user
            6. Delete user      
            7. Log out
            ''')
            admin_selection = input("Enter your selection: ")

            if admin_selection == '1':
                user_name = input("Enter username to search: ")
                self.search_user(user_name)
            elif admin_selection == '2':
                self.list_all_users()
            elif admin_selection == '3':
                self.list_all_units()
            elif admin_selection == '4':
                user_name = input("Enter username to enable/disable: ")
                self.enable_disable_user(user_name)
            elif admin_selection == '5':
                user_obj = input("Username: ")
                self.add_user(user_obj)
            elif admin_selection == '6':
                user_name = input("Enter username to delete: ")
                self.delete_user(user_name)
            elif admin_selection == '7':
                print("Logging out.")
                break
            else:
                print("Invalid selection. Please try again.")

    def search_user(self, user_name):
        """
        Search for and display information of a specific user.

        Args:
            user_name (str): The username to search for in the system.
        """
        users = read_from_file(user_file_path)
        found = False
        for user in users:
            if user_name.lower() + "," in user.lower():
                user_split = user.strip().split(",", 5)
                user_join = ", ".join(user_split)
                print(f"User found: {user_join}")
                found = True
                break
        if not found:
            print(f"User '{user_name}' not found.")
        # For testing
        return True

    def list_all_users(self):
        """
        Display a list of all users currently stored in the system.
        """
        users = read_from_file(user_file_path)
        print("List of all users:")
        for user in users:
            user_split = user.strip().split(",", 5)
            user_join = ", ".join(user_split)
            print(user_join)
        # For testing
        return True

    def list_all_units(self):
        """
        Display a list of all units currently stored in the system.
        """
        units = read_from_file(unit_file_path)
        print("List of all units:")
        for unit in units:
            print(unit.strip())
        # For testing
        return True

    def enable_disable_user(self, user_name):
        """
        Enable or disable a user's account based on their current status.

        Args:
            user_name (str): The username of the account to be enabled or disabled.
        """
        users = read_from_file(user_file_path)
        updated_users = []
        user_found = False
        for user in users:
            if "," + user_name + "," in user:
                user_data = user.strip().split(',')
                user_data[4] = 'enabled' if user_data[4] == 'disabled' else 'disabled'
                updated_user = ','.join(user_data)
                updated_users.append(updated_user)
                user_found = True
            else:
                updated_users.append(user.strip())
        if user_found:
            write_to_file(user_file_path, updated_users)
            print(f"User '{user_name}' status updated.")
        else:
            print(f"User '{user_name}' not found.")
        # For testing
        return True

    def add_user(self, user_obj):
        """
        Add a new user to the system.
        
        Args:
            user_obj (User): An instance of User, UserTeacher, or UserStudent to be added.
        """
        users = read_from_file(user_file_path)
        print(f"Enter details for {user_obj}: ")

        # Input user detail
        new_user_password = input("Password: ")
        new_user_role = input("Role (TA/ST): ")
        new_user_status = input("Status (enabled/disabled): ")

        # Validate the value
        for user in users:
            user_data = user.strip().split(',')
            for user_name in user_data:
                if user_obj.lower() in user_name.lower() and len(user_obj) == len(user_name):
                    print("Username already exist!")
                    return
        if new_user_role.lower() not in ["ta", "st"]:
            print("The user role must be TA (Teacher) / ST (Student).")
            return
        if new_user_status.lower() not in ["enabled", "disabled"]:
            print("The user status must be enabled or disabled.")
            return

        if new_user_role.lower() == 'ta':
            new_user = UserTeacher(None, user_obj.lower(), new_user_password, new_user_role.upper(),
                                   new_user_status.lower(), None)
        if new_user_role.lower() == 'st':
            new_user = UserStudent(None, user_obj.lower(), new_user_password, new_user_role.upper(),
                                   new_user_status.lower(), None)

        users.append(str(new_user))
        write_to_file(user_file_path, users)
        print(f"User '{user_obj}' added successfully.")
        # For testing
        return True

    def delete_user(self, user_name):
        """
        Delete a user from the system.

        Args:
            user_name (str): The username of the user to be deleted.
        """
        users = read_from_file(user_file_path)
        user_exists = any(user_name in user for user in users)

        if user_exists:
            # User exists, proceed with deletion
            updated_users = [user for user in users if "," + user_name + "," not in user]
            write_to_file(user_file_path, updated_users)
            print(f"User '{user_name}' deleted successfully.")
            return True  # Indicate successful deletion
        else:
            # User does not exist
            print(f"User '{user_name}' not found.")
            return False  # Indicate unsuccessful deletion

    @classmethod
    def from_user(cls, user):
        return cls(user_id=user.user_id, user_name=user.user_name,
                   user_password=user.user_password, user_role=user.user_role,
                   user_status=user.user_status)
