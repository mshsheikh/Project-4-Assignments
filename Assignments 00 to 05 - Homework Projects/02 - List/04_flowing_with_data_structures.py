print("\n-- -- -- -- -- -- -- -- -- -- --")
print("          02 - LIST               ")
print("  Flowing with Data Structures    ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

message: str = input("Enter a message to copy: ")

messages: list[str] = ["Empty"]

print("\nList before:", messages)

messages.append(message)

print("List after:", messages)

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
