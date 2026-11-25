# Name: Ghina Ranianda Husni
# NIM: 2611531014
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = "Ghina Ranianda Husni"
nim = "2611531014"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]
print(username)
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().