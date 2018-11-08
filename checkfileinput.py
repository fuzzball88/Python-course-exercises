def checkFiles(userinput):
	try:
		userinput = string(userinput)
		luefilu = open(userinput,"r")
		content = int(luefilu)
		result = content/1000
	except ValueError: #Errors caused by the unsuitable values of variables.
		print("The file contents were unsuitable.")
	except ImportError: 	#Errors associated to importing external modules and library modules.
		print("There seems to be no file with that name.")
	else:
		print("The result was ",result)
file = input("Give the file name: ")
checkFiles(file)
