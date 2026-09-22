#Buat file dengan nama Konstanta_2611531014.py
#Program ini menggunakan konstanta untuk menghitung luas lingkaran
#nama variabel ditambah 4 digit nim terakhir contoh: jari_1014

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1014 = float(input('Masukkan nilai jari-jari: '))
luas_1014 = PI * jari_1014 * jari_1014
print("luas lingkaran dengan jari-jari %.2f adalah %.2f" %(jari_1014, luas_1014))