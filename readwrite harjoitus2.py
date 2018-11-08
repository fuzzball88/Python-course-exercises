# -*- coding: cp1252 -*-
name = input("Give a file name: ")
mytext = input("Write something: ")
content = ""

def writetofile(name):

	myfile = open(name,"w")
	content = myfile.write(mytext)
	myfile.close()

def readfromfile(name):

        myfile = open(name,"r")
        content = myfile.read()
        myfile.close()

        return content

writetofile(name)
content = readfromfile(name)

print("wrote",content,"to the file",name)

