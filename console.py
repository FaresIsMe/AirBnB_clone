#!/usr/bin/python3
"""That is my console module"""
import sys
sys.path.append('/home/fares_me/ALX/AirBnB_clone/models/')
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple hbnb commmand interpreter example."""
    prompt = '(hbnb) '
    def do_EOF(self, line):
        """A method to exit the cmd with a new line"""
        print()
        return True

    def help_EOF(self):
        """The help for eof"""
        print("Used to exit the cmd")

    def do_quit(self, line):
        """A method to exit the cmd witout a new line"""
        return True

    def help_quit(self):
        """The help for quit command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Making emptyline command do nothing"""
        pass
    
    def do_create(self, line):
        """Creates a new class instnace"""
        args = line.split()
        if line is None:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            
        def do_show(self, line):
            """Prints the string representation of an 
            instance based on the class name and id """
            args = line.split()
            if not args:
                print("** class name missing **")
                return
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + '.' + instance_id
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            except IndexError:
                if args[0] in storage.classes():
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
                    
            def destroy(self, line):
                """Deletes an instance based on the class name and id"""
                args = line.split()
            if not args:
                print("** class name missing **")
                return
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + '.' + instance_id
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if args[0] in storage.classes():
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    storage.reload()