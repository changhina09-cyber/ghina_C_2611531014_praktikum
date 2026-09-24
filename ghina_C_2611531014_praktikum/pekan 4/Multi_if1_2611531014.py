# Buat file dengan nama multi_if1_2611541014.py
# Buat program untuk kondisi if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1014
# Program ini menggunakan fungsi input()

umur_1014 = int(input("Masukkan umur Anda: "))
sim = input("Apakah Anda Sudah punya Sim C (y/t): ")[0]

if umur_1014 >= 17 and sim == "y":
    print("Anda Sudah Dewasa dan boleh mengendarai motor")

if umur_1014 >= 17 and sim != "y":
    print("Anda Sudah Dewasa tetapi tidak boleh mengendarai motor")

if umur_1014 < 17 and sim == "y":
    print("Anda belum cukup umur punya SIM")

if umur_1014 < 17 and sim != "y":
    print("Anda belum cukup umur bawa motor")