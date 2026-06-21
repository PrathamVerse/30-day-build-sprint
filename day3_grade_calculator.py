# Day 3 - Grade Calculator
# Takes marks for 5 subjects, stores in list + dict, calculates average and grade

subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
marks_dict = {}
marks_list = []

for subject in subjects:
    marks = int(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks
    marks_list.append(marks)

average = sum(marks_list) / len(marks_list)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n--- Report Card ---")
for subject, mark in marks_dict.items():
    print(f"{subject}: {mark}")

print(f"\nAverage: {average:.2f}")
print(f"Grade: {grade}")