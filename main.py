import os 
import sys
from time import sleep
import importlib
from datetime import date
from termcolor import colored as c

def loading():
    for i in range(0, 101):
        sleep(0.02)
        sys.stdout.write("\rbooting system... " + str(i) + "%")
        sys.stdout.flush()

    print("\nboot succes!")

loading()
print(c("Welcome to OrbitOS beta! type 'help' to see a list of available commands!", "yellow"))
print("Today's date:", date.today())
print(c("security patch: 1 march 2024", "red"))

def runCommand(command, args):
    command = importlib.import_module("commands."+command)
    command.cmd(args)

while True:
    enter = input("root@orbitos:~$>> ")

    cmd = enter.split(" ")[0]
    args = enter.split(" ")[1:]

    runCommand(cmd, args)