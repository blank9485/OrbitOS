
# refeactored into a class based system, for greater control and scalabillity


import random
from termcolor import colored
import os
import time

class CommandProcessor:
    @staticmethod
    def help(command):
        if command[0] == "help":
            print("available commands: neofetch, whoami, shutdown, bored, software_update, echo, ls, weather, faq, clear, ipg, write, rm, cd, mkdir, rmdir, pwd, rservices, stop")

    @staticmethod
    def software_update(command):
        if command[0] == "software_update":
            print("what's new: -downgraded to 3.2.4 -added FS -added better command system")

    @staticmethod
    def whoami(command):
        if command[0] == "whoami":
            print("root")

    @staticmethod
    def shutdown(command):
        if command[0] == "shutdown":
            exit()

    @staticmethod
    def echo(command):
        if command[0] == "echo":
            if len(command) == 2:
                print(command[1])

    @staticmethod
    def Neofetch(command):
        if command[0] == "neofetch":
            print("OS: OrbitOS 3.2.2")
            print("security patch: 1 march 2024")
            print("host: device 8082")
            print("kernel: 5.4.1 orbitosarm64")
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

    @staticmethod
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

    @staticmethod
    def weather(command):
        if command[0] == "weather":
            c = colored
            print(c("Weather for new York", "green"))
            print(c("temperature: 25°C", "red"))
            print(c("humidity: 50%", "blue"))
            print(c("wind speed: 10km/h", "yellow"))
            print(c("sunrise: 6:00 AM", "green"))
            print(c("sunset: 6:00 PM", "red"))

    @staticmethod
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

    @staticmethod
    def clear(command):
        if command[0] == "clear":
            os.system("clear")

    @staticmethod
    def ipg(command):
        if command[0] == "ipg":
            print("----")
            print("IP Generator")
            print("----")
            print("Enter the amount of IPs you want to generate, warning ⚠️ it may lead to a crash if you generate too many! ")
            amount = int(input("Amount: "))
            print("----")
            print("IPs:")
            print("----")
            for i in range(amount):
                print(f"IP {i + 1}: {random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")

    @staticmethod
    def rservice(command):
        if command[0] == "rservices":
            print("----")
            print("running services")
            print("----")
            print("system")
            print("drivers")
            print("type 'stop' [service name] to stop a running task")

    @staticmethod
    def stop(command):
        if command[0] == "stop":
            if not len(command) == 2:
                print("Usage: stop <service name>")
                return
            if command[1] == "system":
                print("stopping system...")
                time.sleep(3)
                print("couldn't load system properly. please restart")
                exit(0)
            if command[1] == "drivers":
                print("stopping drivers...")
                time.sleep(3)
                print("your device has reached into an error state. please restart")
                exit(0)

# Example usage:
# cmd_processor = CommandProcessor()
# cmd_processor.neofetch(["neofetch"])
# cmd_processor.help(["help"])
# And so on for other commands...
