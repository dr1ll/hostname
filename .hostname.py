#!/usr/bin/python
#-*- coding: utf-8 -*-

###########################################
# - hostname.py -
# - For Linux / Python 2.7.3
# - setting a hostname
# - different modes
# - wordlist-path: '~/.HostnameWordlist'
# - OS-file: /etc/.hostname
###########################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os
import socket
import random
import string
import commandeer
import time


# vars

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
Favouritelist_Filename = ".Favouritelist"
Favouritelist_Path = os.path.join(Script_Dir, Favouritelist_Filename)
goon = False
choice = ""


### Change these vars for your menue:

# Count your versions here:
versionnumber = "0.2.0"

# How many columns do you have in your window for default (Standard=80)?
columns = 80

# Name oy your app, this is shown in the first line
title = "Changing hostname"

# Insert some hints
hint1 = "Please execute as \"ROOT\"! Reboot lets changes take effect!\n"
hint2 = "Hostname       before: "+OldName
hint3 = "Hostname   now actual: "+HostName
hint4 = "Hostname after reboot: "+StoredName
hint5 = " "*46+"[Enter]: More options   [Q]: Quit\n"

# Don't change:
version = " v"+versionnumber
text_for_functions = []
emptyfunction = "This function is empty"


# Here is the header


def header():
    os.system("clear")
    OldName = socket.gethostname()
    HostName = socket.gethostname()
    InputFile = open('/etc/hostname', 'r')
    StoredName = InputFile.read()
    InputFile.close()
    hint1 = "Please execute as \"ROOT\"! Reboot lets changes take effect!\n"
    hint2 = "Hostname       before: "+OldName
    hint3 = "Hostname   now actual: "+HostName
    hint4 = "Hostname after reboot: "+StoredName
    hint5 = " "*46+"[Enter]: More options   [Q]: Quit\n"
    length = int(len(title+version+" "*2))
    print("+"*(int(columns/2)-int(length/2))+" "+title+version+" "+"+"*(int((columns/2)-1)-int(length/2)))
    print
    print(hint1)
    print(hint2)
    print(hint3)
    print(hint4)
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
    answer = str(raw_input("Your choice (1-9):\n\n>>> "))
    return answer


def randomname():                               # returns a random string
    length = random.randint(2, 11)
    finalname = random.choice(Ascii)
    for i in range(length):
        finalname += random.choice(AllChars)
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


def replacename():                               # store a self-defined hostname
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


def filename():                                     # stores the existing hostname for reboot
    actualname = socket.gethostname()
    outputfile = open('/etc/hostname', 'w')
    outputfile.write(actualname)
    outputfile.close()


def fixname():                                       # reset the already stored hostname
    InputFile = open('/etc/hostname', 'r')
    fix = InputFile.read()
    InputFile.close()
    print"\nThis hostname will be resetted: "+fix
    os.system("hostname -b {0}".format(fix))


def help_command():                                 # call the help-function
    print"Empty function"


def showfavourite():                                 # showes a favourites-list
    InputFile = open(Favouritelist_Path, 'r')
    content = InputFile.read()
    InputFile.close()
    content = content.split("\n")
    i = 0
    header()
    print("The Favourites-list:\n")
    for objects in content:
        print(str(i+1)+" - "+str(objects))
        i += 1
    time.sleep(5)


def setfavourite():                                  # sets a fav-hostname
    print"\nSORRY: This function is empty\n"
    pass


def loadfavourite_command():                        # load a favourite hostname
    print"\nSORRY: This function is empty\n"
    pass


def setname(toset):                                 # function for setting the hostname
    os.system("hostname -b {0}".format(toset))


def storeornot():                                   # routine for storing hostname
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


def end_command():                                   # output at the end of all functions
    InputFile = open('/etc/hostname', 'r')
    SysName = InputFile.read()
    InputFile.close()
    HostName = socket.gethostname()

    print
    print"Hostname before:", OldName
    print"Hostname actual:", HostName
    print"Hostname reboot:", SysName
    print"\n>>> done, perhaps you better reboot!?\n"


### Inserting your functionality:

# Insert: to os.system('[name of your intern def/function etc. or execute somescript.py]')
# Insert: text_for_functions.append("[String to decribe your function etc.]")
# Remove: print(emptyfunction)

def function1():
    nametoset = randomname()
    setname(nametoset)
    storeornot()

text_for_functions.append("Set an actual hostname randomly")


def function2():
    nametoset = listname()
    setname(nametoset)


text_for_functions.append("Set an actual hostname from a wordlist")


def function3():
    nametoset = combinename()
    setname(nametoset)
    storeornot()

text_for_functions.append("Set an actual hostname form a wordlist with modification")


def function4():
    nametoset = androidname_command()
    setname(nametoset)
    storeornot()


text_for_functions.append("Set an Android-hostname")


def function5():
    nametoset = ownname()
    setname(nametoset)


text_for_functions.append("Set a self-defined actual hostname")


def function6():
    replacename()

text_for_functions.append("Store a new permanent hostname")


def function7():
    filename()


text_for_functions.append("Store the actual hostname permanently")


def function8():
    fixname()


text_for_functions.append("Reset a stored hostname from the OS-file")


def function9():
    help_command()


text_for_functions.append("")


def function10():
    help_command()


text_for_functions.append("help")


def function11():
    print(emptyfunction)


text_for_functions.append("Show favourite hostnames")


def function12():
    print(emptyfunction)


text_for_functions.append("Set a favourite hostname")


def function13():
    print(emptyfunction)


text_for_functions.append("Load a favourite hostname")


def function14():
    print(emptyfunction)


text_for_functions.append("")


def function15():
    print(emptyfunction)


text_for_functions.append("")


def function16():
    print(emptyfunction)


text_for_functions.append("")


def function17():
    print(emptyfunction)


text_for_functions.append("")


def function18():
    print(emptyfunction)


text_for_functions.append("")


def function19():
    print(emptyfunction)


text_for_functions.append("")


def function20():
    print(emptyfunction)


text_for_functions.append("help")


#!!! STOP inserting stuff here !!!

def menue1():
    header()
    for i in range(10):
        print(str(i)+" - "+text_for_functions[i])
    print


def menue2():
    header()
    for i in range(10):
        print(str(i)+" - "+text_for_functions[i+10])
    print


def footer():
    end_command()


#def menue3():
#   header()
#   for i in range(10):
#       print(str(i)+" - "+text_for_functions[i+20])
#   print
#   footer()


if __name__ == '__main__':
    commandeer.cli()
    goon = True
    which_menue = 1
    counter = 0
    while goon:
        if counter > 0:
            raw_input("\nPress Enter to continue!")
        counter += 1
        HostName = socket.gethostname()
        InputFile = open('/etc/hostname', 'r')
        StoredName = InputFile.read()
        InputFile.close()
        if which_menue == 1:
            menue1()
        elif which_menue == 2:
            menue2()
#       elif which_menue == 3:
#           menue3()
        menue_counter = int((which_menue*10)-10)
        choice = choiceinput()
        choices = range(10)
        choice_control = 999
        if choice == "0" or choice == "1" or choice == "2" or choice == "3" or choice == "4":
            choice_control = int(choice)
        if choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9":
            choice_control = int(choice)
        if choice_control in range(10):
            function_string = 'function'+str(choice_control+1+menue_counter)
            locals()[function_string]()
        if choice == "Q" or choice == "q":
            goon = False
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
    for i in range (10):
        print(str(i)+" -")
    print('\n'*2)
# end
