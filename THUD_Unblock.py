import ctypes
import os
import pathlib
import platform
import sys
import time
import win32api
import wmi

from injector import Injector
from ctypes import *

 



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def determine_dll_file():
    if platform.platform().lower().startswith('windows-7'):
        win_platform = 'win7'
    elif platform.platform().lower().startswith('windows-10'):
        win_platform = 'win10'
    else:
        print('Could not find Windows version')
        sys.exit(1)

    if platform.architecture()[0].startswith('64'):
        win_arch = 64
    elif platform.architecture()[0].startswith('32'):
        win_arch = 32
    else:
        print('Could not find the Windows Architecture')
        sys.exit(1)

    if win_platform == 'win7' and win_arch == 64:
        return os.path.join(pathlib.Path(__file__).parent.absolute(),'win7x64_dll_inject.dll')  
    if win_platform == 'win10' and win_arch == 64:
        return os.path.join(pathlib.Path(__file__).parent.absolute(),'win10x64_dll_inject.dll')

# Path to inject file
dll_path = determine_dll_file()

class THUD_Unblock(object):
    
    def __init__(self):
        pass

    # Just for reference what windows api function is being overrided
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
            
        print('Full DLL path: %s' %dll_path)

        # Inject DLL into THUD
        print('Injecting...')
        injector = Injector()
        injector.load_from_pid(pid)
        injector.inject_dll(dll_path)
        injector.unload()
        print('Injectine Done.')

        # Countdown until exit
        for i in range(10,1,-1):
            print('Exiting in ... %s' %i)
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
