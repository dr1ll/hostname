#!/usr/bin/python
#-*- coding: utf-8 -*-

###########################################
# - hostname.py -
# For Linux / Python 2.7.3
# - setting a hostname
# - different modes
# - wordlist-path: '~/.HostnameWordlist'
# - OS-file: /etc/hostname
###########################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os
import socket
import random
import string
import commandeer


# vars

version = "0.1.32"
Ascii = string.ascii_letters
Numbers = string.digits
AllChars = Ascii+Numbers
OldName = socket.gethostname()
HostName = socket.gethostname()
inputfile = open('/etc/hostname', 'r')
StoredName = inputfile.read()
inputfile.close()
nametoset = ''
Script_Dir = os.path.dirname(__file__)
Hostnamelist_Filename = ".HostnameWordlist"
Hostnamelist_Path = os.path.join(Script_Dir, Hostnamelist_Filename)
goon = False

# defs


def makenamelist():
    inputfile = open(Hostnamelist_Path, 'r')
    listtext = inputfile.read()
    inputfile.close()
    listarray = listtext.split("\n")
    return listarray


def randomname():
    length = random.randint(2, 11)
    finalname = random.choice(Ascii)
    for i in range(length):
        finalname += random.choice(AllChars)
    return finalname


def listname():
    tmp = random.choice(NameList)
    return tmp


def combinename():
    length = random.randint(3, 7)
    numbers = string.digits
    finalname = random.choice(NameList)
    for i in range(length):
        finalname += random.choice(numbers)
    return finalname


def ownname():
    goon = False
    own = ''
    while goon == False:
        print"\n4: Input your own hostname \n"
        print"(Only A-Z / a-z / 0-9)"
        goon = True
        own = raw_input("\n>>> ")
        i = 1
        for c in own:
            if not c in Ascii and i == 1:
                print"*** First Character should be a-z or A-Z! ***\n"
                goon = False
                break
            if not c in AllChars:
                print"*** Please use only a-z, A-Z, 0-9 ! ***\n"
                goon = False
                break
            i += 1
    return own


def replacename():
    goon = False
    while goon == False:
        print"\n5: Input a hostname for storing:\n"
        print"(Only A-Z / a-z / 0-9)"
        goon = True
        newname = raw_input("\n>>> ")
        i = 1
        for c in newname:
            if not c in Ascii and i == 1:
                print"*** First Character should be a-z or A-Z! ***\n"
                goon = False
                break
            if not c in AllChars:
                print"*** Please use only a-z, A-Z, 0-9 ! ***\n"
                goon = False
                break
            i += 1
        outputfile = open('/etc/hostname', 'w')
        outputfile.write(newname)
        outputfile.close()
    return newname


def filename():
    actualname = socket.gethostname()
    outputfile = open('/etc/hostname', 'w')
    outputfile.write(actualname)
    outputfile.close()


def fixname():
    inputfile = open('/etc/hostname', 'r')
    fix = inputfile.read()
    inputfile.close()
    print"This hostname is stored permanently: "+fix
    os.system("hostname -b {0}".format(fix))

def androidname_command():
    length = 16
    lowercase = string.ascii_lowercase
    androidchars = Numbers+lowercase
    finalname = 'android-'
    for i in range(length):
        finalname += random.choice(androidchars)
    return finalname


def help_command():
    print('Help is still empyty ')
    pass


def setname(toset):
    os.system("hostname -b {0}".format(toset))


def start_command():
    os.system("clear")
    print"+++++++++++++++++++++++ hostname.py for Linux V",version,"++++++++++++++++++++++++\n"
    print"Please execute as \"ROOT\" !"
    print
    print"Hostname is now actual: ", HostName
    print"Hostname  after reboot: ", StoredName
    print
    print("Choose an option:\n")
    print("1 - Set an actual hostname randomly")
    print("2 - Set an actual hostname from a wordlist")
    print("3 - Set an actual hostname form a wordlist with modifications")
    print("4 - Set an Android-hostname")
    print("5 - Set an actual hostname yourself")
    print("6 - Set a permanent hostname")
    print("7 - Store the actual hostname permanently")
    print("8 - Reset a stored hostname from the OS-file")
    print("9 - Help")
    print
    choice = str(raw_input("Your choice (1-9):\n\n>>> "))

    if choice == "1":
        nametoset = randomname()
    elif choice == "2":
        nametoset = listname()
    elif choice == "3":
        nametoset = combinename()
    elif choice == "4":
        nametoset = androidname_command()
    elif choice == "5":
        nametoset = ownname()
    elif choice == "6":
        replacename()
    elif choice == "7":
        filename()
    elif choice == "8":
        fixname()
    else:
        help_command()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "8":
        setname(nametoset)
        goon = False
        while goon == False:
            goon = True
            answer = raw_input("\nStore this for next reboot (Y/n)?\n\n>>> ")
            if answer == "Y" or answer == "y" or answer == "":
                outputfile = open('/etc/hostname', 'w')
                outputfile.write(nametoset)
                outputfile.close()
            elif answer == "N" or answer == "n":
                pass
            else:
                goon = False


def end_command():
    inputfile = open('/etc/hostname', 'r')
    SysName = inputfile.read()
    inputfile.close()
    HostName = socket.gethostname()

    print
    print"Hostname before:", OldName
    print"Hostname actual:", HostName
    print"Hostname reboot:", SysName
    print"\n+++ done +++\n"


if __name__ == '__main__':
    commandeer.cli()
    NameList = makenamelist()
    start_command()
    end_command()
