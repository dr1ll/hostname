#!/usr/bin/python
#-*- coding: utf-8 -*-

#######################################################
#   Changing hostname - hostname.py                   #
#                                                     #
# - tested for:                                       #
#   Python 2.7.3                                      #
#   Debian Wheezy                                     #
#                                                     #
# - made with:                                        #
#   menue_template.py                                 #     
#                                                     #
# - setting a hostname                                #
# - different modes                                   #
#                                                     #
# - working directory: '~/.hostname.py'               #
# - wordlist-path: '~/.HostnameWordlist'              #
# - favouritelist-path: '~/.Favouritelist'            #
# - OS-file: /etc/.hostname (replacing: .nodename)    #
#                                                     #
#           ***   REBOOT IS IMPORTANT   ***           # 
#                                                     #
#######################################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os
import socket
import random
import string
import commandeer
import time
import webbrowser


# vars

Ascii = string.ascii_letters
Numbers = string.digits
AllChars = Ascii+Numbers
Script_Dir = os.path.dirname(__file__)
Hostnamelist_Filename = ".HostnameWordlist"
Hostnamelist_Path = os.path.join(Script_Dir, Hostnamelist_Filename)
Favouritelist_Filename = ".Favouritelist"
Favouritelist_Path = os.path.join(Script_Dir, Favouritelist_Filename)
goon = False
reboot = False
choice = ""
nametoset = ""
content = []


### Change these vars for your menue:

# Count your versions here:
versionnumber = "0.3.3"

# How many columns do you have in your window for default (Standard=80)?
columns = 80

# Name of your app, this is shown in the first line
title = "Changing hostname"

# Insert hints for header
hint1 = "Please execute as \"ROOT\"! Only REBOOT lets some changes take effect!\n"
hint2 = ""
hint3 = "Hostname  now  actual: "
hint4 = "Hostname after reboot: "
hint5 = "\n[1-9]: Choose option   [Enter]: More options   [Q]: Quit   [H]: Help\n"

# Don't change:
version = " v"+versionnumber
text_for_functions = ["empty"]
emptyfunction = "\nThis function is empty"


# This Class is for refreshing your system's hostname etc.

class Refresh(object):
    OldName = socket.gethostname()
    HostName = socket.gethostname()
    InputFile = open('/etc/hostname', 'r')
    StoredName = InputFile.read()
    InputFile.close()


old = Refresh.OldName
host = Refresh.HostName
stored = Refresh.StoredName


# Here is the header

def header():
    os.system("clear")
    length = int(len(title+version+" "*2))
    host = socket.gethostname()                                 # WHY DOES CLASS REFRESH NOT WORK HERE ???
    InputFile = open('/etc/hostname', 'r')
    stored = InputFile.read()
    InputFile.close()
    print("+"*(int(columns/2)-int(length/2))+" "+title+version+" "+"+"*(int((columns/2)-1)-int(length/2)))
    print
    print(hint1)
    # print(hint2)
    print(hint3+host)
    print(hint4+stored)
    print(hint5)


### defs from hostname.py

def makenamelist():
    InputFile = open(Hostnamelist_Path, 'r')
    listtext = InputFile.read()
    InputFile.close()
    listarray = listtext.split("\n")
    return listarray


NameList = makenamelist()


def choiceinput():
    answer = str(raw_input("\n>>> "))
    return answer


def randomname():                               # returns a random string
    length = random.randint(2, 11)
    finalname = random.choice(Ascii)
    for i in range(length):
        finalname += random.choice(AllChars)
    reboot = True
    return finalname


def listname():                                 # returns a random wordstring from your list
    tmp = random.choice(NameList)
    return tmp


def combinename():                              # returns a randomly modified wordstring
    length = random.randint(3, 7)
    numbers = string.digits
    finalname = random.choice(NameList)
    for i in range(length):
        finalname += random.choice(numbers)
    return finalname


def androidname_command():                           # returns an android hostname
    length = 16
    lowercase = string.ascii_lowercase
    androidchars = Numbers+lowercase
    finalname = 'android-'
    for i in range(length):
        finalname += random.choice(androidchars)
    return finalname


def ownname():                                  # returns of a self-defined string
    goon = False
    own = ''
    while goon == False:
        goon = True
        own = raw_input("\nNow Input your own hostname (only A-Z / a-z / 0-9) >>> ")
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


