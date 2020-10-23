import os
from colorama import Fore, Style
import sys
import time
import socket
import json
import sys

os.system("clear")
print("Checking Files....")
time.sleep(0.5)
files = os.listdir()
if "blackawz.py" not in files:
    print("can not found blackawz.py")
elif "blackawz.py" in files:
    time.sleep(1)
    print("blackfox.py ..... Ok")
if "setup" not in files:
    print("can not found setup folder")
elif "setup" in files:
    time.sleep(1)
    print("setup ..... Ok")
filesSetup = os.listdir("setup")
if "setup.c" in filesSetup:
    print("""    |setup.c ..... Ok""")
if "setup" in filesSetup:
    print("""    |setup ..... Ok""")
if "setup.c" not in filesSetup:
    print("""    |setup.c ..... NOT FOUND""")
elif "setup" not in filesSetup:
    print("""    |setup ..... NOT FOUND""")
if "modules" not in files:
    print("can not found modules folder")
elif "modules" in files:
    time.sleep(1)
    print("modules ..... Ok")
filesModules = os.listdir("modules")
if "banner.py" in filesModules:
    print("""    |banner.py ..... Ok""")
if "deb.py" in filesModules:
    print("""    |deb.py ..... Ok""")
if "banner.py" not in filesModules:
    print("""    |banner.py ..... NOT FOUND""")
elif "deb.py" not in filesModules:
    print("""    |deb.py ..... NOT FOUND""")
if "template" not in files:
    print("can not found template folder")
elif "template" in files:
    time.sleep(1)
    print("template ..... Ok")
time.sleep(5)
os.system("clear")
print("installing....")
time.sleep(1.6)
os.system("clear")
print("installing...")
time.sleep(1.6)
os.system("clear")
print("installing..")
time.sleep(1.6)
os.system("clear")
print("installing.")
time.sleep(1.6)
os.system("clear")
IPaddress=socket. gethostbyname(socket. gethostname())
print("Checking Network \.")
time.sleep(1.6)
os.system("clear")
print("Checking Network /.")
time.sleep(1.6)
os.system("clear")
print("Checking Network \.")
time.sleep(1.6)
os.system("clear")
if IPaddress=="127.0.0.1":
   print("No internet, your localhost is "+ IPaddress)
else:
    print("Connected, with the IP address: "+ IPaddress )
time.sleep(1.6)
try:
    print(Style.BRIGHT+Fore.CYAN+"Install colorama"+Style.RESET_ALL)
    time.sleep(1)
    os.system("pip3 install colorama")
except:
    print("install colorama by pip or pip3")
try:
    os.system("pip install colorama")
except:
    print("install colorama by pip or pip3")
try:
    print(Style.BRIGHT+Fore.CYAN+"Install pyngrok 2.1.7"+Style.RESET_ALL)
    os.system("pip3 install pyngrok==2.1.7")
except:
    print("install pyngrok==2.1.7")
try:
    os.system("pip install pyngrok==2.1.7")
except:
    print("install pyngrok==2.1.7")
try:
    print(Style.BRIGHT+Fore.CYAN+"install php"+Style.RESET_ALL)
    time.sleep(1)
    os.system("sudo apt install php -y")
except:
    print("please install php.")
try:
    print(Style.BRIGHT+Fore.CYAN+"install git"+Style.RESET_ALL)
    os.system("sudo apt install git -y")
except:
    print("please install git.")