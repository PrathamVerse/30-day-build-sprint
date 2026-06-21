# Day 4 - Exceptions, File Handling

import csv

# --- Part 1: Exception Handling Practice ---

# 1. Divide 100 by user input, handle errors
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")

# 2. Keep asking until valid input given
while True:
    try:
        num2 = int(input("Enter a valid number: "))
        print(f"Great, you entered {num2}")
        break
    except ValueError:
        print("That's not a number. Try again.")


# --- Part 2: CSV File Reader ---

# First, create a sample CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Pratham", 19, "Solan"])
    writer.writerow(["Aman", 20, "Delhi"])
    writer.writerow(["Riya", 21, "Mumbai"])
    writer.writerow(["Karan", 19, "Pune"])
    writer.writerow(["Simran", 22, "Chandigarh"])

# Now read the CSV file
ages = []
print("\n--- CSV Data ---")
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")
        ages.append(int(row["Age"]))

average_age = sum(ages) / len(ages)
print(f"\nAverage Age: {average_age:.2f}")