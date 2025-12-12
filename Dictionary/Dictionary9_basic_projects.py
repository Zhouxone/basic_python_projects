daftar_buku = {
	"Pemogramaan Python":{"harga":55000, "Stok":10},
	"Pemograman Javascript":{"harga":100000, "Stok":5},
	"Pemograman bash":{"harga":150000, "Stok":20},
	"Malware development":{"harga":190000, "Stok":30},
	"Cyber Security":{"harga":190000, "Stok":30}
}

def tabel():
	print("="*60)
	print(f"| {'Nama Buku':<30} | {'harga Buku':<20} | {'stock Buku':<9}|")
	print("="*60)

	for nama, info in daftar_buku.items():
		harga = f"Rp. {info['harga']:,}"
		stok = info["Stok"]
		print(f"{nama:<30} | {harga:<20} | {stok:<9} | ")
	print("="*60)
tabel()


cari_buku =input("mana buku yang anda mau=")


if cari_buku in daftar_buku:
	x = daftar_buku[cari_buku]
	print(f"Hasil pencarian {cari_buku} dan harganya Rp{x['harga']:,} ini buku yang kamu cari masik ada {x['Stok']}")
else:
	print("\nMaaf buku yang Anda cari tidak ditemukan")