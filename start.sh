#!/bin/bash

echo "\033[1;33m[+] Installing Required Modules...."

pkg install python 
pkg install python3
pkg install python git -y
pip install colorama
pip install six
pip install requests

clear

echo "Checking Required modules..."
sleep 2
echo "Starting Program...."
clear
python instagram-bruteforce-attack.py
