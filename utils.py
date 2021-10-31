#!/usr/bin/python

def printName(surname, name, dicts):
    keys = dicts.keys()
    keys.sort()
    for key in keys:
        if(not dicts[key]):
            if name != "" and not name.endswith(" "):
                name += " "
            if key!= "":
                key+= " "
            print name + key + surname
        else:
            if name != "":
                name += " "
            newName =  name + key
            printName(surname,newName,dicts[key])
