# Login and Access Level

username = input("Enter username: ")
password = input("Enter password: ")

# Step 1: Check credentials (nested conditions)
login_ok = False
role = ""

if username == "admin":
    if password == "admin123":
        login_ok = True
        role = "Administrator"
elif username == "student12":
    if password == "study123":
        login_ok = True
        role = "Student"

# Step 2: Display result based on login status and role
print("\n----- Login Result -----")

if login_ok:
    print(f"Login successful. Welcome, {username}!")
    print(f"Role: {role}")

    if role == "Administrator":
        print("Full system access")
    elif role == "Teacher":
        print("Teacher access")
    else:
        print("Student access")
else:
    print("Invalid username or password")