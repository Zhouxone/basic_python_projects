from tabulate import tabulate

data = [
    {"nim":300, "nama":"Xin","Prodi":"TI", "SEM":1,"Nilai":60},
    {"nim":400, "nama":"Rin","Prodi":"IF", "SEM":1,"Nilai":70},
    {"nim":500, "nama":"Zin","Prodi":"TI", "SEM":1,"Nilai":80},
    {"nim":600, "nama":"Hin","Prodi":"IF", "SEM":1,"Nilai":60},
    {"nim":700, "nama":"Ain","Prodi":"TI", "SEM":1,"Nilai":90}
]
def knilai(nilai):
	if 85 <= nilai <= 100:
		return "A"
	if 80 <= nilai <= 84:
		return "A-"
	if 75 <= nilai <= 79:
		return "B+"
	if 70 <= nilai <= 74:
		return "B"
	if 65 <= nilai <= 69:
		return "D"
	if 60 <= nilai <= 64:
		return "c+"
	if 50 <= nilai <= 59:
		return "c"
	if 40 <= nilai <= 49:
		return "c"
	if 0 <= nilai <= 39:
		return "e"
	
for mhs in data:
	mhs["Prestasi"] = knilai(mhs["Nilai"])

tabel = []
for mhs in data:
	tabel.append([
		mhs["nim"],
		mhs["nama"],
		mhs["Prodi"],
		mhs["SEM"],
		mhs["Nilai"],
		mhs["Prestasi"]
])
print(tabulate(tabel,headers=["NIM","NAMA","PRODI","SEM","NILAI","PRESTASI"],tablefmt="grid"
    ))






