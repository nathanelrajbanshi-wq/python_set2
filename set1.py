name = input("Enter student name: ")
mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3
highest = max(mark1, mark2, mark3)
lowest = min(mark1, mark2, mark3)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print(f"Name          : {name}")
print(f"Total Marks   : {total:.2f}")
print(f"Average Marks : {average:.2f}")
print(f"Highest Mark  : {highest}")
print(f"Lowest Mark   : {lowest}")
print(f"Grade         : {grade}")