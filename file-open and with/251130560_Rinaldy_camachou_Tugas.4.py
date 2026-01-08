
# Penjelasan perbedaan BST dan Balanced Tree + Penggunaan mode akses file

def tulis_penjelasan_ke_file():
    # Menulis penjelasan ke file "Tugas 4.txt" menggunakan mode 'w'
    with open("Tugas 4.txt", "w", encoding="utf-8") as file:
        file.write("Perbedaan Binary Search Tree dan Balanced Tree\n\n")
        file.write("1. Definisi:\n")
        file.write("   - Binary Search Tree (BST): Struktur data pohon biner di mana setiap simpul memiliki nilai, dan untuk setiap simpul:\n")
        file.write("        * Semua nilai di subtree kiri lebih kecil dari nilai simpul tersebut.\n")
        file.write("        * Semua nilai di subtree kanan lebih besar dari nilai simpul tersebut.\n")
        file.write("     BST tidak menjamin keseimbangan tinggi pohonnya.\n\n")
        file.write("   - Balanced Tree: Jenis pohon biner yang secara otomatis menjaga keseimbangan tinggi antara subtree kiri dan kanan. Contohnya: AVL Tree, Red-Black Tree.\n")
        file.write("     Tujuannya agar operasi pencarian, penyisipan, dan penghapusan tetap efisien (O(log n)) bahkan pada kasus terburuk.\n\n")
        file.write("2. Kinerja:\n")
        file.write("   - BST: Dalam kasus terbaik (pohon seimbang), operasi berjalan dalam O(log n). Namun, dalam kasus terburuk (misalnya, data dimasukkan secara terurut), pohon bisa menjadi seperti linked list → O(n).\n")
        file.write("   - Balanced Tree: Selalu mempertahankan keseimbangan, sehingga kompleksitas operasi tetap O(log n) dalam semua kasus.\n\n")
        file.write("3. Rotasi:\n")
        file.write("   - BST: Tidak melakukan rotasi atau penyesuaian struktur setelah penyisipan/penghapusan.\n")
        file.write("   - Balanced Tree: Melakukan rotasi (single/double) untuk menjaga keseimbangan setelah operasi modifikasi.\n\n")
        file.write("4. Contoh Penerapan:\n")
        file.write("   - BST: Cocok untuk aplikasi sederhana dengan data acak dan tidak terlalu besar.\n")
        file.write("   - Balanced Tree: Digunakan di database, sistem file, dan aplikasi yang membutuhkan performa stabil (misalnya: std::map di C++, TreeMap di Java).\n\n")
        file.write("5. Kesimpulan:\n")
        file.write("   Balanced Tree adalah evolusi dari BST yang menyelesaikan masalah ketidakseimbangan, sehingga memberikan performa yang lebih konsisten dan andal dalam skenario real-world.\n\n")
        file.write("---\n")
        file.write("Mode Akses File Python yang Digunakan:\n\n")
        file.write("1. 'w' (write): Membuka file untuk menulis. Jika file sudah ada, isi file akan dihapus (overwrite). Jika tidak ada, file baru dibuat.\n")
        file.write("2. 'a' (append): Membuka file untuk menambahkan konten di akhir file. Jika file tidak ada, akan dibuat.\n")
        file.write("3. 'r' (read): Membuka file hanya untuk membaca. Error jika file tidak ada.\n")
        file.write("4. 'r+' (read and write): Membuka file untuk membaca dan menulis. Pointer di awal file.\n")
        file.write("5. 'w+' (write and read): Membuka file untuk menulis dan membaca. Jika file ada, isi dihapus. Jika tidak ada, dibuat.\n")
        file.write("6. 'a+' (append and read): Membuka file untuk menambahkan dan membaca. Pointer di akhir file.\n\n")
        file.write("Contoh penggunaan dalam kode Python:\n")
        file.write("- Untuk menulis penjelasan ke file: gunakan mode 'w'\n")
        file.write("- Untuk menambahkan catatan tambahan: gunakan mode 'a'\n")
        file.write("- Untuk membaca ulang isi file: gunakan mode 'r'\n\n")
        file.write("---\n")
        file.write("Ditulis oleh: 251130560_Rinaldy_camachou_Tugas 4.py\n")
        file.write("Tanggal: Selasa, 06 Januari 2026\n")

def baca_dan_tampilkan_file():
    # Membaca isi  dengan  menggunakan mode 'r'
    try:
        with open("Tugas 4.txt", "r", encoding="utf-8") as file:
            print("Isi file 'Tugas 4.txt':\n")
            print(file.read())
    except FileNotFoundError:
        print("File 'Tugas 4.txt' belum dibuat. Jalankan fungsi tulis_penjelasan_ke_file() terlebih dahulu.")

def tambah_catatan():
    # Menambahkan catatan tambahannya dengan  menggunakan mode 'a'
    with open("Tugas 4.txt", "a", encoding="utf-8") as file:
        file.write("\n\nCatatan Tambahan:\n")
        file.write("Mode 'a' sangat berguna jika ingin menambahkan informasi tanpa menghapus isi file sebelumnya.\n")

# Eksekusi utama
if __name__ == "__main__":
    print("Menjalankan penulisan penjelasan ke file...")
    tulis_penjelasan_ke_file()
    print("Penjelasan telah ditulis ke 'Tugas 4.txt'.\n")

    # Baca dan tampilkan isi file
    baca_dan_tampilkan_file()

    # Tambahkan catatan (contoh penggunaan mode 'a')
    print("\nMenambahkan catatan tambahan...")
    tambah_catatan()
    print("Catatan tambahan telah ditambahkan.\n")

    # Tampilkan ulang isi file setelah penambahan
    baca_dan_tampilkan_file()