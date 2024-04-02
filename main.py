import os
import time
import pywintypes
import win32api
import win32con
import win32ui
from pyautogui import size as screenSize

# Get the screen width and height
start_width, start_height = screenSize()

def clearConsole():
    os.system("cls")

def setRes(w, h):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = w
    devmode.PelsHeight = h

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT | win32con.VREFRESH

    win32api.ChangeDisplaySettings(devmode, 0)


def WindowExists(classname):
    try:
        win32ui.FindWindow(classname, None)
    except win32ui.error:
        return False
    else:
        return True


def print_title():
    title = "\033[35;1m" + r"""               _                      
    __ _ _   _| |_ ___  _ __ ___  ___ 
   / _` | | | | __/ _ \| '__/ _ \/ __|
  | (_| | |_| | || (_) | | |  __/\__ \
   \__,_|\__,_|\__\___/|_|  \___||___/
   """ + "\033[0m"
    print(title)

def main():
    clearConsole()
    print_title()

    classname = input("" + "What classname should I look for [default: LWJGL (lunarclient)]? " + "\033[0m")
    if classname == "":
        classname = "LWJGL"
    clearConsole()
    print_title()
    print(f"Classname: \033[35;1m{classname}\033[0m")
    print()
    print("" + "What resolution should I set when the classname is detected?" + "\033[0m")
    print("\033[35;1m[\033[33;1m1\033[35;1m]\033[0m 1920x1080")
    print("\033[35;1m[\033[33;1m2\033[35;1m]\033[0m 1440x1080")
    print("\033[35;1m[\033[33;1m3\033[35;1m]\033[0m 1280x720")
    print("\033[35;1m[\033[33;1m4\033[35;1m]\033[0m 600x800")
    resolution = input("Choice [default: 3]: ")
    if resolution == "":
        resolution = 3


    try:
        res_id = int(resolution)
    except ValueError:
        print("Wrong resolution!")
        os._exit()

    resolutions = [(1920, 1080), (1440, 1080), (1280, 720), (800, 600)]

    clearConsole()
    print_title()
    print(f"Classname: \033[35;1m{classname}\033[0m")
    print(f"Resolution: \033[35;1m{"x".join(list(str(i) for i in resolutions[res_id-1]))}\033[0m")
    print()

    wasOpen = False

    while True:
        try:
            if WindowExists(classname):
                if not wasOpen:
                    setRes(resolutions[int(res_id)-1][0], resolutions[int(res_id)-1][1])
                    wasOpen = True
                    print("\033[30;1m[\033[35;1mevent\033[30;1m]\033[0m Process \033[32;1mstarted\033[0m")

            else:
                if wasOpen:
                    setRes(start_width, start_height)
                    wasOpen = False
                    print("\033[30;1m[\033[35;1mevent\033[30;1m]\033[0m Process \033[31;1mclosed\033[0m")

            time.sleep(.1)
        except KeyboardInterrupt:
            os._exit(0)

if __name__ == "__main__":
    main()
