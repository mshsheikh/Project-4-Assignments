print("\n-- -- -- -- -- -- -- --")
print("    04 - DICTIONARIES    ")
print("        Phonebook        ")
print("-- -- -- -- -- -- -- --\n")

phonebook: dict[str, str] = {}

while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":
        break

    number = input(f"Enter phone number for {name}: ")
    phonebook[name] = number

print("\nPhonebook Entries:")

for name in phonebook:
    print(f"{name}: {phonebook[name]}")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
