#!/usr/bin/python3
"""Crates the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Cretes the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the interpreter"""
        return True

    def emptyline(self):
        """Does nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def help_quit(self):
        print("quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
