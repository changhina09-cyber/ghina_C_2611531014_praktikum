# tugas pekan 4 
# Struktur percabangan python

print("=== SISTEM LOKET ALPRO ADVANTURE PARK ===")

#1. INPUT DATA PENGUNJUNG
nama_1014 = input("Masukkan nama pengunjung :")
umur_1014 = int(input("input umur anda :"))
sim_1014 = input("Apakah anda sudah punya SIM C (y/t):") [0].lower()

print("\nPilihan paket Wahana (1-5):")
print(" 1. Safari Rimba (Rp 50,000)")
print(" 2. Arung Jeram  (Rp 75,000)")
print(" 3. Motor ATV Ekstrim (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp100,000)")
print(" 5. All-Accsess VIP (RP 220,000)")

paket_1014 = int(input("masukkan nomor paket (1-5) :"))
jumlah_tiket_1014 = int(input("masukkan jumlah tiket :" ))

# 2. IF TUNGGAL
#validasi jumlah tiket

if jumlah_tiket_1014 <= 0:
    print("Peringatan: Kuota tiket tidak valid")
    print("Program selesai.")
    exit()

# 3. MATCH-CASE
#menentukan jenis wahana dan harga

match paket_1014:
    case 1:
        nama_wahana_1014 = "Wahana Safari Rimba"
        harga_satuan_1014 = 50000
    case 2: 
        nama_wahana_1014 = "Wahana Arung Jeram"
        harga_satuan_1014 = 75000
    case 3:
        nama_wahana_1014 = "Wahana Motot ATV Ekstrim"
        harga_satuan_1014 = 120000
    case 4:
        nama_wahana_1014 = "Wahana Roller Coaster Kilat"
        harga_satuan_1014 = 100000
    case 5: 
        nama_wahana_1014 = "Wahana All_Accsess VIP"
        harga_satuan_1014 = 220000
    case _:
        print("paket wahana tidak valid")
        print("Program selesai.")
        exit()

# INPUT MEMBER DAN KODE PROMO
is_member_1014 = input("Apakah anda member? (y/t) :").strip().lower()
kode_promo_valid_1014 = input("Apakah kode promo valid? (y/t) :").strip().lower()

# 5.VALIDASI IZIN KENDALI WAHANA
#khusus paket 3 menggunakan if-elif-else

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_1014 == 3:
    if umur_1014 >= 17 and sim_1014 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_1014 >= 17 and sim_1014 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh" "bawa motor ATV (wajib didampingi instruktur).")
    elif umur_1014 < 17 and sim_1014 == 'y':
        print("Status Akses: identitas tidak valid:" "belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur" "dan tidak boleh bawa motor ATV.")

# Untuk paket selain 3 menggunakan if-else sederhana
else:
    if umur_1014 >= 10:
        print("Status Akses: Anda memenuhi batas usia wahana.")
    else:
        print("Status Akses: Anda belum memenuhi batas usia wahana.")

# 6. PERHITUNGAN SUBTOTAL
subtotal_1014 = harga_satuan_1014 * jumlah_tiket_1014

#variabel awal untuk menampung total diskon
total_diskon_persen_1014 = 0

# 7. MULTI-IF
#setiap if berdiri sendiri agar diskon dapat ditumpuk

#diskon belanja besar
if subtotal_1014 >= 200000:
    total_diskon_persen_1014 += 10
#diskon member
if is_member_1014 in ['y', 'ya']:
    total_diskon_persen_1014 += 5
#diskon voucher promo
if kode_promo_valid_1014 in ['y', 'ya']:
    total_diskon_persen_1014 += 15
#diskon tambahan rombongan
if jumlah_tiket_1014 >= 5:
    total_diskon_persen_1014 += 5

# 8. PERHITUNGAN TOTAL PEMBAYARAN
nominal_diskon_1014 = (subtotal_1014 * (total_diskon_persen_1014 / 100))
total_bayar_1014 = subtotal_1014 - nominal_diskon_1014

# 9. IF-ELSE UNTUK AUDIT TRANSAKSI
if total_bayar_1014 > 300000:
    catatan_layanan_1014 = ("Selamat! Anda berhak mendapatkan souvenir gratis.")
else:
    catatan_layanan_1014 = "Terima kasih telah berkunjung."

# 10. MENAMPILKAN RINCIAN PEMBAYARAN
print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung : {nama_1014}")
print(f"Wahana : {nama_wahana_1014}")
print(f"Jumlah Tiket : {jumlah_tiket_1014}")
print(f"Harga Satuan : Rp {harga_satuan_1014}")
print(f"Subtotal Belanja : Rp {subtotal_1014:,.0f}")
print(f"Total Diskon : {total_diskon_persen_1014}%" f"(Rp {nominal_diskon_1014:,.0f})")
print(f"Total Bayar : Rp {total_bayar_1014:,.0f}")
print(f"Catatan Layanan : {catatan_layanan_1014}")

print("\nProgram Selesai")