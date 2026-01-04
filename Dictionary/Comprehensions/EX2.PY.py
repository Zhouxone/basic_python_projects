#Basic list comprehension
values = []
for x in range(10):
	values.append(x)

values = [x +1  for x in range(10)]
print(values)

#Comprehension Condition
evens = []
for number in range(50):
	is_even =number % 2 == 0
	if is_even:
		evens.append(number)

evens =[x for x in range(50) if x % 2==0]
print(evens)

options = ["any","albhany","apple","world","hello", ""]
valid_strings = []
for string in options:
	if len(string) <= 1:
		continue
	if string[0] !="a":
		continue
	if string[-1] !="y":
		continue
	valid_strings.append(string)
print(valid_strings)

valid_strings = [
	string
	for string in options
	if len(string) >= 2
	if string[0] == "a"
	if string[-1] == "y"
]
print(valid_strings)

#multiple list comprehension
matrix =[[1,2,3], [4,5,6],[7,8,9]]
flattened = []

for row in matrix:
	for num in row:
		flattened.append(num)
		
flattened = [num for row in matrix for num in row]
print(flattened)

#if/else in a comprehensionn
categories  = []

for number in range(10):
	if number % 2 == 0:
		categories.append("Even")
	else:
		categories.append("odd")
print(categories)

categories = [
	"Even" if x % 2 == 0 else "Odd" for x in range(10)
]
print(categories)

