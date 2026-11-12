# Name: Ghina Ranianda Husni
# NIM: 2611531014
# Question bonus

kalimat = input("Masukkan kalimat: ")
teks = kalimat.replace(" ", " ").lower()
if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")