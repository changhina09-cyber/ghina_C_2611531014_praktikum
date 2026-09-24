# Buat file dengan nama Assingment_2611531014.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_1014 = int(input("Input angka-1: "))
angka2_1014 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_1014)
print("Nilai angka2 =", angka2_1014)

# Assingment biasa 
hasil = angka1_1014
print("\nAssignment baisa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_1014
hasil += angka2_1014
print("nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assingment pengurangan
hasil = angka1_1014
hasil -= angka2_1014
print("nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assingment perkalian
hasil = angka1_1014
hasil *= angka2_1014
print("nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assingment pembagian, pembagian bulat, dan sisa bagi
if angka2_1014 != 0:
    hasil = angka1_1014
    hasil /= angka2_1014
    print("nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_1014
    hasil //= angka2_1014
    print("nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_1014
    hasil %= angka2_1014
    print("nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)     
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_1014
hasil **= angka2_1014
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)