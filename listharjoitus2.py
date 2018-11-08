list = []
while True:
    print("Would you like to")
    print("(1)Add or")
    print("(2)Remove items or")
    print("(3)Quit?: ")
    action = int(input(" "))

    if(action == 1):
        list.append(input("What will be added?: "))
        
    elif(action == 2):
        print("There are ",len(list)," items in the list.")
        selection = int(input("Which item is deleted?: "))
        try:
            list.pop(selection)
        except IndexError:
            print("Incorrect selection.")
            
            
    elif(action == 3):
        print("The following items remain in the list: ")
        for i in list:
            print(i)
        break
            
    else:
        print("Incorrect selection.")
