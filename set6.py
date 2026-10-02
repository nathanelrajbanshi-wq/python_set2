# Shopping Discount Calculator

name = input("Enter customer name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
member = input("Are you a member? (yes/no): ").strip().lower()

# Subtotal
subtotal = price * quantity

# Base discount based on subtotal
if subtotal >= 10000:
    discount_percent = 15
elif subtotal >= 5000:
    discount_percent = 10
elif subtotal >= 2000:
    discount_percent = 5
else:
    discount_percent = 0

# Additional member discount
member_bonus = 0
if member == "yes" and subtotal >= 5000:
    member_bonus = 5

total_percent = discount_percent + member_bonus
discount_amount = subtotal * total_percent / 100
final_amount = subtotal - discount_amount

# Output
print("\n----- Shopping Bill -----")
print(f"Customer Name     : {name}")
print(f"Product Price     : Rs. {price:.2f}")
print(f"Quantity          : {quantity}")
print(f"Member            : {member.capitalize()}")
print(f"Subtotal          : Rs. {subtotal:.2f}")
print(f"Base Discount     : {discount_percent}%")
print(f"Member Discount   : {member_bonus}%")
print(f"Total Discount    : {total_percent}% (Rs. {discount_amount:.2f})")
print(f"Final Amount      : Rs. {final_amount:.2f}")