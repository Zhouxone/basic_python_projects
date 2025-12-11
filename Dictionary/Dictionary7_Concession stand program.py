menu = {
	"pizaa": 3.00,
	"nachos":4.50,
	"popcorn": 9.00,
	"fries": 7.00,
	"hanbao": 5.00
}

cart = []
total = 0
print("----------MENU-----------")
for k, value in menu.items():
	print(f"{k:19}:  ${value:.2f}")
print("----------------------------")

while True:
	food = input("select an item (q to quit)=").lower()
	if food == "q":
		break
	elif menu.get(food) is not None:
		cart.append(food)
	else:
		print("NOT IN MENU")
		
print("---YOUR Chart-------")
for food in cart:
	total += menu.get(food)
	print(food, end=" ")
print()
print(f"Total is :${total:.2f}")