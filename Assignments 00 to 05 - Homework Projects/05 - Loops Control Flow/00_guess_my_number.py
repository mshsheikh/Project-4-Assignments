print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("        Guess My Number           ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

import random

print("Computer: I am thinking of a number between 0 and 99...")

secret_number = random.randint(1, 99)

# print(f"Secret number is: {secret_number}")

guess = None

while guess != secret_number:
    try:
        guess = int(input("User: "))
        
        if guess < 0 or guess > 99:
            print("Computer: Please enter a number between 0 and 99")
        elif guess < secret_number:
            print("Computer: Your guess is too low")
        elif guess > secret_number:
            print("Computer: Your guess is too high")
        else:
            print(f"Computer: Congrats! The number was: {guess}")
    except ValueError:
        print("Please enter a valid number")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
