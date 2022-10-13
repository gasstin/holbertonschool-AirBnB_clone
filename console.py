#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""
import cmd, sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review

from models import storage


dict_class = {'BaseModel': BaseModel, 'User': User, 'City': City, 'State': State, 'Review': Review}
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, *arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, *arg):
        'EOF command to exit the program'
        return True

    def do_create(self, line):
        'Creates a new instance, saves it (to the JSON file) and prints the id. Example: (hbnb) create User'
        arguments = line.split()
        if len(arguments) < 1:
            print("** class name missing **")
        else:
            try:
                if arguments[0] in dict_class:
                    c = dict_class[arguments[0]]()
                c.save()
                print(c.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        'Prints the string representation of an instance based on the class name and id. Example: (hbnb) BaseModel 12t4-5e7n-91l11'
        arguments = line.split()
        n = len(arguments) # numbers of arguments
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
        'Deletes an instance based on the class name and id (save the change into the JSON file). Example: (hbnb) destroy BaseModel 12t4-5e7n-91l11'
        arguments = line.split()
        n = len(arguments) # numbers of arguments
        if n == 0:
            print("** class name missing **")
        elif n == 1:
            if arguments[0] not in dict_class:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if f"{arguments[0]}.{arguments[1]}" in storage.all().keys():
                del storage.all()[f"{arguments[0]}.{arguments[1]}"]
                storage.save() # save the changes
            else:
                print("** no instance found **")
                
    def do_all(self, line):
        'Prints all string representation of all instances based or not on the class name. Example: (hbnb) all User or (hbnb) all'
        if not line: #if not arguments
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
            
                    
                
            
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()