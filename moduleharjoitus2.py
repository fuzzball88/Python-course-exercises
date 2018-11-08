import random


#Makes the Ai choose its one
def aiChooses():
        aiGuess = random.randint(1,3)
        if aiGuess == 1:
            aiChoose = "Foot"
        elif aiGuess == 2:
            aiChoose = "Nuke"
        elif aiGuess == 3:
            aiChoose = "Cockroach"
        print("Computer chose: ",aiChoose)
        return aiGuess
        checkScore()
       

def checkScore(myAnswer = None,aiAnswer = None):
    if myAnswer == 1 and aiAnswer == 1:
        print("It is a tie!")

    elif myAnswer == 1 and aiAnswer == 2:
        print("You LOSE!")
        
    elif myAnswer == 1 and aiAnswer == 3:
        print("You WIN!")

    elif myAnswer == 2 and aiAnswer == 1:
        print("You LOSE!")

    elif myAnswer == 2 and aiAnswer == 2:
        print("Both LOSE!")

    elif myAnswer == 2 and aiAnswer == 3:
        print("You WIN!")

    elif myAnswer == 3 and aiAnswer == 1:
        print("You LOSE!")

    elif myAnswer == 3 and aiAnswer == 2:
        print("You WIN!")

    elif myAnswer == 3 and aiAnswer == 3:
        print("It is a tie!")

    
def main():
        wins = 0
        rounds = 0
        draws = 0

        while True:
                string = input("Foot, Nuke or Cockroach?(quit ends): ")
                if string == "quit":
                                #return False
                                break
                elif string == "Foot":
                                myAnswer = 1
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                checkScore(int(myAnswer),int(aiAnswer))
                elif string == "Nuke":
                                myAnswer = 2
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                checkScore(int(myAnswer),int(aiAnswer))
                elif string == "Cockroach":
                                myAnswer = 3
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                checkScore(int(myAnswer),int(aiAnswer))
                else:
                                print("Incorrect selection.")
if __name__ == "__main__":
    main()      

