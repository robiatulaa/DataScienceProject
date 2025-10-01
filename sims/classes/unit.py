"""
ITI9136 - Algorithms and Programming Foundations in Python
Assignment 3
Group 09

Group Members:
- Reza Maliki Akbar (34292020)
- Hugo Andrew Prathama (34022961)
- Robiatul Adawiyah Al-Qosh (34269193)

File: classes/unit.py
Description: Defines the Unit class with attributes and methods to represent and manage academic units.
"""

import random
import re


class Unit:
    """
    Represents an academic unit or course.

    Attributes:
        unit_id (int): Unique identifier for the unit.
        unit_code (str): Unique code for the unit.
        unit_name (str): Name of the unit.
        unit_capacity (int): Maximum enrollment capacity of the unit.
    """

    existing_unit_ids = set()  # Track existing unit IDs
    existing_unit_codes = set()  # Track existing unit codes

    def __init__(self, unit_id=None, unit_code=None, unit_name="Default Unit", unit_capacity=30):
        """
        Initialize a new Unit instance.

        Args:
            unit_id (int, optional): Unique integer ID for the unit. Defaults to a generated ID.
            unit_code (str, optional): Unique code for the unit. Must start with 'ITI' followed by four digits.
            unit_name (str, optional): Name of the unit. Defaults to 'Default Unit'.
            unit_capacity (int, optional): Maximum capacity of the unit. Defaults to 30.
        """
        if unit_id is not None and not isinstance(unit_id, int):
            raise ValueError("Unit ID must be an integer.")
        self.unit_id = unit_id if unit_id else self.generate_unit_id()

        if unit_code and not re.match(r"^ITI\d{4}$", unit_code):
            raise ValueError("Unit code must be in the format 'ITI' followed by four digits.")

        if unit_code in Unit.existing_unit_codes:
            raise ValueError(f"Unit code {unit_code} already exists.")

        if not isinstance(unit_capacity, int) or unit_capacity <= 0:
            raise ValueError("Unit capacity must be a positive integer.")

        self.unit_id = unit_id if unit_id else self.generate_unit_id()
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

        Unit.existing_unit_ids.add(self.unit_id)
        Unit.existing_unit_codes.add(self.unit_code)

    def __str__(self):
        """
        Return the unit information as a formatted string.

        Returns:
            str: Formatted string representing the unit.
        """
        return f"{self.unit_id},{self.unit_code},{self.unit_name},{self.unit_capacity}"

    @classmethod
    def generate_unit_id(cls):
        """
        Generate a unique 7-digit unit ID.

        Returns:
            int: A unique 7-digit unit ID.
        """
        while True:
            new_unit_id = ''.join(random.choices('0123456789', k=7))
            if new_unit_id not in cls.existing_unit_ids:
                cls.existing_unit_ids.add(new_unit_id)
                return int(new_unit_id)
