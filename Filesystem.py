#
# protonOS 1.6's Filesystem but ported to OrbitOS
# Port by Proton0 (the creator of protonOS)
#

import __main__
import shutil
import os

def cd(command):
    if command[0] == "cd":
        if not len(command) == 2:
            print("not enough args")
            return
        if command[1] == "..":
            # Go back a directory
            if __main__.fs["full_directory"] == "filesystem":
                __main__.fs["current_directory"] = "/"
                __main__.fs["full_directory"] = "/"
            else:
                current_directory_parts = __main__.fs["full_directory"].split("/")
                parent_directory_parts = current_directory_parts[:-1]
                parent_directory = "/".join(parent_directory_parts)
                parent_directory_name = parent_directory_parts[-1]
                if parent_directory_name == "filesystem":
                    __main__.fs["current_directory"] = "/"
                else:
                    __main__.fs["current_directory"] = parent_directory_name
                if parent_directory == "/" or parent_directory == "":
                    __main__.fs["full_directory"] = "filesystem"
                else:
                    __main__.fs["full_directory"] = parent_directory
            return
        __main__.fs["current_directory"] = command[1]
        __main__.fs["full_directory"] = __main__.fs[
                                                                   "full_directory"] + "/" + command[1]


def ls(command):
    if command[0] == "ls":

        if len(command) == 2:
            k = os.listdir("filesystem/" + command[1])
            for f in k:
                print(f)
            return
        if __main__.fs["current_directory"] == "/":
            k = os.listdir("filesystem")
            for f in k:
                print(f)
            return
        else:
            k = os.listdir(__main__.fs["full_directory"])
            for f in k:
                print(f)
            return


def cat(command):
    if command[0] == "cat":
        if len(command) == 2:
            f = open(__main__.fs["full_directory"] + "/" + command[1], "r")
            for line in f.readlines():
                print(line)


def rm(command):
    if command[0] == "rm":
        if len(command) == 3:
            if command[1] == "-rf":
                if command[2] == "/":
                    k = input("Are you sure you want to delete the entire filesystem (y/n) : ")
                    if k.lower() == "y" or k.lower() == "yes":
                        print("Deleting filesystem")
                        shutil.rmtree("filesystem")
                        print("Critical error")
                        exit()
                    else:
                        print("Cancelled")
        if len(command) == 2:
            if os.path.isfile(__main__.fs["full_directory"] + "/" + command[1]):
                os.remove(__main__.fs["full_directory"] + "/" + command[1])
            else:
                shutil.rmtree(__main__.fs["full_directory"] + "/" + command[1])


def rmdir(command):
    if command[0] == "rmdir":
        rm(["rm", command[1]])


def pwd(command):
    if command[0] == "pwd":
        print(__main__.fs['full_directory'])


def mkdir(command):
    if command[0] == "mkdir":
        if len(command) == 2:
                os.mkdir(__main__.fs["full_directory"] + "/" + command[1])