def replacename():                               # store a self-defined hostname
    goon = False
    while goon == False:
        goon = True
        newname = raw_input("\nNow Input a hostname for storing (only A-Z / a-z / 0-9) >>> ")
        i = 1
        for c in newname:
            if not c in Ascii and i == 1:
                print"*** First Character should be a-z or A-Z! ***\n"
                goon = False
                #break
            if not c in AllChars:
                print"*** Please use only a-z, A-Z, 0-9 ! ***\n"
                goon = False
            i += 1
    outputfile = open('/etc/hostname', 'w')
    outputfile.write(newname)
    outputfile.close()
    return newname


def filename():                                     # stores the existing hostname for reboot
    outputfile = open('/etc/hostname', 'w')
    outputfile.write(socket.gethostname())
    outputfile.close()


def fixname():                                       # reset the already stored hostname
    InputFile = open('/etc/hostname', 'r')
    fix = InputFile.read()
    InputFile.close()
    os.system("hostname -b {0}".format(fix))


def help_command():                                 # call the help-function
    print"SORRY, help is empty"
    time.sleep(1)
    print("But wait...")
    time.sleep(2)
    webbrowser.open("https://github.com/dr1ll/hostname")


def showfavourite():                                 # showes a favourites-list
    InputFile = open(Favouritelist_Path, 'r')
    content = InputFile.read()
    InputFile.close()
    content = content.split("\n")
    header()
    for i in range(9):
        if i < len(content):
            print(str(i+1)+" - "+content[i])
        else:
            print(str(i+1)+" -")


def setfavourite():                                  # sets a fav-hostname
    InputFile = open(Favouritelist_Path, 'r')
    content = InputFile.read()
    InputFile.close()
    content = content.split("\n")
    goon = True
    while goon:
        answer = raw_input("\nWhich position for your new fav (1-9)? >>> ")
        goon = False
        for i in range(1, 10):
            if answer not in (string.digits) or answer == "0" or answer == "":
                goon = True
    goon = False
    while goon == False:
        goon = True
        favname = raw_input("\nNow Input a favourite hostname for storing >>> ")
        i = 1
        for c in favname:
            if not c in Ascii and i == 1:
                print"*** First Character should be a-z or A-Z! ***\n"
                goon = False
                #break
            if not c in AllChars:
                print"*** Please use only a-z, A-Z, 0-9 ! ***\n"
                goon = False
            i += 1
    answer = int(answer)-1
    content[answer] = favname
    outputfile = open(Favouritelist_Path, 'w')
    i = 0
    for i in range(9):
        outputfile.write(content[i]+"\n")
    outputfile.close()


def loadfavourite_command():                        # load a favourite hostname
    goon = True
    while goon:
        answer = raw_input("\nWhich hostname do U want to load (1-9)? >>> ")
        goon = False
        for i in range(1, 10):
            if answer == "0":
                goon = True
            elif answer == "":
                goon = True
            elif answer not in (string.digits):
                goon = True
    InputFile = open(Favouritelist_Path, 'r')
    content = InputFile.read()
    InputFile.close()
    content = content.split("\n")
    answer = int(answer)-1
    load = content[answer]
    return(load)


def storefavourite_command():                       # store a favourite hostname
    goon = True
    while goon:
        answer = raw_input("\nWhich position for your new favourite (1-9)? >>> ")
        goon = False
        for i in range(1, 10):
            if answer not in (string.digits) or answer == "0" or answer == "":
                goon = True
    InputFile = open(Favouritelist_Path, 'r')
    content = InputFile.read()
    InputFile.close()
    content = content.split("\n")
    content[int(answer)-1] = socket.gethostname()
    outputfile = open(Favouritelist_Path, 'w')
    i = 0
    for i in range(9):
        if i != int(answer):
            outputfile.write(content[i]+"\n")
        elif i == int(answer):
            outputfile.write(content[int(answer)]+"\n")
    outputfile.close()


def randomfav_command():
    ranfav = ""
    goon = True
    host = socket.gethostname()
    while goon:
        finalname_int = random.randint(1, 9)
        InputFile = open(Favouritelist_Path, 'r')
        content = InputFile.read()
        InputFile.close()
        content = content.split("\n")
        ranfav = content[finalname_int-1]
        if host == ranfav:
            goon = True
        else:
            goon = False
    return ranfav


