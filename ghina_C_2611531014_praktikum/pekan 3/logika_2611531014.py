# Buat file dengan nama logika_2611531014.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1014
# program ini menggunakan fungsi input()
# Program operator logika dalam python

# Memasukkan nilai boolean 
# Input tidak peka terhadap huruf besar dan kecil
a1_1014 = input("Input nilai booelan-1 (true/false): ").strip().lower() == "true"
a2_1014 = input("Input nilai booelan-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_1014)
print("A2 =", a2_1014)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_1014 and a2_1014
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_1014 or a2_1014
print("\nDijungsi (OR)")
print("A1 or A2 =",hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_1014
print("\nNegasi A2 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_1014
print("\nNegasi A2 (NOT)")  
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_1014 != a2_1014
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)