#
# protonOS 1.6's Filesystem but ported to OrbitOS
# Port by Proton0 (the creator of protonOS)
#
#
# Modified by Breado aka TheRammatraMain 

import __main__
import shutil
import os


# using classes to manage commands better, for greater scalabillity.
# and to make sure were not importing A WHOLE FILE, this will enable faster "boot" time, and greater control 
# over what is used when

class FileSystem:
    def __init__(self):
        self.current_directory = "/"
        self.full_directory = "filesystem"

    def cd(self, command):
        if command[0] == "cd":
            if not len(command) == 2:
                print("not enough args")
                return
            if command[1] == "..":
                # Go back a directory
                if self.full_directory == "filesystem":
                    self.current_directory = "/"
                    self.full_directory = "/"
                else:
                    current_directory_parts = self.full_directory.split("/")
                    parent_directory_parts = current_directory_parts[:-1]
                    parent_directory = "/".join(parent_directory_parts)
                    parent_directory_name = parent_directory_parts[-1]
                    if parent_directory_name == "filesystem":
                        self.current_directory = "/"
                    else:
                        self.current_directory = parent_directory_name
                    if parent_directory == "/" or parent_directory == "":
                        self.full_directory = "filesystem"
                    else:
                        self.full_directory = parent_directory
                return
            self.current_directory = command[1]
            self.full_directory = self.full_directory + "/" + command[1]

    def ls(self, command):
        if command[0] == "ls":
            if len(command) == 2:
                path = "filesystem/" + command[1]
            else:
                path = self.full_directory if self.current_directory != "/" else "filesystem"
            k = os.listdir(path)
            for f in k:
                print(f)

    def cat(self, command):
        if command[0] == "cat":
            if len(command) == 2:
                with open(self.full_directory + "/" + command[1], "r") as f:
                    for line in f.readlines():
                        print(line)

    def rm(self, command):
        if command[0] == "rm":
            if len(command) == 3:
                if command[1] == "-rf" and command[2] == "/":
                    k = input("Are you sure you want to delete the entire filesystem (y/n) : ")
                    if k.lower() == "y" or k.lower() == "yes":
                        print("Deleting filesystem")
                        shutil.rmtree("filesystem")
                        print("Critical error")
                        exit()
                    else:
                        print("Cancelled")
            if len(command) == 2:
                path = self.full_directory + "/" + command[1]
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)

    def rmdir(self, command):
        if command[0] == "rmdir":
            self.rm(["rm", command[1]])

    def pwd(self, command):
        if command[0] == "pwd":
            print(self.full_directory)

    def mkdir(self, command):
        if command[0] == "mkdir" and len(command) == 2:
            os.mkdir(self.full_directory + "/" + command[1])