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
    pass
    """if myAnswer == 1 and aiAnswer == 1:
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
        print("It is a tie!")"""

    
def main():
        wins = 0
        rounds = 0
        ties = 0

        while True:
                string = input("Foot, Nuke or Cockroach?(Quit ends): ")
                if string == "Quit":
                                #return False
                                print("You played ",rounds," rounds, and won ",wins," rounds, playing tie in ",ties," rounds.")
                                break
                elif string == "Foot":
                                rounds += 1
                                myAnswer = 1
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                if myAnswer == 1 and aiAnswer == 1:
                                        print("It is a tie!")
                                        ties += 1

                                elif myAnswer == 1 and aiAnswer == 2:
                                        print("You LOSE!")
        
                                elif myAnswer == 1 and aiAnswer == 3:
                                        print("You WIN!")
                                        wins += 1

                                
                                
                elif string == "Nuke":
                                rounds += 1
                                myAnswer = 2
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                if myAnswer == 2 and aiAnswer == 1:
                                        print("You WIN!")
                                        wins += 1

                                elif myAnswer == 2 and aiAnswer == 2:
                                        print("Both LOSE!")
                                        ties += 1

                                elif myAnswer == 2 and aiAnswer == 3:
                                        print("You LOSE!")
                                        


                elif string == "Cockroach":
                                rounds += 1
                                myAnswer = 3
                                print("You chose: ",string)
                                aiAnswer = aiChooses()
                                if myAnswer == 3 and aiAnswer == 1:
                                        print("You LOSE!")

                                elif myAnswer == 3 and aiAnswer == 2:
                                        print("You WIN!")
                                        wins += 1

                                elif myAnswer == 3 and aiAnswer == 3:
                                        print("It is a tie!")
                                        ties += 1
                else:
                                print("Incorrect selection.")
if __name__ == "__main__":
    main()      

