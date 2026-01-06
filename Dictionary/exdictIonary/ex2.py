
mahasiswa_db = {}
def tambah_mahasiswa(nim, nama, prodi):
    mahasiswa_db[nim] = {"nama": nama, "prodi": prodi}
    print("Data mahasiswa berhasil ditambahkan.")

def cari_mahasiswa(nim):
    if nim in mahasiswa_db:
        data = mahasiswa_db[nim]
        print("Data Mahasiswa Ditemukan:")
        print(f"NIM  : {nim}")
        print(f"Nama : {data['nama']}")
        print(f"Prodi: {data['prodi']}")
    else:
        print(f"Data mahasiswa dengan NIM tersebut tidak ditemukan.")


tambah_mahasiswa(231110123, "Ryutaro", "Teknik Alam Ghoib")
tambah_mahasiswa(231121011, "Takumi", "Teknik Informatika")
tambah_mahasiswa(200100001, "Godai", "Arkeologi")

print()

cari_mahasiswa(200100001)
print()
cari_mahasiswa(231401999)