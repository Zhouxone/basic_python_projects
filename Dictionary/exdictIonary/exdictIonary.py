antrian = []

while True:
	print("\n=== SPBU - Antrian Motor ===")
	print("1. Tambah motor")
	print("2. Layani motor")
	print("3. Lihat antrian")
	print("0. Keluar")
	
	pilih = input("Pilih: ")
	
	if pilih == "1":
		motor = input("Masukkan nama/nomor motor: ")
		antrian.append(motor)
		print(f"{motor} masuk antrian.")
	
	elif pilih == "2":
		if antrian:
			dilayani = antrian.pop(0)
			print(f" {dilayani} selesai dilayani.")
		else:
			print(" Antrian kosong!")
	
	elif pilih == "3":
		if antrian:
			print("Antrian:", antrian)
		else:
			print("Antrian kosong.")
	
	elif pilih == "0":
		print(" Sampai jumpa!")
		break
	
	else:
		print("Pilih 0–3 saja.")