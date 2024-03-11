COMMAND = "rm"

from time import sleep

def cmd(args):
    if "-rf" in args and "/" in args:
        print("this is a dangerous command and cannot execute. use rm -rf-# to skip this warning")
        return

    if "-rf-#" in args:
        print("⚠️ Missing drivers: /system/binary/drivers/ is required ⚠️") 
        sleep(2)
        exit(0)