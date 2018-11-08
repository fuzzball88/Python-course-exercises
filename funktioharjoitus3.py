def tester(givenstring = "Too short"):
	print(givenstring)

def main():
	end = True
	while(end):
		string = input("Write something(quit ends): ")
		if string == "quit":
			return False
		elif len(string) < 10:
			tester()
		else:
			tester(string)
if __name__ == "__main__":
    main()		
