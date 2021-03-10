import ctypes
import os
import pathlib
import sys
import time
import win32api
import wmi

from injector import Injector
from ctypes import *
dll_path = os.path.join(pathlib.Path(__file__).parent.absolute(),'win7x64_dll_inject.dll')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class THUD_Unblock(object):
    
    def __init__(self):
        pass

    @classmethod
    def unblock(cls,hwnd):
        ctypes.windll.user32.SetWindowDisplayAffinity(hwnd,0)

    @classmethod
    def run(cls):
        # Find the PID of THUD
        c = wmi.WMI ()
        pid = None
        for process in c.Win32_Process ():
            if process.Name.lower() == 'turbohud.exe':
                print('Found THUD')
                print(process.ProcessId, process.Name)
                pid = process.ProcessId

        if not pid:
            print('No PID')
            sys.exit(1)
            
        print("Full DLL path: %s" %dll_path)

        # Inject DLL into THUD
        injector = Injector()
        injector.load_from_pid(pid)
        injector.inject_dll(dll_path)
        injector.unload()

        # Countdown until exit
        for i in range(10,1,-1):
            print("Exiting in ... %s" %i)
            time.sleep(1)

def main():
    # As of season 22, THUD requires admin
    # Need to make sure this script is admin also to inject into THUD
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    try:
        THUD_Unblock.run()
    except Exception as e:
        print(e)


main()
