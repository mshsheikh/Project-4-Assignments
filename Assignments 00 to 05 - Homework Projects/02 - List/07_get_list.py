print("\n-- -- -- -- -- -- --")
print("     02 - LIST        ")
print("     Get  List       ")
print("-- -- -- -- -- -- --\n")

user_list: list[str] = []

while True:
    item = input("Enter a value (or press Enter to finish): ")
    if item == "":
        break
    user_list.append(item)

print("\nHere’s the final list:")
print(user_list)

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
