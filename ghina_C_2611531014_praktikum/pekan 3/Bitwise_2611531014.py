# Buat file dengan nama bitwise_2611531014.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()

print("\n============================")
print("3. OPERATOR BITWISE")
print("==============================")

angka1_1014 = int(input("Masukkan angka bitwise-1: "))
angka2_1014 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1014, "| biner =", bin(angka1_1014))
print("angka2 =", angka2_1014, "| biner =", bin(angka2_1014))

# Bitwise AND
hasil = angka1_1014 & angka2_1014
print("\nBitwise AND (&)")
print(angka1_1014, "&", angka2_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_1014 | angka2_1014
print("\nBitwise OR (|)")
print(angka1_1014, "|", angka2_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_1014 ^ angka2_1014
print("\nBitwise XOR (^)")
print(angka1_1014, "^", angka2_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_1014
print("\nBitwise NOT (~)")
print("~", angka1_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser_1014 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_1014 << jumlah_geser_1014
print("\nBitwise geser kiri (<<)")
print(angka1_1014, "<<", jumlah_geser_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_1014 >> jumlah_geser_1014
print("\nBitwise geser kanan (>>)")
print(angka1_1014, ">>", jumlah_geser_1014, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)=", format(hasil, "08b"))