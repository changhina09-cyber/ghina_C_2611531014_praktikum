# Buat file dengan nama perulangan_for3_2611531014.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1014
# Program ini menggunakan fungsi input()

ulang_1014 = int(input("Masukkan jumlah perulangan: "))

jumlah_1014 = 0
for i_1014 in range(1, ulang_1014+1):
    print(i_1014, end="")
    jumlah_1014 = jumlah_1014 + i_1014

    if i_1014 < ulang_1014:
        print("+", end="")
    else:
        print("=", jumlah_1014, end="")
print()
print("jumlah =", jumlah_1014)