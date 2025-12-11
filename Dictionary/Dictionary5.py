#Multim keys dan Nesting directory
import datetime
mahasiswa1 = {
	"nama":"xin",
	"nim":"19292929",
	"sks_lulus":130,
	"beasiswa":False,
	"Lahir":datetime.datetime(2007,9,9)
}


mahasiswa2 = {
	"nama":"viuhero",
	"nim":"19292929",
	"sks_lulus":140,
	"beasiswa":True,
	"Lahir":datetime.datetime(2007,10,9)
}

mahasiswa3 = {
	"nama":"zxhero",
	"nim":"19292929",
	"sks_lulus":100,
	"beasiswa":False,
	"Lahir":datetime.datetime(2000,10,9)
}

data_mahasiswa = {
	"MAH001":mahasiswa1,
	"MAH002":mahasiswa2,
	"MAH003":mahasiswa3,
	
}

print(f"{'KEY':<6} {'NAMA':<17}{'SKS':<6}{'Beasiswa':<10}{'Lahir':<10}")
print("-"*50)

for mhs in data_mahasiswa:
	KEY = mhs
	
	NAMA = data_mahasiswa[KEY]['nama']
	NIM = data_mahasiswa[KEY]['nim']
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x")
	
	print(f"{KEY:<6} {NAMA:<17}{SKS:<6}{BEASISWA:^10}{LAHIR:^10}")
