#!/usr/bin/python3
""" this file represent the console.py """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ console that is hbnb """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """the console to be exit"""
        return True

    def emptyline(self):
        """ the emptyline method to be overwritten """
        return False

    def do_quit(self, arg):
        """to exit the program by the quit command"""
        return True

    def _key_value_parser(self, args):
        """a list of string to be created in a dictionary"""
        n_d = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                mofta = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                n_d[mofta] = value
        return n_d

    def do_create(self, arg):
        """a new instance of a class to be created"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            n_d = self._key_value_parser(args[1:])
            moment = classes[args[0]](**n_d)
        else:
            print("** class doesn't exist **")
            return False
        print(moment.id)
        moment.save()

    def do_show(self, arg):
        """based on the class and id an instance to be printed"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                moftah = args[0] + "." + args[1]
                if moftah in models.storage.all():
                    print(models.storage.all()[moftah])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """based on class and if an instance to be deleted"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                moftah = args[0] + "." + args[1]
                if moftah in models.storage.all():
                    models.storage.all().pop(moftah)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """string representation of an instance to be printed"""
        args = shlex.split(arg)
        list_obj = []
        if len(args) == 0:
            dictionay_o = models.storage.all()
        elif args[0] in classes:
            dictionay_o = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for moftah in dictionay_o:
            list_obj.append(str(dictionay_o[moftah]))
        print("[", end="")
        print(", ".join(list_obj), end="")
        print("]")

    def do_update(self, arg):
        """based on the class name, id,attribute and value to be updated"""
        args = shlex.split(arg)
        arkam = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                c = args[0] + "." + args[1]
                if c in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in arkam:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[c], args[2], args[3])
                            models.storage.all()[c].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
