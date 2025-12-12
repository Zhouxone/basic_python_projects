n = int(input("masukan jumlah mahasiswa = "))

daftar = []
for i in range(1,n+1):
	print(f"Data mahasiswa ke -{i}")
	nama = str(input("Nama panggilan ="))
	nilai = int(input("Nilai mahasiswa="))
	daftar.append({"nama":nama, "nilai":nilai})

print("Daftar Mahasiswa dan Nilainya =")
for mhs in daftar:
	print(f"{mhs['nama']}: {mhs['nilai']}")
	
print("daftar mahasiswa yang lulus")
for mhs in daftar:
	if mhs["nilai"] >=70:
		print(f"{mhs['nama']} selamat anda lulus")
	elif mhs["nilai"] <=45:
		print(f"{mhs['nama']} maaf anda tidak lulus mohon berusaha lagi")
	else:
		print(f"nilai tidak mencukupi silahkan remedial\n{mhs['nilai']}")