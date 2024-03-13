import random
from termcolor import colored
import os
def help(command):
    if command[0] == "help":
        print(
            "available commands: neofetch, whoami, shutdown, bored, software_update, echo, ls, weather, faq, clear, ipg, write, rm, cd, mkdir, rmdir, pwd")


def software_update(command):
    if command[0] == "software_update":
        print("what's new: -added clear command -added ip generator -added FS -added better command system")

def whoami(command):
    if command[0] == "whoami":
        print("root")

def shutdown(command):
    if command[0] == "shutdown":
        exit()

def echo(command):
    if command[0] == "echo":
        if len(command) == 2:
            print(command[1])



def Neofetch(command):
    if command[0] == "neofetch":
        print("OS: OrbitOS 3.2.2")
        print("security patch: 1 march 2024")
        print("host: device 8082")
        print("kernel: 5.4.0 orbitosarm64")
        print("arch: arm64")
        print("packages: 0")
        print("shell: bash")
        print("resolution: 1920x1080")
        print("CE: LXDE")
        print("WM: POS")
        print("terminal: Orbit CLI")
        print("terminal font: Cascadia Code")
        print("CPU: Intel(R) Core(TM) i5-10500 CPU @ 2.50GHz")
        print("GPU: Intel(R) UHD Graphics  620")
        print("memory: 6495Mib/8937Mib")

def bored(command):
    if command[0] == "bored":
        print("touch grass")
        print("play games")
        print("watch youtube")
        print("watch Netflix")
        print("watch TikTok")
        print("listen to some music on Spotify")
        print("read a book")
        print("play chess")
        print("sleep")
        print("talk with AI")

def weather(command):
    if command[0] == "weather":
        c = colored
        print(c("Weather for new York", "green"))
        print(c("temperature: 25°C", "red"))
        print(c("humidity: 50%", "blue"))
        print(c("wind speed: 10km/h", "yellow"))
        print(c("sunrise: 6:00 AM", "green"))
        print(c("sunset: 6:00 PM", "red"))

def faq(command):
    if command[0] == "faq":
        c = colored
        print(c("is OrbitOS open source?", "blue"))
        print(c("yes, OrbitOS is open source and can be found on github. you can also fork it on replit", "green"))
        print(c("is OrbitOS available on all devices?", "blue"))
        print(c("yes, OrbitOS is available on all devices running a browser and can be found on replit", "green"))
        print(c("will OrbitOS get new commands?", "blue"))
        print(c("yes, OrbitOS will get new commands and will be updated on github", "green"))
        print(c("is OrbitOS a real operating system?", "blue"))
        print(c("no, OrbitOS is not a real operating system, it is command based.", "green"))
        print(c("i found a bug or i have a suggestion, what should i do?", "blue"))
        print(c("you can report the bug or suggestion on the github page or comment on this repl.", "green"))

def clear(command):
    if command[0] == "clear":
        os.system("clear")

def ipg(command):
    if command[0] == "ipg":
        print("----")
        print("IP Generator")
        print("----")
        print(
            "Enter the amount of IPs you want to generate, warning ⚠️ it may lead to a crash if you generate too many! ")
        amount = int(input("Amount: "))
        print("----")
        print("IPs:")
        print("----")
        for i in range(amount):
            print(
                f"IP {i + 1}: {random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")



