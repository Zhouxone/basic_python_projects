from collections import deque

a = deque([1,2,3,4,5])

print("data sekarang", a)

# add a data
a.append(6)
print("data masuk", 6)
print("data sekarang ", a)

a.append(7)
print("data masuk:", 7)
print("dataa sekarang", a)


out = a.popleft()
print("data keluar", out)
print("datanya sekarang", a)

a.append(9)
print("data masuk:", 9)
print("dataa sekarang", a)
