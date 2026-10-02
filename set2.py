# Number Analyzer

num = int(input("Enter an integer: "))

# a. Positive, negative, or zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# b. Even or odd
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

# c. Divisible by 3
if num % 3 == 0:
    div3 = "Yes"
else:
    div3 = "No"

# d. Divisible by 5
if num % 5 == 0:
    div5 = "Yes"
else:
    div5 = "No"

# e. Divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    div_both = "Yes"
else:
    div_both = "No"

# Output
print("\n----- Number Analysis -----")
print(f"Number                : {num}")
print(f"Sign                  : {sign}")
print(f"Even or Odd           : {parity}")
print(f"Divisible by 3        : {div3}")
print(f"Divisible by 5        : {div5}")
print(f"Divisible by 3 and 5  : {div_both}")