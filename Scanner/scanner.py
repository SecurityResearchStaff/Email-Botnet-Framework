#!/usr/bin/env python

import string
import httplib
import sys
import os
from socket import *
import re
import getopt

try:
    import requests
except:

    sys.exit()

from discovery import *
from lib import htmlExport
from lib import hostchecker


def usage():

    comm = os.path.basename(sys.argv[0])

    if os.path.dirname(sys.argv[0]) == os.getcwd():
        comm = "./" + comm

def start(argv):
    if len(sys.argv) < 4:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "l:d:b:s:vf:nhcte:")
    except getopt.GetoptError:
        usage()
        sys.exit()
    start = 0
    host_ip = []
    filename = ""
    bingapi = "yes"
    dnslookup = False
    dnsbrute = False
    dnstld = False
    shodan = False
    vhost = []
    virtual = False
    limit = 100
    dnsserver = ""
    for opt, arg in opts:
        if opt == '-l':
            limit = int(arg)
        elif opt == '-d':
            word = arg
        elif opt == '-b':
            engine = arg
            if engine not in ("scan"):
                usage()
                print "scan"
                sys.exit()
            else:
                pass
    if engine == "scan":
        search = googlesearch.search_google(word, limit, start)
        search.process()
        all_emails = search.get_emails()
        all_hosts = search.get_hostnames()

        all_emails=sorted(set(all_emails))

    if all_emails == []:
        print "somthing went wrong..."
    else:
        print "\n".join(all_emails)

    
  
   
if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Search interrupted by user.."
    except:
        sys.exit()
