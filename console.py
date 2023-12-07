#!/usr/bin/python3
"""That is my console module"""
import sys
# sys.path.append('/home/fares_me/ALX/AirBnB_clone/models/')
import cmd
from models.base_model import BaseModel
from models.review import Review
from models.amentiy import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    myClasses = ['BaseModel', 'Review', 'Amentiy',
                'City', 'Place', 'User', 'State']
    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                myDic = storage.all()
                myClassList = []
                myClassName = ''
                for key, value in myDic.items():
                    myClassList = key.split('.')
                    myClassName = myClassList[0]
                    if myClassName in HBNBCommand.myClasses and myClassName == arg:
                        print(value)
                    else:
                        if arg != myClassName:
                            pass
                        else:
                            print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class
        name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            instance = storage.all()[key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except NameError:
            print("** class doesn't exist **")

    def emptyline(self):
        """A method to exit the cmd with a new line"""
        pass

    def do_EOF(self, line):
        """A method to exit the cmd with a new line"""
        print()
        return True

    def help_EOF(self):
        """The help for eof"""
        print("Used to exit the cmd")

    def do_quit(self, line):
        """Guess what it does!"""
        return True
    
    def help_create(self):
        """The help for create command"""
        print("Create command to create a new instance of a class")
        
    def help_show(self):
        """The help for show command"""
        print("Show command to print the string representation of an instance")

    def help_destroy(self):
        """The help for destroy command"""
        print("Destroy command to delete an instance based on the class name and id")
        
    def help_all(self):
        """The help for all command"""
        print("All command to print all string representation of all instances")

    def help_update(self):
        """The help for update command"""
        print("Update command to update an instance based on the class name and id")
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()