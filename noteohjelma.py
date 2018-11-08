# -*- coding: cp1252 -*-
import time

notebook = open("notebook.txt","a")
notebook.close()
end = True

while(end):
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit")
    valinta = int(input("Please select one: "))

    def readnotebook():
        try:
            notebook = open("notebook.txt","r")
            content = notebook.readlines()
            for i in content:
                print(i)
            notebook.close()
        except IOError:
            return False

    def addnote(input):
        notebook = open("notebook.txt","a")
        input = str(input)
        input = input + ":::"+time.strftime("%X %x")+"\n"
        content = notebook.write(input)
        notebook.close()

    def emptynotebook():
        notebook = open("notebook.txt","w")
        content = notebook.write("")
        notebook.close()
        print("Notes deleted.")

    def shutdown():
        end = False

    if(valinta == 1):
        readnotebook()
    elif(valinta == 2):
        note = input("Write a new note: ")
        addnote(note)
    elif(valinta == 3):
        emptynotebook()
    elif(valinta == 4):
        #shutdown()
        end = False
    else:
        print("Incorrect selection")
        
print("Notebook shutting down, thank you.")
