try:
    file = open("data.txt")
    data = int(file.readline())
except FileNotFoundError:
    print("File tidak ditemukan.")
except ValueError:
    print("Isi file bukan angka.")