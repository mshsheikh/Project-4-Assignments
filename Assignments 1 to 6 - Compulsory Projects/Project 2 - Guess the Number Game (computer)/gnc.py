# Guess The Number (Computer) - by mshsheikh

import random

print("-- -- -- -- -- -- -- -- -- -- -- --")
print("          GUESS THE NUMBER         ")
print("  Play with computer and have fun! ")
print("-- -- -- -- -- -- -- -- -- -- -- --")

random_number = random.randint(1, 10)

user_guess = 0

while True:
  user_guess = int(input("Guess the number between 1 to 10: "))

  if user_guess < random_number:
    print("\nYour guess is too low!")
  elif user_guess > random_number:
    print("\nYour guess is too high!")

  else: print("\nYay! That's correct!")

  break

footer_A = "\nMade with ❤️  just for you!"
footer_B = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)