# Buat file dengan nama lainnya_2611531014.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()
# Program operator keanggotaan dan indentitas

print("=================================")
print("1. OPERATOR KEANGGOTAAN")
print("=================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1014 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1014= [int(angka_1014.strip()) for angka_1014 in input_data_1014.split(",")]

nilai_dicari_1014 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1014= nilai_dicari_1014 in data_1014
print("\nOperator keanggotaan IN")
print(nilai_dicari_1014, "in", data_1014, "=", hasil_1014)

# Operator not in
hasil_1014 = nilai_dicari_1014 not in data_1014
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1014, "in", data_1014, "=", hasil_1014)


print("=================================")
print("2. OPERATOR IDENTITAS")
print("=================================")

# objek1 menggunakan list dari input pengguna
objek1_1014 = data_1014

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1014 = objek1_1014

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1014 = data_1014.copy()

print("objek1 =", objek1_1014)
print("objek2 =", objek2_1014)
print("objek3 =", objek3_1014)

# Operator is 
hasil = objek1_1014 is objek2_1014
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil)

# Operator is not
hasil = objek1_1014 is not objek3_1014
print("\nOperator identitas IS NOT")    
print("objek1 is not objek3 =", hasil)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai")
print("objek1 is objek3 =", objek1_1014 is objek3_1014)
print("objek1 == objek3 =", objek1_1014 == objek3_1014)