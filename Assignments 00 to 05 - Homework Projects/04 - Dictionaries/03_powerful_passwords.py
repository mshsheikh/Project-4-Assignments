print("\n-- -- -- -- -- -- -- --")
print("   04 - DICTIONARIES     ")
print("  Powerful  Passwords    ")
print("-- -- -- -- -- -- -- --\n")

import hashlib

logins = {
    "abc@abc.com":
    hashlib.sha256("123".encode()).hexdigest(),

    "xyz@xyz.com":
    hashlib.sha256("456".encode()).hexdigest()
}

email    = input("Enter your email: ")
password = input("Enter your password: ")
hashed   = hashlib.sha256(password.encode()).hexdigest()

if logins.get(email) == hashed:
    print("\nLogin successful!")

else:
    print("\nLogin failed. Incorrect email or password.")

footer_A = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
