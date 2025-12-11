#copy & Pop Dictionary
dta_dict = {
	"xin":"xinzero",
	"kao":"kaozero",
	"viu":"viuzero",
	"hao":"haozero",
}

myprend = dta_dict.copy()

print(f"this is myprend={dta_dict}\n")
print(f"prend:{myprend}\n")

dta_dict["xin"] ="xin rupanya adalah orang eropa"

print(f"this is myprend={dta_dict}\n")
print(f"prend:{myprend}\n")


#pop dictionary

dataA = dta_dict.pop("xin")
print(dataA)
print(dta_dict)


#pop item dictionary

dataTerakhir = dta_dict.popitem()
print(f"dta terakhir adalah = {dataTerakhir}\n")