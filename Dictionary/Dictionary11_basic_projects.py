from tabulate import tabulate

data = [
	{"nim":300, "nama":"xin","Prodi":"TI", "SEM":1,"Nilai":60},
	{"nim":400, "nama":"Rin","Prodi":"IF", "SEM":1,"Nilai":70},
	{"nim":500, "nama":"Zin","Prodi":"TI", "SEM":1,"Nilai":80},
	{"nim":600, "nama":"Hin","Prodi":"IF", "SEM":1,"Nilai":60},
	{"nim":700, "nama":"Ain","Prodi":"TI", "SEM":1,"Nilai":90}
	
]

data.pop(1)



def tampilkan(data):
	if not data:
		print("belum ada data ")
		return
	tabel = []
	for mhs in data:
	    tabel.append([
	        mhs["nim"],
	        mhs["nama"],
	        mhs["Prodi"],
	        mhs["SEM"],
	        mhs["Nilai"]
	    ])
	
	print(tabulate(
	    tabel,
	    headers=["NIM", "Nama", "Prodi", "SEM", "Nilai"],
	    tablefmt="simple"))
	
def tambah_data(data):
    nim = int(input("NIM   : "))

    if any(mhs["nim"] == nim for mhs in data):
        print("❌ NIM sudah ada")
        return

    nama = input("Nama  : ")
    prodi = input("Prodi : ")
    sem = int(input("SEM   : "))
    nilai = int(input("Nilai : "))

    data.append({
        "nim": nim,
        "nama": nama,
        "Prodi": prodi,
        "SEM": sem,
        "Nilai": nilai
    })

    print("✅ Data berhasil ditambahkan")

def ubah_data(data):
	nim = int("masukan nim yaang mau diubah")
	
	for mhs in data:
		if mhs['nim'] == nim:
			print("kosongkan jika tidak mau diubah")
			nama = input(f"Nama ({mhs['nama']}): ")
			prodi = input(f"Prodi ({mhs['Prodi']}): ")
			sem = input(f"SEM ({mhs['SEM']}): ")
			nilai = input(f"Nilai ({mhs['Nilai']}): ")
			
			if nama: mhs["nama"] = nama
			if prodi: mhs["Prodi"] = prodi
			if sem: mhs["SEM"] = int(sem)
			if nilai: mhs["Nilai"] = int(nilai)
			
			print(" Data berhasil diubah")
			return
		
		print(" NIM tidak ditemukan")
def hapus_data(data):
    nim = int(input("Masukkan NIM yang ingin dihapus: "))

    for mhs in data:
        if mhs["nim"] == nim:
            data.remove(mhs)
            print("Data berhasil dihapus")
            return

    print("NIM tidak ditemukan")

def menu():
    print("""
=== MENU CRUD MAHASISWA ===
1. Tampilkan Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Keluar
""")

while True:
    menu()
    pilih = input("Pilih menu (1-5): ")

    if pilih == "1":
        tampilkan(data)
    elif pilih == "2":
        tambah_data(data)
    elif pilih == "3":
        ubah_data(data)
    elif pilih == "4":
        hapus_data(data)
    elif pilih == "5":
        print("👋 Program selesai")
        break
    else:
        print("❌ Pilihan tidak valid")