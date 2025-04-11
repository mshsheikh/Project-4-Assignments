import math

print("\n-- -- -- -- -- -- -- -- --")
print("     01 - EXPRESSIONS ")
print("   Pythagorean  Theorem   ")
print("-- -- -- -- -- -- -- -- --\n")

AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))

# Hypotenuse² = AB² + AC²

BC = math.sqrt(AB**2 + AC**2) # Hypotenuse

print(f'\n"The length of BC (the hypotenuse) is: {BC}"')

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
