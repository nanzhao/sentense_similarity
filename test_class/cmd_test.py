# -*- coding:gbk-*-
import cmd
import os
import sys
import class_lsh

class CLI(cmd.Cmd):
    def __init__(self,d2v):
        cmd.Cmd.__init__(self)
        self.prompt = "> "  # define command prompt
        self.d2v = d2v


    def do_help(self, args):
        if args == "exit":
            print("exit this program")
        elif args == "quit":
            print("quit this program")
        elif args == "shell":
            print("run a shell commad")
        elif args == "run":
            print("run a sub shell")
        else:
            print(args)
            model.predict(args)

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("syntax: quit -- terminatesthe application")

    do_q = do_quit


if __name__ == "__main__":
    model = class_lsh.Model("data")

    cli = CLI(model)
    cli.cmdloop()