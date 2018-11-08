def poweroftwo(number):
	result = 2**number
	return result
def main():
	number = int(input("Give a number: "))
	result = poweroftwo(number)
	print("The result is ",result)
if __name__ == "__main__":
    main()
