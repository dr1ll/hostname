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

version = "0.1.35"
Ascii = string.ascii_letters
Numbers = string.digits
AllChars = Ascii+Numbers
OldName = socket.gethostname()
HostName = socket.gethostname()
InputFile = open('/etc/hostname', 'r')
StoredName = InputFile.read()
InputFile.close()
nametoset = ''
Script_Dir = os.path.dirname(__file__)
Hostnamelist_Filename = ".HostnameWordlist"
Hostnamelist_Path = os.path.join(Script_Dir, Hostnamelist_Filename)
goon = False
choice = ""

# defs


def makenamelist():
    InputFile = open(Hostnamelist_Path, 'r')
    listtext = InputFile.read()
    InputFile.close()
    listarray = listtext.split("\n")
    return listarray


def choiceinput():
    answer = str(raw_input("Your choice (1-9):\n\n>>> "))
    return answer


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
        print"\n5: Input your own hostname (only A-Z / a-z / 0-9):\n"
        goon = True
        own = raw_input("\n>>> ")
        i = 1
        for c in own:
            if not c in Ascii and i == 1:
                print"*** First Character should be a-z or A-Z! ***\n"
                goon = False
            if not c in AllChars:
                print"*** Please use only a-z, A-Z, 0-9 ! ***\n"
                goon = False
            i += 1
    return own


def replacename():
    goon = False
    while goon == False:
        print"\n6: Input a hostname for storing (only A-Z / a-z / 0-9):\n"
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
    InputFile = open('/etc/hostname', 'r')
    fix = InputFile.read()
    InputFile.close()
    print"\nThis hostname will be resetted: "+fix
    os.system("hostname -b {0}".format(fix))


def androidname_command():
    length = 16
    lowercase = string.ascii_lowercase
    androidchars = Numbers+lowercase
    finalname = 'android-'
    for i in range(length):
        finalname += random.choice(androidchars)
    return finalname


def showfavourite():
    print"\nSORRY: This function is empty\n"
    pass


def setfavourite():
    print"\nSORRY: This function is empty\n"
    pass


def loadfavourite_command():
    print"\nSORRY: This function is empty\n"
    pass


def help_command():
    print"\nSORRY: This function is empty\n"
    pass


def setname(toset):
    os.system("hostname -b {0}".format(toset))


def header():
    os.system("clear")
    print"+++++++++++++++++++++++ hostname.py for Linux v"+version,"++++++++++++++++++++++++\n"
    print"Please execute as \"ROOT\"! Reboot lets changes take effect!"
    print
    print"Hostname is now actual: ", HostName
    print"Hostname  after reboot: ", StoredName
    print

def start_command():
    header()
    print("Choose an option:\n")
    print("1 - Set an actual hostname randomly")
    print("2 - Set an actual hostname from a wordlist")
    print("3 - Set an actual hostname form a wordlist with modifications")
    print("4 - Set an Android-hostname")
    print("5 - Set a self-defined actual hostname")
    print("6 - Store a new permanent hostname")
    print("7 - Store the actual hostname permanently")
    print("8 - Reset a stored hostname from the OS-file")
    print("9 - more functions")
    print

    choice = choiceinput()
    nametoset = ""
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
        more_command()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
        setname(nametoset)
        goon = False
        while goon == False:
            goon = True
            answer = raw_input("\nStore this choice for next reboot (Y/n)?\n\n>>> ")
            if answer == "Y" or answer == "y" or answer == "":
                outputfile = open('/etc/hostname', 'w')
                outputfile.write(nametoset)
                outputfile.close()
            elif answer == "N" or answer == "n":
                pass
            else:
                goon = False


def more_command():
    header()
    print("Choose some more options:\n")
    print("1 - Show favourite hostnames")
    print("2 - Set a favourite hostname")
    print("3 - Load a favourite hostname")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - Help")
    print("9 - Go back")
    print

    choice = choiceinput()


    if choice == "1":
        showfavourite()
    elif choice == "2":
        setfavourite()
    elif choice == "3":
        loadfavourite_command()
    elif choice == "8":
        help_command()
    elif choice == "7":
        return
    else:
        start_command()

    if choice == "2" or choice == "3" or choice == "4":
        setname(nametoset)
        goon = False
        while goon == False:
            goon = True
            answer = raw_input("\nStore this choice for next reboot (Y/n)?\n\n>>> ")
            if answer == "Y" or answer == "y" or answer == "":
                outputfile = open('/etc/hostname', 'w')
                outputfile.write(nametoset)
                outputfile.close()
            elif answer == "N" or answer == "n":
                pass
            else:
                goon = False


def end_command():
    InputFile = open('/etc/hostname', 'r')
    SysName = InputFile.read()
    InputFile.close()
    HostName = socket.gethostname()

    print
    print"Hostname before:", OldName
    print"Hostname actual:", HostName
    print"Hostname reboot:", SysName
    print"\n>>> done, perhaps you better reboot!?\n"


if __name__ == '__main__':
    commandeer.cli()
    NameList = makenamelist()
    start_command()
    end_command()
