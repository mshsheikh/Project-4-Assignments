import random

print("\n-- -- -- -- -- -- -- -- -- --")
print("      07 - IF STATEMENTS        ")
print("        Random Numbers          ")
print("-- -- -- -- -- -- -- -- -- --\n")

n: int = 10
min: int = 1
max: int = 100

for _ in range(n):  # Here _ is a throwaway variable
                    # It's like a universal "don’t care" symbol
    
    num = random.randint(min, max)
    print(num, end=' ')

print("\n")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
