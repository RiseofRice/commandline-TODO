from sys import argv
from hashids import Hashids
import random
import os


def generate_ids():
    hashids = Hashids(salt="this is my salt")
    generated_id = hashids.encode(random.randint(1, 256))
    return generated_id


def filehandler():
    files = os.listdir()
    if "todo.txt" in files:
        return "todo.txt"
    else:
        foo = open("todo.txt", "w")
        foo.close()
        return foo


def filewriter(gid, name, value=""):
    file = filehandler()
    with open(file, "a+") as file:
        if value == "":
            formated_string_to_write = f"{gid} || Name: {name}\n"
            file.write(formated_string_to_write)
        else:
            formated_string_to_write = f"{gid} || Name: {name} || Description: {value}\n"
            file.write(formated_string_to_write)


def new_todo(name, value=""):
    # print(generate_ids(), name, value)
    gid = generate_ids()
    filewriter(gid, name, value)

def del_todo(gid):
    # print(gid)
    file = filehandler()
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for line in lines:
            # print(line.split(" ")[0])
            if line.split(" ")[0] != gid:
                file.write(line)

def mark_as_done(gid):
    file = "todo.txt"
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for line in lines:
            if line.startswith(gid) == True:
                file.write(str(line).replace("\n", "") + " || DONE!" + "\n")
            else:
                file.write(line)



def view_todos(max="x"):
    with open("todo.txt", "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            print(line)



