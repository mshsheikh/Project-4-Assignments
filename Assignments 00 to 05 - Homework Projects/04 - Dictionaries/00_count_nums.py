print("\n-- -- -- -- -- -- -- -- --")
print("    04 - DICTIONARIES       ")
print("     Count  Numbers         ")
print("-- -- -- -- -- -- -- -- --\n")

num_counts: dict[int, int] = {}

while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":
        break
    
    num = int(user_input)

    if num in num_counts:
        num_counts[num] += 1

    else:
        num_counts[num] = 1

print("\nResults:")
for num in num_counts:
    print(f"{num} appears {num_counts[num]} times.")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
