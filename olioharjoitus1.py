class Player:
    teamcolor = ""
    points = 0
	
    def printout(self):
        print("The ",self.teamcolor," contender has ",self.points," points!")

def main():
    blueteam = Player()
    blueteam.teamcolor = "blue"
    blueteam.points = 300
    blueteam.printout()

if __name__ == "__main__":
	main()
