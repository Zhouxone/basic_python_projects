import json

data = {
	"name":"spongeob",
	"age": 30,
	"job":"cook"
}

try:
	with open("rin2.json","x") as file:
		json.dump(data, file, indent=4)
		print(f"file json sudah dibuat")
except FileExistsError:
		print("that file already exists!")