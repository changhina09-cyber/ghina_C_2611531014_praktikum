all_students = input().split()
submitted = input().split()

all_set = set(all_students)
submitted_set = set(submitted)

submitted_count = len(all_set & submitted_set)
not_submitted = all_set - submitted_set

print("Submitted:", submitted_count, "students")
print("Not submitted:", len(not_submitted), "students")

for student in all_students:
    if student in not_submitted:
        print(student)