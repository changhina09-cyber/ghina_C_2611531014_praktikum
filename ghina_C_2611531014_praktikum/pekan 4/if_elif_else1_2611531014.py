# Buat file dengan nama if_elif_else1_2611531014.py
# Buat program untuk kondisi if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1014
# Program ini menggunakan fungsi input()

umur_1014 = int(input("Input umur anda: "))
sim_1014 = input("Apakah Anda sudah punya sim C: ")[0]

if umur_1014 >= 17 and sim_1014 == "y":
    print("Anda sudah dewasa dan boleh mengendarai motor")
elif umur_1014 >= 17 and sim_1014 != "y":
    print("Anda sudah dewasa tetapi tidak boleh mengendarai motor")
elif umur_1014 < 17 and sim_1014 == "y":
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")