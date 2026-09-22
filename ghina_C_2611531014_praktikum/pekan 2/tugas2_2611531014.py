# SISTEM REGISTRASI PRAKTIKAN ALPRO 2026

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# Input data mahasiswa
nama = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
umur = int(input("Masukkan Umur            : "))
skor = float(input("Masukkan Skor Tes Awal   : "))

# Data alamat
alamat = """Gulai Bancah
    kec.mandiangin koto selayan
    kota Bukittinggi"""

# ID Token Sinyal
id_token = 100 + 3j

# Batas minimum kelulusan
batas_minimum = 75.0

# Menentukan status kelulusan
lulus = skor >= batas_minimum

# MENAMPILKAN DATA

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama, "| Tipe:", type(nama))
print("Jenis Kelamin  :", jenis_kelamin, "| Tipe:", type(jenis_kelamin))

print("Alamat Domisili:")
print(alamat, "| Tipe:", type(alamat))

print("Umur           :", umur, "tahun | Tipe:", type(umur))
print("Skor Tes Awal  :", skor, "| Tipe:", type(skor))
print("ID Token Sinyal:", id_token, "| Tipe:", type(id_token))

# STATUS KELULUSAN

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", batas_minimum)
print("Apakah Dinyatakan Lulus:", lulus, "| Tipe:", type(lulus))