def setname(toset):
    os.system("hostname -b {0}".format(toset))
    hostsfile = open('/etc/hosts', 'r')
    hostarray = hostsfile.read()
    hostsfile.close()
    hostarray = hostarray.split("\n")
    exists = False
    for i in range(len(hostarray)):
        if str("127.0.1.1") in hostarray[i]:
            hostarray[i] = str("127.0.1.1   "+str(toset))
            exists = True
    if exists == False:
        hostarray.append("127.0.1.1    "+str(toset))
    hosttext = "\n".join(hostarray)
    hostsfile = open('/etc/hosts', 'w')
    hostsfile.write(hosttext)
    hostsfile.close()


### Inserting your functionality:

# Insert: to os.system('[name of your intern def/function etc. or execute somescript.py]')
# Insert: text_for_functions.append("[String to decribe your function etc.]")
# Remove: print(emptyfunction)

def function1():
    nametoset = randomname()
    setname(nametoset)

text_for_functions.append("Set an actualized hostname randomly")


def function2():
    nametoset = listname()
    setname(nametoset)


text_for_functions.append("Set an actualized hostname from a wordlist")


def function3():
    nametoset = combinename()
    setname(nametoset)

text_for_functions.append("Set an actualized hostname from a wordlist with modification")


def function4():
    nametoset = androidname_command()
    setname(nametoset)


text_for_functions.append("Set an actualized hostname from an Android-device")


def function5():
    nametoset = ownname()
    setname(nametoset)


text_for_functions.append("Set an actualized hostname yourself")


def function6():
    filename()

text_for_functions.append("Store the actualized hostname permanently")


def function7():
    replacename()


text_for_functions.append("Set & Store a new self-defined hostname permanently")


def function8():
    fixname()


text_for_functions.append("Reset a stored hostname from the OS-file")


def function9():
    pass


text_for_functions.append("")


def function10():
    showfavourite()
    print("\nThis is the list of your favourite hostnames!")


text_for_functions.append("Show the list of favourite hostnames")


def function11():
    showfavourite()
    storefavourite_command()
    showfavourite()


text_for_functions.append("Store the actual hostname into the list")


def function12():
    showfavourite()
    setfavourite()
    showfavourite()


text_for_functions.append("Store a self-defined hostname into the list")


def function13():
    showfavourite()
    nametoset = loadfavourite_command()
    setname(nametoset)


text_for_functions.append("Load a favourite hostname from the list")


def function14():
    showfavourite()
    raw_input("\nPress [Enter] to change into a hostname from this list!")
    nametoset = randomfav_command()
    setname(nametoset)
    showfavourite()


text_for_functions.append("Load a random hostname from the list")


def function15():
    pass


text_for_functions.append("")


def function16():
    pass


text_for_functions.append("")


def function17():
    pass


text_for_functions.append("")


def function18():
    pass


text_for_functions.append("")


#!!! STOP inserting stuff here !!!

def menue1():
    header()
    for i in range(1, 10):
        print(str(i)+" - "+text_for_functions[i])
    #print

def menue2():
    header()
    for i in range(1, 10):
        print(str(i)+" - "+text_for_functions[i+9])
    #print


def footer():
    pass


#   def menue3():
#       header()
#       for i in range(10):
#           print(str(i)+" - "+text_for_functions[i+20])
#       print
#       footer()


if __name__ == '__main__':
    commandeer.cli()
    goon = True
    which_menue = 1
    counter = 0
    while goon:
        if counter > 0:
            raw_input("\nPress Enter to continue!")
        counter += 1
        reboot = False
        host
        stored
        if which_menue == 1:
            menue1()
        elif which_menue == 2:
            menue2()
#       elif which_menue == 3:
#           menue3()
        menue_counter = int((which_menue*9)-9)
        choice = choiceinput()
        choices = range(1, 9)
        choice_control = 999
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            choice_control = int(choice)
        if choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9":
            choice_control = int(choice)
        if choice_control in range(9):
            function_string = 'function'+str(choice_control+menue_counter)
            locals()[function_string]()
        if choice == "Q" or choice == "q":
            goon = False
        if choice == "H" or choice == "h":
            help_command()
        elif choice == "":
            if which_menue == 1:
                which_menue = 2
            elif which_menue == 2:
                which_menue = 1
#           elif which_menue == 3:
#               which_menue = 1
            counter = 0
    os.system('clear')
    header()
    for i in range (11):
        print""
    print(">>> end\n")
# end
