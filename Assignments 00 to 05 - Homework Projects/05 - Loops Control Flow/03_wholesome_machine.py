print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("          Affrimation             ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

affirmation = "I am capable of doing anything I put my mind to."

print("Computer: Please type the following affirmation:", affirmation)
user_input = input("\nUser: ")

while user_input != affirmation:
    print("\nComputer: That was not the affirmation.")
    print("\nComputer: Please type the following affirmation:", affirmation)
    user_input = input()

print("\nComputer: That's right! :)")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
