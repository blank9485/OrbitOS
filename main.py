import os 
import sys
import time

import commands

# Load FS
fs = {
    "current_directory": "/",
    "full_directory": "filesystem"
}
if not os.path.exists("filesystem"):
    os.mkdir("filesystem")
import Filesystem
def loading():
    for i in range(0, 100):
        time.sleep(0.1) 
        sys.stdout.write("\rbooting system... " + str(i) + "%")
        sys.stdout.flush()
    print("\nboot succes!")

loading()

# System Commands
system_commands = [
    Filesystem.cd,
    Filesystem.mkdir,
    Filesystem.rm,
    Filesystem.ls,
    Filesystem.cat,
    Filesystem.rmdir,
    Filesystem.pwd,
    commands.faq,
    commands.ipg,
    commands.echo,
    commands.help,
    commands.bored,
    commands.clear,
    commands.Neofetch,
    commands.shutdown,
    commands.software_update,
    commands.weather,
    commands.whoami
]

from termcolor import colored
from datetime import date
c = colored
print(c("Welcome to OrbitOS beta! type 'help' to see a list of available commands!", "yellow"))

today = date.today()
print("Today's date:", today)
c = colored
print(c("security patch: 1 march 2024", "red"))
while True:
    user_input = input(f"root@orbitos:{fs['current_directory']}$>> ").split(" ")
    for command in system_commands:
        try:
            command(user_input)
        except Exception as e:
            print(f"Error while executing the command : {e}")
