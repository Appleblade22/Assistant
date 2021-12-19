import os
import subprocess as sp

paths = {

    'notepad': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.exe",
    'discord': "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_calculator():
    os.startfile(paths['calculator'])


def open_cmd():
    os.system('start cmd')
