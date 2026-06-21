# Day 2 - Variables, Loops, Functions

# 1. Function to check even/odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))


# 2. Function to convert marks into grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

marks = int(input("Enter your marks (0-100): "))
print(f"Grade: {get_grade(marks)}")


# 3. While loop counting 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1


# 4. For loop - multiplication table
table_num = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")