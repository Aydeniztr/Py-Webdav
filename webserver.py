
import http.server
import socketserver
import functools
from colorama import Fore, Back, Style, init, deinit

init()

banner = '''

@@@  @@@  @@@ @@@@@@@@ @@@@@@@  @@@@@@@   @@@@@@  @@@  @@@
 @@!  @@!  @@! @@!      @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@
 @!!  !!@  @!@ @!!!:!   @!@!@!@  @!@  !@! @!@!@!@! @!@  !@!
  !:  !!:  !!  !!:      !!:  !!! !!:  !!! !!:  !!!  !: .:!
   ::.:  :::   : :: ::: :: : ::  :: :  :   :   : :    ::
   
'''

usg = '''
by aydeniz
'''

to_exit = '''
     __________________       ________       
    ||      ctrl      ||     ||  c   ||      
    ||________________||  +  ||______||     
    |/________________\|     |/______\|      
'''

about = '''
author: Ahmet Yigit AYDENIZ

•github:https://github.com/Aydeniztr
•Website:https://www.aydeniz.tk
 
  • I’m currently working on my own websit
  • I’m currently learning "c" and "sh"
  • I’m looking to not collaborate on my projects
  • I’m looking for help with learning c++
  • Ask me about linux,static-websites,python
  • How to reach me : https://www.aydeniz.tk/chat.html
  
'''

print(Fore.RED + banner+ Fore.WHITE + usg + Fore.WHITE + about)

port = int(input ( Fore.WHITE +'['+ Fore.GREEN + '*' + Fore.WHITE + ']' + Fore.YELLOW + 'select a port number ' + Fore.GREEN + ' (select between 1023-65536)\n'))

if 1024 <= port <= 65535:

  root = str(input('\n' + Fore.WHITE +'['+ Fore.GREEN + '*' + Fore.WHITE + ']' + Fore.YELLOW + 'select a root directory to run the server\n'+ Fore.GREEN ))

  Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory = root)

  with socketserver.TCPServer(("", port), Handler) as httpd:
  
    print('\n'+Fore.WHITE +'['+ Fore.GREEN + '+' + Fore.WHITE + ']' + Fore.YELLOW + "Server started at localhost:" +Fore.YELLOW + str(port)+' ctrl+c to exit\n\n'+Fore.RED+ to_exit +'\n'+Fore.YELLOW)
    httpd.serve_forever()
      
else:
  print('\n'+ Fore.RED +'(!)'+' invalid port exiting ... pls select a valid port ')
  deinit()
  exit()
