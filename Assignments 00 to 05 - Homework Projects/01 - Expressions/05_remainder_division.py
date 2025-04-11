print("\n-- -- -- -- -- -- -- --")
print("    01 - EXPRESSIONS ")
print("  Remainder  Division   ")
print("-- -- -- -- -- -- -- --\n")

user_num1 = int(input("Enter a number to be divided: "))
user_num2 = int(input("Enter an number to divide by: "))

Q = user_num1 // user_num2
R = user_num1 % user_num2

print(f"""\nResults:
  Division is {Q} with a remainder of {R}.""")

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
