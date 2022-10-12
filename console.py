#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""
import cmd, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_create(self, arg):
        if len(arg) < 1:
            print("** class name missing **")
        else:
            try:
                if (arg[1] == "BaseModel"):
                    b = BaseModel()
                b.save()
                print(b.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, *arg):
        print(arg)
        list_aux = list(*arg[:])
        for l in list_aux:
            print(l)
        if arg[1] is not BaseModel:
            print("** class doesn't exist **")
        if not arg[1]:
            print("** class name missing **")
        if not arg[2]:
            print("** instance id missing **")
        print(arg[1])

if __name__ == '__main__':
    HBNBCommand().cmdloop()