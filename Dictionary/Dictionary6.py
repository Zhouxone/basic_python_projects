import datetime
import os
mahasiswa_template = {
	"nama":"nama",
	"nim":"0000000",
	"sks_lulus":0,
	"lahir":datetime.datetime(1111,1,11)
	
}

data_mahasiswa = {}
os.system("cls")
print(f"{'WELCOME':^6}")
print(f"{'DATA MAHASISWA':^6}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("input nama Mahasiswa=")
mahasiswa['nim'] = input("input nim Mahasiswa=")
mahasiswa['sks_lulus'] = int(input("input sks_lulus Mahasiswa="))
TAHUN_LAHIR = int(input("Tahun Lahir(YYYY)="))
BULAN_LAHIR = int(input("BULAN Lahir(1-12)="))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31)="))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print("-\n"*5)
print(f"{'DATA MAHASISWA':^6}")
for i , y in mahasiswa.items():
	print(f"{i} = {y}")