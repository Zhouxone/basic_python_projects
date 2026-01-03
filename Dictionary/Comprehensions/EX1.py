list =['a' , 'b', 'c']
print(list)
list2=[x for x in list]
print(list)
list3 = [x for x in list if x =='a']
print(list3)
list4 = [x for x in range(5)]
print(list4)

list5 = [hex(x) for x in range(5)]
print(list5)

list6 = [hex(x) if x > 0 else"x" for x in range(5)]
print(list6)

list7 = [x * x for x in range(5)]
print(list7)

list8 = [x for x in range(5) if x == 0 or x == 1 ]
print(list8)

list9 = [[1,2,3] ,[4,5,6],[7,8,9]]
print()

list10 = [y for x in list9 for y in x ]
print(list10)

list11 = [c for c in "string"]
print(list11)
print("-".join(list11))

listv = []
for c in "string":
	listv.append(c)
print(listv)