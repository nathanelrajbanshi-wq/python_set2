# Electricity Bill Calculator

units = float(input("Enter number of units consumed: "))

# Slab-based calculation
if units <= 20:
    bill = units * 5
elif units <= 50:
    bill = (20 * 5) + (units - 20) * 7
elif units <= 100:
    bill = (20 * 5) + (30 * 7) + (units - 50) * 10
else:
    bill = (20 * 5) + (30 * 7) + (50 * 10) + (units - 100) * 12

# Output
print("\n----- Electricity Bill -----")
print(f"Units Consumed : {units}")
print(f"Total Bill     : Rs. {bill:.2f}")