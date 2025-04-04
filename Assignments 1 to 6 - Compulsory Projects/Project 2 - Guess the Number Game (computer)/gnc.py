# Guess The Number (Computer) - by mshsheikh

import random

print("\n-- -- -- -- -- -- -- -- -- -- -- -- --")
print("           GUESS THE NUMBER         ")
print(" Play with the computer and have fun! ")
print("-- -- -- -- -- -- -- -- -- -- -- -- --\n")

random_number = random.randint(1, 6)

## print(random_number)  # (CHEAT CODE) #

while True:
  print("""BOT 🤖: I have a number between 1 and 6.
        Can you guess it?""")
  user_guess : int = int(input("\nEnter your guess here: "))

  print(f"\nBOT 🤖: I thought {random_number}, and you guessed {user_guess}.")

  if user_guess < random_number:
    print("\nYour guess was too low!")
  elif user_guess > random_number:
    print("\nYour guess was too high!")

  else: print("\nYay! That's correct!")

  break

footer_A : str = "\nMade with ❤️  just for you!"
footer_B : str = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)
