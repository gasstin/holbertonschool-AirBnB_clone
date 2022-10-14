#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place

from models import storage


dict_class = {'BaseModel': BaseModel, 'User': User,
              'City': City, 'State': State, 'Review': Review,
              'Amenity': Amenity, 'Place': Place}


class HBNBCommand(cmd.Cmd):
    """
        Cmd class
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, *arg):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, *arg):
        """
            EOF command to exit the program
        """
        return True

    def do_create(self, line):
        """
            Creates a new instance, saves it (to the JSON file)
            and prints the id. Example: (hbnb) create User
        """
        arguments = line.split()  # split the input line in a list
        if len(arguments) < 1:
            print("** class name missing **")
        else:
            try:
                if arguments[0] in dict_class:
                    c = dict_class[arguments[0]]()
                c.save()  # saves it (to the JSON file)
                print(c.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
            Prints the string representation of an instance based on
            the class name and id. Example: (hbnb) BaseModel 12t4-5e7n-91l11
        """
        arguments = line.split()
        n = len(arguments)  # numbers of arguments
        if n == 0:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif arguments[0] not in dict_class:
            print("** class doesn't exist **")
        elif n == 2:
            if f"{arguments[0]}.{arguments[1]}" in storage.all().keys():
                # if the key is in storage
                print(storage.all()[f"{arguments[0]}.{arguments[1]}"])
            else:
                # if not in
                print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and
            id (save the change into the JSON file).
            Example: (hbnb) destroy BaseModel 12t4-5e7n-91l11
        """
        arguments = line.split()
        n = len(arguments)  # numbers of arguments
        if n == 0:
            print("** class name missing **")
        if n >= 1:
            if arguments[0] not in dict_class:
                # check if the objects is in storage
                print("** class doesn't exist **")
                return False
            elif n < 2:
                print("** instance id missing **")
        if n >= 2:
            if f"{arguments[0]}.{arguments[1]}" in storage.all().keys():
                del storage.all()[f"{arguments[0]}.{arguments[1]}"]
                storage.save()  # save the changes
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
            Prints all string representation of all instances based or
            not on the class name. Example: (hbnb) all User or (hbnb) all
        """
        if not line:  # if not arguments
            list_obj = []
            for val in storage.all().values():
                list_obj += [f"{str(val)}"]
            print(f"{list_obj}")
        else:
            if line in dict_class:
                list_obj = []
                for key, val in storage.all().items():
                    if key[0:len(line)] == line:
                        # compares the arguments with the keys
                        list_obj += [f"{str(val)}"]
                print(f"{list_obj}")
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file).
            (hbnb) update BaseModel 124d4-1l2s34-12xx3a4 email "aibnb@mail.com"
        """
        arguments = arg.split()
        try:
            # try to set attributes
            setattr(storage.all()[f"{arguments[0]}.{arguments[1]}"],
                    arguments[2], arguments[3][1:len(arguments[3]) - 1])
            storage.save()  # saves it (to the JSON file)
        except Exception:
            # Manage the possibles error casses
            if len(arguments) < 1:
                print("** class name missing **")
            if len(arguments) >= 1:
                if arguments[0] not in dict_class:
                    print("** class doesn't exist **")
                    return False
                elif arguments[0] in dict_class and len(arguments) == 1:
                    print("** instance id missing **")
                    return False
            if len(arguments) >= 2:
                if f"{arguments[0]}.{arguments[1]}" not in\
                        storage.all().keys():
                    # check if the objects is in storage
                    print("** no instance found **")
                    return False
                elif (f"{arguments[0]}.{arguments[1]}" in
                        storage.all().keys()) and len(arguments) == 2:
                    print("** attribute name missing **")
                    return False
            if len(arguments) == 3:
                print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
