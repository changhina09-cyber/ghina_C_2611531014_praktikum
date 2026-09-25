# Tugas pekan 3 
# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("======================================")
print("   SISTEM TRANSAKSI TOKO    ")
print("======================================")

# Input Data Pelanggan
nama_1014 = input("Masukkan nama pelanggan: ")
status_1014 = input("Masukkan status pelanggan (member/non-member): ").lower()
total_belanja_1014 = float(input("Masukkan total belanja: Rp "))
jumlah_barang_1014 = int(input("Masukkan jumlah barang: "))
kode_promo_1014 = input("Masukkan kode promo: ").upper()

# Data promo
daftar_promo_1014 = ["Hemat10", "Hemat20", "GratisOngkir"]
promo_tersedia_1014 = kode_promo_1014 in daftar_promo_1014
promo_tidak_tersedia_1014 = kode_promo_1014 not in daftar_promo_1014

# Operator Perbandingan
syarat_belanja_1014 = total_belanja_1014 >= 200000
syarat_barang_1014 = jumlah_barang_1014 >= 3
status_member_1014 = status_1014 == "member"

# Operator logika
diskon_member_1014 = status_member_1014 and syarat_belanja_1014
promo_1014 = syarat_belanja_1014 and promo_tersedia_1014
akses_umum_1014 = status_member_1014 and promo_tersedia_1014
bukan_member_1014 = not status_member_1014
mendapat_diskon_1014 = diskon_member_1014 

# Operator aritmatika
if diskon_member_1014:
    diskon_1014 = total_belanja_1014 * 10 / 100
else:
    diskon_1014 = 0
total_pembayaran_1014 = total_belanja_1014 - diskon_1014
if jumlah_barang_1014 > 0:
    rata_rata_harga_1014 = total_belanja_1014 / jumlah_barang_1014
else:
    rata_rata_harga_1014 = 0
sisa_bagi_1014 = jumlah_barang_1014 % 2

#  Operator penugasan
#untuk +=
poin_1014 = 0
poin_1014 += int(total_pembayaran_1014 / 10000) 

#untuk -=
stok_bonus_1014 = 10
if stok_bonus_1014:
    stok_bonus_1014 -= 1

# Operator identity
#untuk is dan is not
objek_1_1014 = ["member", 10]
objek_2_1014 = objek_1_1014
objek_3_1014 = ["member", 10]

identitas_sama_1014 = objek_1_1014 is objek_2_1014
identitas_berbeda_1014 = objek_1_1014 is not objek_3_1014
nilai_sama_1014 = objek_1_1014 == objek_3_1014

# operator bitwise
#untuk nilai bit:
# 0001 = Member
# 0010 = Belanja >= 200000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

kode_member_1014 = 0b0001 
kode_belanja_1014 = 0b0010 
kode_barang_1014 = 0b0100
kode_promo_bit_1014 = 0b1000

kode_status_1014 = 0

#operator or(|) unutk menggabungkan kondisi
if status_member_1014:
    kode_status_1014 = kode_status_1014 | kode_member_1014
if syarat_belanja_1014:
    kode_status_1014 = kode_status_1014 | kode_belanja_1014
if syarat_barang_1014:
    kode_status_1014 = kode_status_1014 | kode_barang_1014
if promo_tersedia_1014:
    kode_status_1014 = kode_status_1014 | kode_promo_bit_1014

#operator and (&) untuk memeriksa kondisi tertentu
cek_member_bit_1014 = kode_status_1014 & kode_member_1014
cek_belanja_bit_1014 = kode_status_1014 & kode_belanja_1014
cek_barang_bit_1014 = kode_status_1014 & kode_barang_1014
cek_promo_bit_1014 = kode_status_1014 & kode_promo_bit_1014

#oprator XOR (^) untuk membandingkan dua kode
kode_referensi_1014 = 0b1011
hasil_xor_1014 = kode_status_1014 ^ kode_referensi_1014

#opertaor shift kiri (<<)
hasil_shift_1014 = kode_status_1014 << 1

# Hak Akses Pelanggan
member_access_1014 = cek_member_bit_1014 == kode_member_1014
promo_access_1014 = cek_promo_bit_1014 == kode_promo_bit_1014

# free shipping jika memiliki promo GratisOngkir
free_shipping_1014 = kode_promo_1014 == "GratisOngkir"

if member_access_1014 and promo_access_1014:
    hak_akses_1014 = "Member + Promo"
elif member_access_1014:
    hak_akses_1014 = "Member"
elif promo_access_1014:
    hak_akses_1014 = "Promo"
else:
    hak_akses_1014 = "Umum"

# Ouput Data Pelanggan
print("\n==========================")
print("  DATA PELANGGAN  ")
print("============================")

