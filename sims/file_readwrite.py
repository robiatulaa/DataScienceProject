"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: file_readwrite.py
Description: Provides functions for reading from and writing to data files used by the application.

The purpose of file_readwrite.py
This module abstracts away the file I/O operations, providing a set of reusable functions
for reading from and writing to files.
This helps avoid code duplication and centralizes error handling related to file operations.

By using a dedicated module for file operations, you avoid repeating
the same code across different parts of the application
Centralized error handling.
Allowing for easier testing and potential replacement or extension of file handling functionality.

On PyCharm you can see how many method(s) that has been used, it shows many.
If you write this method or function everytime it will take times and hard to maintain.
So we use best practice and modular functionality.
"""


def read_from_file(file_path):
    """
    Read data from a given file and return it as a list of lines.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        list: A list of lines from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError:
        print(f"Error reading file: {file_path}")
        return []


def write_to_file(file_path, data):
    """
    Write data to a given file.

    Args:
        file_path (str): The path to the file to be written to.
        data (list): A list of lines to be written to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in data:
                file.write(line.strip() + "\n")
    except IOError:
        print(f"Error writing to file: {file_path}")
