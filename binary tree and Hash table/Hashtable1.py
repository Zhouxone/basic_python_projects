def Hashing(keys, panjangArray):# pembuatan fungsi hashing
	ttl = 0
	for i in range(len(keys)):
		ttl = ttl + ord(keys[i])
	return ttl % panjangArray
panjang = 10
hash_table = [None] * panjang

ind = Hashing("rin", panjang)
hash_table[ind] = 100

ind = Hashing("Yanto", panjang)
hash_table[ind] = 90

print("\Hash Table setelaha 2 data masuk:")
print(hash_table)

ind = Hashing("rin", panjang)
print(hash_table[ind])