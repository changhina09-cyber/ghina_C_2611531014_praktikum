n = int(input())

kas = {}

for i in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])

    if nama not in kas:
        kas[nama] = nominal
    else:
        kas[nama] += nominal

total_cash = sum(kas.values())

top_name = ""
top_total = 0

for nama, total in kas.items():
    if total > top_total:
        top_name = nama
        top_total = total

for nama, total in kas.items():
    print(f"{nama}: {total}")

print(f"Total cash: {total_cash}")
print(f"Top contributor: {top_name} ({top_total})")