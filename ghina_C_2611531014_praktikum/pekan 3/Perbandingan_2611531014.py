# Buat file dengan nama Perbandingan_2611531014.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam python

angka1_1014 = int(input("input angka-1: "))
angka2_1014 = int(input("input angka-2: "))

# Lebih besar dari 
hasil = angka1_1014 > angka2_1014
print("\nOperator lebih besar dari")
print("angka1 > angka2 =", hasil)

# Lebih kecil dari
hasil = angka1_1014 < angka2_1014
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =", hasil)

# Lebih besar dari atau sama dengan 
hasil = angka1_1014 >= angka2_1014
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_1014 <= angka2_1014
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil)

# Sama dengan
hasil = angka1_1014 == angka2_1014
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil)

# Tidak sama dengan 
hasil = angka1_1014 != angka2_1014
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil)

# Tambahan: perbandingan berantai dalam python
hasil = 0 < angka1_1014 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil)

hasil = 0 < angka2_1014 < 100
print("0 < angka2 < 100 =", hasil)