# Name: Ghina Ranianda Husni
# NIM: 2611531014
# Question 4

phone = "082611531014"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)
