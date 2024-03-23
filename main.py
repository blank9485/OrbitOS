import os 
import sys
import time
import commands
from termcolor import colored
from datetime import date
from Filesystem import FileSystem  # Import the FileSystem class instead of importing a whole file 
from commands import CommandProcessor # import the CommandProcessor class instead of importing a whole file ( again )
# moved all imports to the top to reflect the PEP-8 standards

# Load File System commands as fs
fs = FileSystem()
cp = CommandProcessor()


def loading():
    for i in range(0, 101):
        time.sleep(0.0099)
        sys.stdout.write("\rbooting system... " + str(i) + "%")
        sys.stdout.flush()
    print("\nboot success!")

# moved the system commands class UP, so we can make sure the list and the commands are initilaized BEFORE the "OS" "booted"
# System Commands
system_commands = [
    fs.cd,        # Change to fs.cd instead of Filesystem.cd
    fs.mkdir,     # Change to fs.mkdir instead of Filesystem.mkdir
    fs.rm,        # Change to fs.rm instead of Filesystem.rm
    fs.ls,        # Change to fs.ls instead of Filesystem.ls
    fs.cat,       # Change to fs.cat instead of Filesystem.cat
    fs.rmdir,     # Change to fs.rmdir instead of Filesystem.rmdir
    fs.pwd,       # Change to fs.pwd instead of Filesystem.pwd
                  # to reflect the class change made

    cp.faq,
    cp.ipg,
    cp.echo,
    cp.help,
    cp.bored,
    cp.clear,
    cp.Neofetch,
    cp.stop,
    cp.rservice,
    cp.shutdown,
    cp.software_update,
    cp.weather,
    cp.whoami
]             # same shit done like above   





loading()

c = colored
print(c("Welcome to OrbitOS beta! type 'help' to see a list of available commands!", "yellow"))

today = date.today()
print("Today's date:", today)
c = colored
print(c("security patch: 1 march 2024", "red"))
while True:
    user_input = input(f"root@orbitos:{fs.current_directory}$>> ").split(" ")
    for command in system_commands:
        try:
            command(user_input)
        except Exception as e:
            print(f"Error while executing the command : {e}")
