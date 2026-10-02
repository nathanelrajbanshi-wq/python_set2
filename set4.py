# ATM Withdrawal Validation

CORRECT_PIN = "1234"

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")

print("\n----- ATM Transaction -----")

if pin == CORRECT_PIN and amount > 0 and amount <= balance:
    remaining = balance - amount
    print("Status            : Withdrawal successful")
    print(f"Previous Balance  : Rs. {balance:.2f}")
    print(f"Amount Withdrawn  : Rs. {amount:.2f}")
    print(f"Remaining Balance : Rs. {remaining:.2f}")
elif pin != CORRECT_PIN:
    print("Status : Transaction failed - Invalid PIN")
elif amount <= 0:
    print(f"Status : Transaction failed - Invalid withdrawal amount (Rs. {amount:.2f})")
else:
    print("Status : Transaction failed - Insufficient balance")
    print(f"Available Balance : Rs. {balance:.2f}")