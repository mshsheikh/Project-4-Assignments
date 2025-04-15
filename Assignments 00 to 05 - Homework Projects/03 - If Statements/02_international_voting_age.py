print("\n-- -- -- -- -- -- -- -- -- --")
print("      03 - IF STATEMENTS       ")
print("   International Voting Age    ")
print("-- -- -- -- -- -- -- -- -- --\n")

Peturksbouipo_Age = 16
Stanlau_Age = 25
Mayengua_Age = 48

user_age = int(input("How old are you? "))

if user_age >= Peturksbouipo_Age:
    print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo_Age}.")
else:
    print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo_Age}.")

if user_age >= Stanlau_Age:
    print(f"You can vote in Stanlau where the voting age is {Stanlau_Age}.")
else:
    print(f"You cannot vote in Stanlau where the voting age is {Stanlau_Age}.")

if user_age >= Mayengua_Age:
    print(f"You can vote in Mayengua where the voting age is {Mayengua_Age}.")
else:
    print(f"You cannot vote in Mayengua where the voting age is {Mayengua_Age}.")

footer_A: str = "\n\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
