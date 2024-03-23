import os 
import sys
import time
import commands
from datetime import date
from termcolor import colored
from commands import CommandProcessor
from kernel import Kernel

# Instantiate the imported classes
cp = CommandProcessor()

def loading():
    for i in range(0, 101):
        time.sleep(0.0099)
        sys.stdout.write("\rbooting system... " + str(i) + "%")
        sys.stdout.flush()
    print("\nboot success!")

# System Commands
system_commands = [
    'cp.faq',
    'cp.ipg',
    'cp.help',
    'cp.bored',
    'cp.clear',
    'cp.Neofetch',
    'cp.rservice',
    'cp.shutdown',
    'cp.software_update',
    'cp.weather',
    'cp.whoami'
]

# Start the kernel
kernel = Kernel()

loading()

c = colored
print(c("Welcome to OrbitOS beta! type 'help' to see a list of available commands!", "yellow"))

today = date.today()
print("Today's date:", today)
c = colored
print(c("security patch: 1 march 2024", "red"))
while True:
    user_input = input(f"root@orbitos:{os.curdir}/$>> ").split(" ")
    entered_command = user_input[0]  # Extract the entered command
    args = user_input[1:]  # Extract the arguments
    
    command_found = False
    
    for command_str in system_commands:
        command_name = command_str.split('.')[-1]  # Extract the command name from the string
        if command_name == entered_command:
            try:
                command_func = eval(command_str)  # Evaluate the string to get the function reference
                command_func(*args)  # Call the command function with arguments
                command_found = True
                break
            except Exception as e:
                print(f"Error while executing the command '{entered_command}': {e}")
                break  # Break the loop on error to avoid attempting to execute other commands
    if not command_found:
        print(f"Command '{entered_command}' not found.")
