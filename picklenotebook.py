# -*- coding: cp1252 -*-
import time
import pickle

def checkNoteBook(notebookname = "notebook.dat"):
        try:
            notebook = open(notebookname,"rb")            
            notebook.close()
        except IOError:
            print("No default notebook was found, created one.")

def changeNoteBook(notebookname):
        try:
            notebookname = open(notebookname,"r")
        except IOError:
            print("No notebook with that name detected, created one.")
            notebookname = open(notebookname,"a")

def main():
    filename = "notebook.dat"
    checkNoteBook(filename)
    notes = {}
    
    while True:
        
        
        print("Now using file",filename)
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Edit a note")
        print("(4) Delete a note")
        print("(5) Save and quit")
        valinta = int(input("Please select one: "))

        def readnotebook():
            try:
                notebook = open(filename,"rb")
                content = notebook.readlines()
                for i in content:
                    print(i)
                notebook.close()
            except IOError:
                return False

        def addnote(input):
            notebook = open(filename,"a")
            input = str(input)
            input = input + ":::"+time.strftime("%X %x")+"\n"
            content = notebook.write(input)
            notebook.close()

        def emptynotebook():
            notebook = open(filename,"w")
            content = notebook.write("")
            notebook.close()
            print("Notes deleted.")

        def shutdown():
            pass

        if(valinta == 1):
            readnotebook()
        elif(valinta == 2):
            note = input("Write a new note: ")
            addnote(note)
        elif(valinta == 3):
            emptynotebook()
        elif(valinta == 4):
            filename = input("Give the name of the new file: ")
            changeNoteBook(filename)
        elif(valinta == 5):
            #shutdown()
            break
            notebook.close()
        else:
            print("Incorrect selection")
            
    print("Notebook shutting down, thank you.")

if __name__ == "__main__":
    main()
