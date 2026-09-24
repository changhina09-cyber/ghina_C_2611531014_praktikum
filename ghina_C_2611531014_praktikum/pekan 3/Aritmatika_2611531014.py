# Buat file dengan nama aritmatika_2611531014.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1014 = int(input("input angka-1:"))
angka2_1014 = int(input("input angka-2:"))

# Penjumlahan
hasil = angka1_1014 + angka2_1014
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

# Pengurangan 
hasil = angka1_1014 - angka2_1014
print("\nOperator Pengurangan")
print("Hasil =", hasil)

# Perkalian 
hasil = angka1_1014 * angka2_1014
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1014 != 0:
    hasil = angka1_1014 / angka2_1014
    print("\nOperator Pembagian")
    print("Hasil=", hasil)

    hasil = angka1_1014 // angka2_1014
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_1014 % angka2_1014
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil = angka1_1014 ** angka2_1014
print("\nOperator Pangkat")
print("Hasil =", hasil)