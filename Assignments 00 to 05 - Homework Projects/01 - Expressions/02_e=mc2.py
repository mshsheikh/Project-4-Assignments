print("\n-- -- -- -- -- -- --")
print("  01 - EXPRESSIONS ")
print("      e = mc²   ")
print("-- -- -- -- -- -- --\n")

print('''We're using Einstein's equation e = mc²\n''')

c = 299_792_458 # Speed of light in m/s

user_mass = float(input("Enter mass in Kilogram: "))

m = user_mass

E = m * c**2

print(f"""
e = energy in joules, which is {E}.
m = mass in kilograms, which is {m}.
c = speed of light in m/s, which is {c}.
""")

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
