print("\n-- -- -- -- -- -- -- -- -- -- --")
print("       03 - IF STATEMENTS         ")
print("           Leap Year              ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

year: int = int(input("Enter a year to check: "))

# Conditions:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("\nThat's a leap year!")

else:
    print("\nThat's not a leap year.")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
