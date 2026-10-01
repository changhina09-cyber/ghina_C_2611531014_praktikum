#Buat file dengan nama nested_for4_2611531014.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditam#bah 4 digit nim terakhir contoh: ulang_1014
# Program ini menggunakan fungsi input()

tinggi_1014 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1014 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1014 = tinggi_1014
    c_1014 = a_1014
    lebar_1014 = (2 * tinggi_1014) - 2

    for i_1014 in range(1, tinggi_1014 + 1):
        b_1014 = c_1014 + 1

        for j_1014 in range(1, lebar_1014 + 1):

            # Baris atas dan bawah
            if i_1014 == 1 or i_1014 == tinggi_1014:
                if j_1014 == 1 or j_1014 == lebar_1014:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1014 == 1 or j_1014 == lebar_1014:
                    print("|", end="")
                elif j_1014 == c_1014:
                    print("<", end="")
                elif j_1014 == b_1014:
                    print(">", end="")
                elif j_1014 == lebar_1014 - c_1014:
                    print("<", end="")
                elif j_1014 == lebar_1014 - c_1014 + 1:
                    print(">", end="")
                elif b_1014 < j_1014 < lebar_1014 - c_1014:
                    print(".", end="")
                else:
                    print(" ", end="")

        print()

        a_1014 -= 2
        if a_1014 <= 0:
            c_1014 = (-a_1014) + 2
        else:
            c_1014 = a_1014