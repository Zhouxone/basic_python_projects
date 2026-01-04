#Transformation in Compreshension
def square(x):
	  return x**2

def valid(x):
	return x % 2 == 0
squared_numbers =[square(x) for x in range(10) if valid(x)]

print(squared_numbers)

#dictionary comprehension

pairs = [("a",1), ("b",2) ,("c",3)]

my_dict = {k: v for k,v in pairs}
print(my_dict)

#set comprehension

nums = [1,2,2,3,3,4,4,5,5,5]

unique_square = {x**2 for x in nums}
print(unique_square)
# Generator comprehnesion

sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)