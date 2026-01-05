# CARA membaca file eksternal


print(3*"=", "membaca file txt", 3*"=")
file = open("xiaohui.txt",mode="r")
print(f"status read: {file.readable()}")
print(f"status write : {file.writable()}")


#baca seluruh baris
#print(file.read())

print(file.readline(),end="")
print(file.readline(),end="")

# baca semua baris sebagai list
print(file.readlines())


print(f"apakah file sudash di close>?:{file.closed}")
file.close()

print(f"apakah file sudash di close>?:{file.closed}")
print(3*"=", "membaca file txt dengan with", 3*"=")

with open("xiaohui.txt",mode="r") as file:
	content = file.readline()
	print(content,end="")
	print(f"apakah file sudah diclose:{file.closed}")
print(f"apakah file sudah diclose:{file.closed}")

