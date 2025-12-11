import datetime
import os
import string
import random
mahasiswa_template = {
	"nama":"nama",
	"nim":"0000000",
	"sks_lulus":0,
	"lahir":datetime.datetime(1111,1,11)
	
}

data_mahasiswa = {}

while True:
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
	
	KEY = ' '.join(random.choice(string.ascii_uppercase) for i in range(6))
	data_mahasiswa.update({KEY:mahasiswa})
	print("-"*20)
	print(f"{'KEY':<6} {'NAMA':<17}{'SKS':<6}{'Lahir':<10}")
	print("-" * 50)
	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa
		
		NAMA = data_mahasiswa[KEY]['nama']
		NIM = data_mahasiswa[KEY]['nim']
		SKS = data_mahasiswa[KEY]['sks_lulus']
		LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
		print(f"{KEY:<6} {NAMA:<17}{SKS:<6}{LAHIR:^10}")
	print("\n")
	is_done = input("mau tambah data lagi? y/n")
	if is_done == "n":
		break
print("akhir dari program,thx")