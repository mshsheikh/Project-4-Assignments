print("\n-- -- -- -- -- --")
print("    02 - LIST     ")
print("     Shorten      ")
print("-- -- -- -- -- --\n")

MAX_LENGTH = 3
user_list: list[str] = []

while True:
    item = input("Enter a value (or press Enter to finish): ")
    if item == "":
        break
    user_list.append(item)

print(f"\nOriginal list: {user_list}")

while len(user_list) > MAX_LENGTH:
    removed = user_list.pop()
    print(f"Removed: {removed}")

print(f"\nFinal list (max {MAX_LENGTH} items): {user_list}")

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
