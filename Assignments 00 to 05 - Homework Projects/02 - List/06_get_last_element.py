print("\n-- -- -- -- -- -- -- -- -- -- --")
print("           02 - LIST              ")
print("        Get Last Element          ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

num: int = int(input("""Computer: How many elements do you want to add to the list?
                     
User: """))

user_list: list[str] = []

for X in range(num):
    user_item = input(f"\nEnter element {X + 1}: ")
    user_list.append(user_item)

print(f"\nElement {num} in the list: {user_list[-1]}")

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
