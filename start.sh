#!/bin/bash
#Modified by : Shantanu Patel

RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"
YELLOW="$(printf '\033[33m')" BLUE="$(printf '\033[1;34m')"

echo -e "${RED}[+] ${GREEN}Installing Required Modules...."

pkg install python 
pkg install python3
pkg install python git -y
pkg install termux-api
pip install colorama
pip install six
pip install requests

clear

pkg update && pkg upgrade
clear
echo -e "${YELLOW}[+] ${GREEN}Installing Tor...."
sleep 1
pkg install tor
clear
sleep 1
echo -e "\n${YELLOW}Please open second terminal and run this command :- ${BLUE}tor \nafter running tor again come in this terminal"
sleep 3
echo -e "${BLUE}\n[✓] ${GREEN}Starting Program...."
sleep 1
clear
python instagram-bruteforce-attack.py
