#!/usr/bin/python3
"""That is my console module"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()