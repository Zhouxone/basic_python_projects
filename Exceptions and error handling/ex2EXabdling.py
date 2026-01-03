try:
	number = int(input("enter a number"))
	print(1/number)
except ZeroDivisionError:
	print("you cnt dvd By ZeRo id0t")
except ValueError:
	print("Something went wrong !")
finally:
	print("do some cleanup here")