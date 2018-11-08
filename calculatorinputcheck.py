import math

def getNumber1():
    while True:
        try:
            number1 = input("Give the first number: ")
            number1 = int(number1)
            return number1
        except Exception:
            print("This input is invalid.")

def getNumber2():
    while True:
        try:
            number2 = input("Give the second number: ")
            number2 = int(number2)
            return number2
        except Exception:
            print("This input is invalid.")
def main():
    print("Calculator")
    number1 = getNumber1()
    number2 = getNumber2()
    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5)sin(number1/number2)")
        print("(6)cos(number1/number2)")
        print("(7) Change numbers")
        print("(8) Quit")
        print("Current numbers:",number1,number2,sep=" ")
        selection = input("Please select something (1-8): ")
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
            print("The result is: ", math.sin(number1/number2))
        elif(selection == 6):
            print("The result is: ", math.cos(number1/number2))
        elif(selection == 7):
            number1 = int(input("Give the first number: "))
            number2 = int(input("Give the second number: "))
        elif(selection == 8):
            break
        else:
            print("Selection was not correct.")
    print("Thank you!")
if __name__ == "__main__":
    main()
