import os
import sys

option = raw_input("\033[1;32mGmail/Yahoo [y/G]> \033[1;m")
if option == 'g':
     os.system('python Bruteforce/gmail.py')
else:
    os.system('python Bruteforce/yahoo.py')