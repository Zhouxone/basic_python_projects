import heapq

tali = [4, 3, 2, 6]
heapq.heapify(tali)  # ubah jadi heap sekali → O(n)

total = 0
while len(tali) > 1:
    a = heapq.heappop(tali)  # ambil terkecil
    b = heapq.heappop(tali)  # ambil terkecil berikutnya
    jumlah = a + b
    total += jumlah
    heapq.heappush(tali, jumlah)  # masukkan hasil gabungan

print(total)  # → 29



