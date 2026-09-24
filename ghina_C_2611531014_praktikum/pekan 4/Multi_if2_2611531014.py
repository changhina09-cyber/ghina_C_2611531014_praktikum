# Buat file dengan nama multi_if2_2611531014.py
# Buat program untuk kondisi if
# Nma variabel ditambah 4 digit nim terakhir contoh: ipk_1014
# Program ini menggunakan fungsi input()
# Program menghitung Diskon Belanja

# Input dari user
total_belanja_1014 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1014 = input("Apakah Anda member (y/t): ").strip().lower()
is_member_1014 = input_member_1014 in [ "y", "ya"]

#  Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya'
input_promo_1014 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1014 = input_promo_1014 in [ "y", "ya"]

total_diskon_persen_1014 = 0

# Multi-if terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1014 > 1000000:
    total_diskon_persen_1014 += 10  # Diskon belanja besar

if is_member_1014:
    total_diskon_persen_1014 += 5  # Diskon member

if kode_promo_valid_1014:
    total_diskon_persen_1014 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1014 = total_belanja_1014 * (total_diskon_persen_1014 / 100)
total_bayar_1014 = total_belanja_1014 - nominal_diskon_1014

# Output hasil 
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1014}% (Rp{nominal_diskon_1014:,.0f})")
print(f"Total bayar : Rp{total_bayar_1014:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_1014}%")
# Output Total diskon yang anda dapatkan: 30% jika belanja > 1 juta , member dan kode promo valid