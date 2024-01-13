#!/usr/bin/python3
"""the HBnB"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def myPerse(arg):
    curBrace = re.search(r"\{(.*?)\}", arg)
    brack = re.search(r"\[(.*?)\]", arg)
    if curBrace is None:
        if brack is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brack.span()[0]])
            rL = [i.strip(",") for i in lex]
            rL.append(brack.group())
            return rL
    else:
        lex = split(arg[:curBrace.span()[0]])
        rL = [i.strip(",") for i in lex]
        rL.append(curBrace.group())
        return rL


class HBNBCommand(cmd.Cmd):
    """It defines the HolbertonBnb cmd interpreter.
    Attributes:
        prompt (str): cmd prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """It only receives an empty line."""
        pass

    def default(self, arg):
        """Default behavior cmd for invalid input."""
        argDict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        exact = re.search(r"\.", arg)
        if exact is not None:
            argL = [arg[:exact.span()[0]], arg[exact.span()[1]:]]
            exact = re.search(r"\((.*?)\)", argL[1])
            if exact is not None:
                comd = [argL[1][:exact.span()[0]], exact.group()[1:-1]]
                if comd[0] in argDict.keys():
                    calling = "{} {}".format(argL[0], comd[1])
                    return argDict[comd[0]](calling)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Use: create <class>
        Create a new class instance and print its id.
        """
        argL = myPerse(arg)
        if len(argL) == 0:
            print("** class name missing **")
        elif argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argL[0])().id)
            storage.save()

    def do_show(self, arg):
        """Use: show <class> <id> or <class>.show(<id>)
        Shows the representation of a class instance of an id given.
        """
        argL = myPerse(arg)
        objDict = storage.all()
        if len(argL) == 0:
            print("** class name missing **")
        elif argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argL[0], argL[1]) not in objDict:
            print("** no instance found **")
        else:
            print(objDict["{}.{}".format(argL[0], argL[1])])

    def do_destroy(self, arg):
        """Use: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of an id given.
        """
        argL = myPerse(arg)
        objDict = storage.all()
        if len(argL) == 0:
            print("** class name missing **")
        elif argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argL[0], argL[1]) not in objDict.keys():
            print("** no instance found **")
        else:
            del objDict["{}.{}".format(argL[0], argL[1])]
            storage.save()

    def do_all(self, arg):
        """Use: all <class> or all <class> or <class>.all()
        Shows the representation of a class instance of an id given.
        Or all classes if no class given"""
        argL = myPerse(arg)
        if len(argL) > 0 and argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objL = []
            for o in storage.all().values():
                if len(argL) > 0 and argL[0] == o.__class__.__name__:
                    objL.append(o.__str__())
                elif len(argL) == 0:
                    objL.append(o.__str__())
            print(objL)

    def do_count(self, arg):
        """Use: count <class> or <class>.count()
        Pritns the number of instances of the given class.
        """
        argL = myPerse(arg)
        if len(argL) == 0:
            print("** class name missing **")
        elif argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            c = 0
            for o in storage.all().values():
                if argL[0] == o.__class__.__name__:
                    c += 1
            print(c)

    def do_update(self, arg):
        """Use: update <class> <id> <attribute_name> <attribute_value>
        or <class>.update(<id>, <attribute_name>, <attribute_value>)
        or <class>.update(<id>, <dictionary>)
        Updates a class instance of an id given.
        """
        argL = myPerse(arg)
        objDict = storage.all()

        if len(argL) == 0:
            print("** class name missing **")
            return False
        if argL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argL) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argL[0], argL[1]) not in objDict.keys():
            print("** no instance found **")
            return False
        if len(argL) == 2:
            print("** attribute name missing **")
            return False
        if len(argL) == 3:
            try:
                type(eval(argL[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argL) == 4:
            o = objDict["{}.{}".format(argL[0], argL[1])]
            if argL[2] in o.__class__.__dict__.keys():
                valT = type(o.__class__.__dict__[argL[2]])
                o.__dict__[argL[2]] = valT(argL[3])
            else:
                o.__dict__[argL[2]] = argL[3]
        elif type(eval(argL[2])) == dict:
            o = objDict["{}.{}".format(argL[0], argL[1])]
            for k, v in eval(argL[2]).items():
                if (k in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[k]) in {str, int, float}):
                    valT = type(o.__class__.__dict__[k])
                    o.__dict__[k] = valT(v)
                else:
                    o.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