print("nama pelanggan :", nama_1014)
print("status pelanggan :", status_1014)
print("total belanja_1014 : Rp", format(total_belanja_1014,".0f"))
print("jumlah barang :", jumlah_barang_1014)
print("kode promo :", kode_promo_1014)

# Hasil Validasi
print("\n==========================")
print("  HASIL VALIDASI  ")
print("============================")

print("belanja >= Rp200000 :", syarat_belanja_1014)
print("jumlah barang >= 3 :", syarat_barang_1014)
print("syarat member :", status_member_1014)
print("kode promo trsedia :", promo_tersedia_1014)
print("mendapatkan diskon :", mendapat_diskon_1014)
print("mendapatkan promo :", promo_1014)

# Hasil Perhitungan
print("\n==========================")
print("  HASIL PERHITUNGAN  ")
print("============================")

print("besarnya diskon : Rp", format(diskon_1014, ".0f"))
print("total pembayaran :Rp", format(total_pembayaran_1014, ".0f"))
print("rata-rata harga barang : Rp", format(rata_rata_harga_1014, ".0f"))
print("sisa jumlah barang / 2 :", sisa_bagi_1014)

# Hasil Operator Logika
print("\n==========================")
print("  OPERATOR LOGIKA  ")
print("============================")

print("member and belanja >= 200000 :", diskon_member_1014)
print("barang >= 3 and promo ada :", promo_1014)
print("member or promo ada :", akses_umum_1014)
print("not member :", bukan_member_1014)

# Operator Assignment
print("\n==========================")
print("  OPERATOR PENUGASAN  ")
print("============================")

print("poin pelanggan (+) :", poin_1014)
print("stok bonus (-) :", stok_bonus_1014)

# Operator Membership
print("\n==========================")
print("  OPERATOR PENUGASAN  ")
print("============================")

print("kode promo in daftar :", promo_tersedia_1014)
print("kode promo not in daftar :", promo_tidak_tersedia_1014)

# Operator identity
print("\n==========================")
print("  OPERATOR IDENTITY  ")
print("============================")

print("objek_1 is objek_2 :", identitas_sama_1014)
print("objek_1 is not objek_3 :", identitas_berbeda_1014)
print("objek_1 == objek_3 :", nilai_sama_1014)

# Operasi Bitwise
print("\n==========================")
print("  OPERATOR BITWISE  ")
print("============================")

print("kode status transaksi")
print("0001 = member")
print("0010 = belanja >= Rp200000")
print("0100 = jumlah barang >= 3")
print("1000 = kode promo tersedia")

print("\nKode Biner :", format(kode_status_1014, "04b"))
print("kode Desimal :", kode_status_1014)

print("\n--- Pemeriksaan Status ---")

print("\ncek member")
print(format(kode_status_1014, "04b"), "&", format(kode_member_1014, "04b"))
print("Hasil Biner :", format(cek_member_bit_1014, "04b"))
print("Hasil Desimal :", cek_member_bit_1014)

print("\nCek Belanja")
print(format(kode_status_1014, "04b"), "&", format(kode_belanja_1014, "04b"))
print("Hasil Biner :", format(cek_belanja_bit_1014, "04b"))
print("Hasil Desimal :", cek_belanja_bit_1014)

print("\nCek jumlah Barang")
print(format(kode_status_1014, "04b"), "&", format(kode_barang_1014, "04b"))
print("Hasil Biner :", format(cek_barang_bit_1014, "04b"))
print("Hasil Desimal :", cek_barang_bit_1014)

print("\nCek Promo")
print(format(kode_status_1014, "04b"), "&", format(kode_promo_bit_1014, "04b"))
print("Hasil Biner :", format(cek_promo_bit_1014, "04b"))
print("Hasil Desimal :", cek_promo_bit_1014)

print("\n---Perbandingan Status XOR ---")
print("Kode Transaksi :", format(kode_status_1014, "04b"))
print("Kode Referensi :", format(kode_referensi_1014, "04b"))
print(format(kode_status_1014, "04b"), "^", format(kode_referensi_1014, "04b"))
print("Hasil Biner :", format(hasil_xor_1014, "04b"))
print("Hasil Desimal :", hasil_xor_1014)

print("\n--- Shift ---")
print(format(kode_status_1014, "04b"), "<< 1")
print("Hasil Biner :", format(hasil_shift_1014))
print("Hasil Desimal :", hasil_shift_1014)

# Hak Akses
print("\n==========================")
print("  HAK AKSES PELANGGAN  ")
print("============================")

print("kode hak akses :", hak_akses_1014)
print("member accsess :", member_access_1014)
print("promo access :", promo_access_1014)
print(" free shipping accsess :", free_shipping_1014)

print("\n==========================")
print("  SELESAI  ")
print("============================")