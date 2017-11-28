# -*- coding:gbk-*-
import cmd
from gensim.models import Word2Vec
import os
import sys

class CLI(cmd.Cmd):
    def __init__(self,model):
        cmd.Cmd.__init__(self)
        self.prompt = "> "  # define command prompt
        self.model = model

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
            print(model.most_similar([args]))

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("syntax: quit -- terminatesthe application")

    do_q = do_quit


if __name__ == "__main__":
    model = Word2Vec.load('w2v_model')
    cli = CLI(model)
    cli.cmdloop()