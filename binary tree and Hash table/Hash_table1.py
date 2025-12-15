def Hashing(keys, panjangArray):# pembuatan fungsi hashing
	ttl = 0
	for i in range(len(keys)):
		ttl = ttl + ord(keys[i])
	return ttl % panjangArray
panjang = 10
hash_table = [None] * panjang

ind = Hashing("rin", panjang)
hash_table[ind] = 100
print(f"nilai rin adalah {hash_table[ind]}")
ind = Hashing("Yanto", panjang)
hash_table[ind] = 90
print(f"nilai yanto adalah {hash_table[ind]}")
print("\n Hash Table setelah 2 data masuk:")
print(hash_table)


