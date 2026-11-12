text = "Informatika"
print(text[11])
print(text.upper)
print(text[0:20])

text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "aiueo":
        count = 1
print("Vowels:", count)