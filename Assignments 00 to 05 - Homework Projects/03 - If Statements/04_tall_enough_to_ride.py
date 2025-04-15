print("\n-- -- -- -- -- -- -- -- -- -- --")
print("       06 - IF STATEMENTS         ")
print("      Tall Enough to Ride         ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

min_height = 50

user_height = input("""How tall are you?
Enter your height in inches: """)

if user_height:
    height = int(user_height)

    if height >= min_height:
        print("\nYou're tall enough to ride!")
        print("Enjoy :)")

    else:
        print("\nYou're not tall enough to ride!")
        print("Sorry :(")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
