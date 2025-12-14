data = {
	"name":"rin" , "job": "It guy"
}


def intro():
	print("welkam")
	print("enter your password")
	enter_password()
def enter_password():
	password = "12345"
	x = input("password:")
	if (len(x)<3 and (x != password)):
		print("acess denied")
	else:
		print("acess granted")
		data_base()

def data_base():
	x = int(input("clear(1),update(2),print(3)"))
	if x == 1:
			data.clear()
			print(data)
			print("cleared")
	elif x ==2:
			update_dictionary()
	elif x == 3:
			print(data)

def update_dictionary():
		name = input("input namanya")
		job = input("Enter job")
		data["name"] = name
		data["job"] = job
		print("data update")
		print(data)
intro()