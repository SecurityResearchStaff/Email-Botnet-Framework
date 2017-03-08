import os
import sys

option = raw_input("\033[1;32mScan Gmail/Yahoo? [y/G]> \033[1;m")
if option == 'g':
     os.system('python Scanner/scanner.py -d gmail.com -l 500 -b scan')
else:
	print "coming soon..."