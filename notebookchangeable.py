# -*- coding: cp1252 -*-
import time

def checkNoteBook(notebookname = "notebook.txt"):
        try:
            notebook = open(notebookname,"a")
            print("No default notebook was found, created one.")
            notebook.close()
        except IOError:
            print()

def changeNoteBook(notebookname = "notebook.txt"):
        try:
            notebookname = open(notebookname,"r")
        except IOError:
            print("No notebook with that name detected, created one.")
            notebookname = open(notebookname,"a")

def main():
    checkNoteBook()
    filename = checkNoteBook
    while True:     
        print("Now using file",filename)
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Change the notebook")
        print("(5) Quit")
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
