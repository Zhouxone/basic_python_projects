print("Testing 1")

try:
    f = open("cscscscscc")
except:
    print("the file does not exists")
try:
    f = open("adadad")
except FileNotFoundError:
    print("the file does not exist")
except Exception as e:
    print(e)
finally:
    print("this message")

n = 0
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int")
print(1/n)

n = 0
assert(n != 0)
print(1/n)