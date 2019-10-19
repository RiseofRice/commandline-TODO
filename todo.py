import os
from sys import argv
import main


def startup():
    # print(len(argv))
    if len(argv) > 1:
        if argv[1] == "-n":
            print(argv)
            name = str(input("Name of the Todo: \n"))
            value = str(input("Description of your todo: \n"))
            main.new_todo(name,value)

        elif argv[1] == "--new":
            name = argv[2]
            value = argv[3]
            print(argv)
            main.new_todo(name, value)

        elif argv[1] in ["-d", "--delete", "--del"]:
            if len(argv) > 2:
                gid = argv[2]
                main.del_line(gid)

        elif argv[1] in ["-l", "--list", "-ls"]:
            main.view_todos()


if __name__ == '__main__':
    startup()