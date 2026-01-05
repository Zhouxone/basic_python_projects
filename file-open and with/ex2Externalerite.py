with open("romeo.txt","w",encoding="utf-8") as file:
	file.write("xixixixixiixxixix")
with open("romeo.txt","w",encoding="utf-8") as file:
	file.write("xxoxoxoxooxoxox")
	
	
	
with open("romeo2.txt","w",encoding="utf-8") as file:
	file.write("xixixixixiixxixix\n")
with open("romeo2.txt","a",encoding="utf-8") as file:
	file.write("haohao")
#mode r+
with open("romeo2.txt","w",encoding="utf-8") as file:
	file.write("data ke 3\n")

with open("romeo2.txt","r+",encoding="utf-8") as file:
	file.write("baris 1\n")
with open("romeo2.txt","r+",encoding="utf-8") as file:
	data = file.read()
	print(data)
	
with open("romeo2.txt","r+",encoding="utf-8") as file:
	file.write("baris-3\n")


