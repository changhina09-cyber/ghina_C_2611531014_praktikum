# Buat file dengan nama tugas5_2611531014.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1014
# Program ini menggunakan fungsi input()

print(" === JAM PASIR KRISTAL PALINDROMIK ===")

n_1014 = int(input("Masukkan ukuran skala jam pasir (N):"))

# Border atas
for pagar_1014 in range(1):
    print("#", end="")

    for garis_1014 in range(4 * n_1014 + 5):
        print("=", end="")

    print("#")

# Fase 1: Jam pasir bagian atas
for baris_1014 in range(n_1014, 0, -1):
    print("|", end="")

    # Spasi penyeimbang kiri
    for spasi_1014 in range(2 * n_1014 + 1 - baris_1014):
        print(" ", end="")

    # Deret angka menurun
    for angka_1014 in range(baris_1014, 0, -1):
        print(angka_1014, end="")

    # Poros kristal
    print("<*>", end="")

    # Deret angka menaik
    for angka_1014 in range(1, baris_1014 + 1):
        print(angka_1014, end="")

    # Spasi penyeimbang kanan
    for spasi_1014 in range(2 * n_1014 + 1 - baris_1014):
        print(" ", end="")

    print("|")

# Fase 2: Titik pusat
print("|", end="")

for spasi_1014 in range(2 * n_1014 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_1014 in range(2 * n_1014 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bagian bawah
for baris_1014 in range(1, n_1014 + 1):
    print("|", end="")

    # Spasi penyeimbang kiri
    for spasi_1014 in range(2 * n_1014 + 1 - baris_1014):
        print(" ", end="")

    # Deret angka menurun
    for angka_1014 in range(baris_1014, 0, -1):
        print(angka_1014, end="")

    # Poros kristal
    print("<*>", end="")

    # Deret angka menaik
    for angka_1014 in range(1, baris_1014 + 1):
        print(angka_1014, end="")

    # Spasi penyeimbang kanan
    for spasi_1014 in range(2 * n_1014 + 1 - baris_1014):
        print(" ", end="")

    print("|")

# Border bawah
for pagar_1014 in range(1):
    print("#", end="")

    for garis_1014 in range(4 * n_1014 + 5):
        print("=", end="")

    print("#")