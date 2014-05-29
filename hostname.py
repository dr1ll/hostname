#!/usr/bin/python
#-*- coding: utf-8 -*-

###########################################
# RandomHostname.py
# Erstellt fuer Linux unter Python 2.7.3
# Das Programm setzt den Netzwerknamen
# - nach eigener manueller Eingabe
# - aus der Wordlist '~/.HostnameWordlist'
# - aus der Systemdatei /etc/hostname
# - zufaellig (3-12 random characters)
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

version = "0.1.28"
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


# defs


def makenamelist():
    inputfile = open(Hostnamelist_Path, 'r')
    listtext = inputfile.read()
    inputfile.close()
    listarray = listtext.split("\n")
    return listarray


def randomname():
    laenge = random.randint(2, 11)
    finalname = random.choice(Ascii)
    for i in range(laenge):
        finalname += random.choice(AllChars)
    return finalname


def listname():
    tmp = random.choice(NameList)
    return tmp


def combinename():
    laenge = random.randint(3, 7)
    numbers = string.digits
    finalname = random.choice(NameList)
    for i in range(laenge):
        finalname += random.choice(numbers)
    return finalname


def ownname():
    weiter = False
    own = ''
    while weiter == False:
        print"\n4: Hostnamen nun manuell eingeben \n"
        print"(Groß- Kleinschrift Zahl | keine Leer- und Sonderzeichen)"
        weiter = True
        own = raw_input("\nEingabe >>> ")
        i = 1
        for c in own:
            if not c in Ascii and i == 1:
                print"*** Fehler: ERSTER Buchstabe immer nur a-z oder A-Z! ***\n"
                weiter = False
                break
            if not c in AllChars:
                print"*** Fehler: Geben Sie nur a-z, A-Z, 0-9 ein! ***\n"
                weiter = False
                break
            i += 1
    return own


def replacename():
    weiter = False
    while weiter == False:
        print"\n5: Permanenten Hostnamen nun manuell eingeben \n"
        print"(Groß/Kleinschrift/Zahl - keine Leer/Sonderzeichen)"
        weiter = True
        newname = raw_input("\nEingabe >>> ")
        i = 1
        for c in newname:
            if not c in Ascii and i == 1:
                print"*** Fehler: ERSTER Buchstabe immer nur a-z oder A-Z! ***\n"
                weiter = False
                break
            if not c in AllChars:
                print"*** Fehler: Geben Sie nur a-z, A-Z, 0-9 ein! ***\n"
                weiter = False
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
    print"Folgender Hostname wird dauerhaft gespeichert: "+fix
    os.system("hostname -b {0}".format(fix))


def setname(toset):
    os.system("hostname -b {0}".format(toset))


def start_command():
    os.system("clear")
    print"+++++++++++++++++++++++++ Linux-Hostnamen setzen ++++++++++++++++++++++++++++"
    print"Please execute as \"ROOT\"", "                                            v", version
    print
    print"Aktueller Hostname: ", HostName
    print"Hostname n. Reboot: ", StoredName
    print
    print("Für das Setzen eines Netzwerknamens stehen folgende Aktionen zur Verfügung:\n")
    print("1 - Temporären Zufalls-Hostnamen setzen lassen")
    print("2 - Temporären Hostnamen aus Namensliste setzen lassen")
    print("3 - Temporären Hostnamen aus Namensliste mit Modifikation setzen lassen")
    print("4 - Temporären Hostnamen selbst eingeben")
    print("5 - Permanenten Hostnamen in das System eingeben")
    print("6 - Aktuellen Hostnamen nur in Datei dauerhaft speichern")
    print("7 - Vormals gespeicherten Hostnamen reaktivieren (aus Datei resetten)")
    print
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    choice = str(raw_input("Geben Sie die Zahl der gewünschten Aktion (1-7) ein: "))

    if choice == "1":
        nametoset = randomname()
    elif choice == "2":
        nametoset = listname()
    elif choice == "3":
        nametoset = combinename()
    elif choice == "4":
        nametoset = ownname()
    elif choice == "5":
        replacename()
    elif choice == "6":
        filename()
    else:
        fixname()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        setname(nametoset)
        weiter = False
        while weiter == False:
            weiter = True
            answer = raw_input("\nAktuellen Hostnamen dauerhaft abspeichern (J/n)? > ")
            if answer == "J" or answer == "j":
                outputfile = open('/etc/hostname', 'w')
                outputfile.write(nametoset)
                outputfile.close()
            elif answer == "n" or answer == "N":
                pass
            else:
                weiter = False


def end_command():
    inputfile = open('/etc/hostname', 'r')
    SysName = inputfile.read()
    inputfile.close()
    HostName = socket.gethostname()

    print
    print"Hostname      vorher:", OldName
    print"Hostname     aktuell:", HostName
    print"Hostname nach Reboot:", SysName


if __name__ == '__main__':
    commandeer.cli()
    NameList = makenamelist()
    start_command()
    end_command()