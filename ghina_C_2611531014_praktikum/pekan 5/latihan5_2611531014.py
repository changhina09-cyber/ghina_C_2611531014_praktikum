# Buat file dengan nama latihan5_2611531014.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1014
# Program ini menggunakan fungsi input()

tinggi_1014 = int(input("Masukkan tinggi segitiga: "))

for i_1014 in range(1, tinggi_1014 + 1):
    print(" " * (tinggi_1014 - i_1014), end="")
    print("* " * i_1014)