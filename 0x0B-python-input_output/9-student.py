#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return (self.__dict__)
