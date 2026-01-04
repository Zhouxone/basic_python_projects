#building a 3D list
import pprint

printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
	l1 = []
	for b in range(5):
		l2 = []
		for num in range(5):
			l2.append(num)
		l1.append(l2)
	lst.append(11)
printer.pprint(lst)

lst = [
    [
        [num for num in range(5)]   # payload list
        for b in range(5)            # 5 port
    ]
    for a in range(5)                # 5 host
]

printer.pprint(lst)