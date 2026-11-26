schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

# 6a. Mencari hari dengan mata kuliah terbanyak
best_day = ""
max_courses = 0

for day, courses in schedule.items():
    if len(courses) > max_courses:
        best_day = day
        max_courses = len(courses)

print(f"Best day: {best_day} ({max_courses} courses)")

# 6b. Menghitung jumlah hari suatu mata kuliah muncul
course = input()
count = 0

for courses in schedule.values():
    if course in courses:
        count += 1

print(f"{course}: {count} days")