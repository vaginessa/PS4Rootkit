import os
import time
from colorama import Fore
import requests

banner = '''

██████╗ ███████╗██╗  ██╗██████╗  ██████╗  ██████╗ ████████╗██╗  ██╗██╗████████╗
██╔══██╗██╔════╝██║  ██║██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║ ██╔╝██║╚══██╔══╝
██████╔╝███████╗███████║██████╔╝██║   ██║██║   ██║   ██║   █████╔╝ ██║   ██║   
██╔═══╝ ╚════██║╚════██║██╔══██╗██║   ██║██║   ██║   ██║   ██╔═██╗ ██║   ██║   
██║     ███████║     ██║██║  ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██╗██║   ██║   
╚═╝     ╚══════╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   
    PS4Rootkit by Crafttino21/WeepingAngel | Exploit by TheFlow                                                        
    » Easy to Use Toolkit for the PPPwn Exploit for PS4 «
        Supported Versions: 9.00-11.00 (More on test!)
                THIS TOOL IS FOR LINUX ONLY!!

'''
menu = '''
[1] First Run (Setup and Installer)
[2] Launch Exploit (Not Recommend for first time!)
[3] Install LightMods PPPwn (Debug Settings)
[4] Run LightMods PPPwn (Debug Settings)
'''

remi = '''
REMINDER!
Your PC LAN-Cable need to be plugged into your PS4!
Go to Settings and then Network
Select Set Up Internet connection and choose Use a LAN Cable
Choose Custom setup and choose PPPoE for IP Address Settings
Enter anything for PPPoE User ID and PPPoE Password
Choose Automatic for DNS Settings and MTU Settings
Choose Do Not Use for Proxy Server
Click Test Internet Connection to communicate with your computer
'''


red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
green = Fore.GREEN

print(red + banner)
print(f"{magenta}Do you wanna Prepare the first run or Just rerun the exploit?")
print(menu)
xddr = input(" > ")

if xddr == "1":
    print(f"[+] Update Distru and APT...")
    os.system("sudo apt update && sudo apt upgrade")
    print(f"[+] Install needed Linux Packages...")
    os.system("sudo apt install python3 && sudo apt install python3-pip && sudo apt install gcc && sudo apt install net-tools")
    print(f"[+] Clone PPPwn Official Respo...")
    os.system("git clone --recursive https://github.com/TheOfficialFloW/PPPwn")
    os.system("clear")
    print(f"[+] Install Python Libarys...")
    os.system("sudo pip install -r requirements.txt")
    os.system("sudo apt install python3-scapy")
    print(f"{green}[+] Finished Part 1/2")
    print(f"{blue}[+] What Firmware do you use?")
    fwr = input("FW [e.x 9.00 = 900, 11.0 = 1100] > ")
    print(f"{magenta}[+] Compiling Payloads...")
    os.system(f"cd PPPwn && make -C stage1 FW={fwr} clean && make -C stage1 FW={fwr}")
    os.system(f"cd PPPwn && make -C stage2 FW={fwr} clean && make -C stage2 FW={fwr}")
    print(f"{green} Instalattion Successfully!")
    print("Now connect a LAN-Cable to your PS4! If you use a VM Set your Network from NAT to Network Bridge!")
    print("Rerun the Script if you finished!")
    time.sleep(8)
    exit()
elif xddr == "2":
    print(f"{magenta} [+] Configuration")
    pat = input("[+] Path of PPPwn > ")
    os.system("ifconfig")
    print(remi)
    adp = input("[+] Input your Network adapter name [e.x enp0s3] > ")
    fwr2 = input("[+] Firmware Version [e.x 9.00 = 900, 11.0 = 1100] > ")
    print(f"{green} [*] Launch Exploit..")
    os.system(f"cd {pat} && sudo python3 pppwn.py --interface={adp} --fw={fwr2}")
elif xddr == "3":
    print(f"[+] Update Distru and APT...")
    os.system("sudo apt update && sudo apt upgrade")
    print(f"[+] Install needed Linux Packages...")
    os.system("sudo apt install python3 && sudo apt install python3-pip && sudo apt install gcc && sudo apt install net-tools && sudo apt install wget")
    print(f"[+] Clone PPPwn Official Respo...")
    os.system("git clone --recursive https://github.com/TheOfficialFloW/PPPwn")
    os.system("clear")
    print(f"[+] Install Python Libarys...")
    os.system("sudo pip install -r requirements.txt")
    os.system("sudo apt install python3-scapy")
    print(f"{green}[+] Finished Part 1/2")
    print(f"{blue}[+] What Firmware do you use?")
    fwr = input("FW [e.x 9.00 = 900, 11.0 = 1100] > ")
    print(f"{magenta}[+] Compiling Payloads...")
    os.system(f"cd PPPwn && make -C stage1 FW={fwr} clean && make -C stage1 FW={fwr}")
    os.system(f"cd PPPwn && make -C stage2 FW={fwr} clean && make -C stage2 FW={fwr}")
    os.system("clear")
    print(f"{blue}[+] Installing Lightmods Payload for debug settings..")
    os.system("wget https://github.com/LightningMods/PPPwn/releases/download/0/stage2.bin && mv -f stage2.bin PPPwn/stage2 && clear")
    print(f"{green}[+] Instalattion Successfully!")
    print("Now connect a LAN-Cable to your PS4! If you use a VM Set your Network from NAT to Network Bridge!")
    print("Rerun the Script if you finished!")
    time.sleep(8)
    exit()
elif xddr == "4":
    print(f"{magenta} [+] Configuration")
    pat = input("[+] Path of PPPwn > ")
    os.system("ifconfig")
    print(remi)
    adp = input("[+] Input your Network adapter name [e.x enp0s3] > ")
    fwr2 = input("[+] Firmware Version [e.x 9.00 = 900, 11.0 = 1100] > ")
    print(f"{magenta}[!] REMINDER: If you get the corrupted data failed.. please try again Run this script here again!")
    print(f"{green}[*] Launch Exploit..")
    os.system(f"cd {pat} && sudo python3 pppwn.py --interface={adp} --fw={fwr2}")
else:
    print(f"{red}Invalid Input")
