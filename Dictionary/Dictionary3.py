# looping dictionary

dta_dict = {
	"xin":"xinzero",
	"vao":"vaozero",
	"hao":"haozero",
	"khao":"khaozero",
	
}

for x in dta_dict:
	print(x)
# operator untk mengambil item

k = dta_dict.keys()
print(k)

for k in dta_dict.keys():
	print(k)
for k in dta_dict.keys():
	print(dta_dict.get(k))

values = dta_dict.values()
print(values)

items = dta_dict.items()
print(items)

for i in dta_dict.items():
	print(i)

for k, v  in dta_dict.items():
	print(f"k ={k} , v = {v}")