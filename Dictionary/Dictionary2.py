# operator dictionary

dta_dict = {
	"xin":"xin zero",
	"vir":"viu zero",
	"sin":"sin zero",
}

LENDICT = len(dta_dict)

print(LENDICT)
print(f"panjang dictinary {LENDICT}")

#menegecek key exist/tidak
KEY ="xin"
CHECKKEY = KEY in dta_dict
print(f"apakah ada data di dta_dict =  {CHECKKEY}")

KEY1 ="miao"
CHECKKEY1 = KEY1 in dta_dict
print(f"apakah ada data di dta_dict =  {CHECKKEY1}")

#mengakses value
print(dta_dict["xin"])
print(dta_dict.get("xin"))
print(dta_dict.get("error","key tydack ditemukan"))

# mengupdate data
dta_dict["xin"] = "xin adalah orang eropa"
print(dta_dict)
dta_dict["ahao"] = "ahao adalah orang eropa ke 2"
print(dta_dict)
dta_dict.update({"xin":"xin zero"})
print(dta_dict)
dta_dict.update({"zao":"zao zero"})
print(dta_dict)

#mendelate data dari dictionary
print(dta_dict)