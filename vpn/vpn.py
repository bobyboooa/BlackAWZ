import os
import time
from colorama import Fore, Style

def connect():
    os.system("sudo windscribe connect")
    time.sleep(5)
    os.system("clear")

def disconnect():
    os.system("sudo windscribe disconnect")
    time.sleep(5)
    os.system("clear")

def status():
    os.system("sudo windscribe status")
    time.sleep(5)
    os.system("clear")

def login():
    os.system("sudo windscribe login")
    time.sleep(5)
    os.system("clear")


def vpnmenu():
    menu =Style.BRIGHT+Fore.YELLOW+"""
    1 ) connect
    2 ) disconnect
    3 ) status
    4 ) login
    5 ) back
    """
    print(menu+Style.RESET_ALL)
    choice = input(Style.BRIGHT+Fore.RED+">>>")
    if choice == "1":
        connect()
    if choice == "2":
        disconnect()
    if choice == "3":
        status()
    if choice == "4":
        login()
    if choice == "5":
        os.system("python3 blackawz.py")
