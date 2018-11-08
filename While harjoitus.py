print("Calculator")
number1 = input("Give the first number: ")
number2 = input("Give the second number: ")
number1 = int(number1)
number2 = int(number2)
end = True

while(end):
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    end = False
    print("(5) Change numbers")
    print("(6) Quit")
    print("Current numbers:",number1,number2,sep=" ")
    selection = input("Please select something (1-6): ")
    selection = int(selection)

    if(selection == 1):
        print("The result is: ",number1+number2)
    elif(selection == 2):
        print("The result is: ",number1-number2)
    elif(selection == 3):
        print("The result is: ",number1*number2)
    elif(selection == 4):
        print("The result is: ",number1/number2)
    elif(selection == 5):
        number1 = int(input("Give the first number: "))
        number2 = int(input("Give the second number: "))
    elif(selection == 6):
        end = False
    else:
        print("Selection was not correct.")
else:
    print("elselausunto.")
print("Thank you!")
