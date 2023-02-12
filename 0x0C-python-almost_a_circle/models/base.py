#!/usr/bin/python3
""" A class that defines Base """
import json
import csv


class Base:
    """Defines the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initailizes the Base class"""
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonf:
            if list_objs is None:
                jsonf.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jsonf.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if (json_string is None or json_string == []):
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if (dictionary and dictionary != {}):
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonf:
                list_dict = Base.from_json_string(jsonf.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvf, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csvf, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                            for d in list_dict]
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
