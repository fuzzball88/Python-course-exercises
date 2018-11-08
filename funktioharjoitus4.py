def tester(givenstring = "Too short"):
	string = "too short"
	if len(givenstring) < 10:
		print(string)
	elif len(givenstring) >= 10:
		print(givenstring)
		if "X" in givenstring:
			return True
	
	

def main():
	end = True
	while(end):
		string = input("Write something(quit ends): ")
		if string == "quit":
			return False
		else:
			checkx = tester(string)
			if checkx == True:
				print("X spotted!")
if __name__ == "__main__":
    main()		
