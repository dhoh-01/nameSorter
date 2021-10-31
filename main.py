#!/usr/bin/python

import sys
from utils import printName

#read inputs
input = ""
if sys.argv[1] != "":
    input = sys.argv[1]
else:
    print("Input file is not there")
    exit(1) 

#read file
inputFile = open(input, "r")
fileRead = inputFile.read()
fileRead = fileRead.rstrip()
inputFile.close()

#parse file
#names are able to have up to the 3 given names, then a surname
#eg. name1 name2 name3 surname
#names will be ordered as such: surname name1 name2 name3
surnameDict = {}
individualName = fileRead.split("\n")
for name in individualName:
    individualNameSplit = name.split(" ");
    numberOfNames = len(individualNameSplit)
    if numberOfNames == 2:
        firstname = individualNameSplit[0]
        surname = individualNameSplit[1]

        if surname not in surnameDict:
            surnameDict[surname] = {}
        if firstname not in surnameDict[surname]:
            surnameDict[surname][firstname] = {}

    elif numberOfNames == 3:
        firstname = individualNameSplit[0]
        secondname = individualNameSplit[1]
        surname = individualNameSplit[2]

        if surname not in surnameDict:
            surnameDict[surname] = {}
        if firstname not in surnameDict[surname]:
            surnameDict[surname][firstname] = {}
        firstnameDict = surnameDict[surname][firstname]
        if secondname not in firstnameDict:
            firstnameDict[secondname] = {}

    elif numberOfNames == 4:
        firstname = individualNameSplit[0]
        secondname = individualNameSplit[1]
        thirdname = individualNameSplit[2]
        surname = individualNameSplit[3]

        if surname not in surnameDict:
            surnameDict[surname] = {}
        if firstname not in surnameDict[surname]:
            surnameDict[surname][firstname] = {}
        firstnameDict = surnameDict[surname][firstname]
        if secondname not in firstnameDict:
            firstnameDict[secondname] = {}
        secondnameDict = firstnameDict[secondname]
        if thirdname not in secondnameDict:
            secondnameDict[thirdname] = {}

    else:
        continue

orderedString = ""
        
surnames = surnameDict.keys()
surnames.sort()
for surnameSorted in surnames:
    printName(surnameSorted, "", surnameDict[surnameSorted])

#write to file
fw = open("sorted-names-list.txt", "w")
fw.write(orderedString)
fw.close()
