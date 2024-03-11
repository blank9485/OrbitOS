COMMAND = "faq"

from termcolor import colored as c

def cmd(args):
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